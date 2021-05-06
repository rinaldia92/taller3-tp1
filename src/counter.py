from google.cloud import datastore
from random import randint

class Counter():
    def __init__(self, kind, partitions, logger):
        self.ds = datastore.Client()
        self.kind = kind
        self.partitions = partitions
        self.logger = logger
    
    def _create(self, entity, partition):
        task = datastore.Entity(self.ds.key(self.kind, f'{entity}-{partition}'))
        task.update({
            'key': entity,
            'quantity': 1
        })
        self.ds.put(task)

    def get_by_key(self, key, trace_header = None):
        self.logger.info(f'Getting quantity of {key} visits', trace_header)
        with self.ds.transaction():
            query = self.ds.query(kind=self.kind)
            query.add_filter('key', '=', key)
            results = list(query.fetch())
            total = 1
            for e in results:
                total += e['quantity']
            return total

    def update_count(self, counter, cant, trace_header = None):
        self.logger.info(f'Updating {counter} counter in {cant}', trace_header)
        with self.ds.transaction():
            partition = randint(1, self.partitions)
            key = self.ds.key(self.kind, f'{counter}-{partition}')
            task = self.ds.get(key)
            if not task:
                self._create(counter, partition)
            else:
                task['quantity'] = task['quantity'] + cant
                self.ds.put(task)
        return task