from google.cloud import tasks_v2
import logging

class Task():
    def __init__(self, project, location, queue, logger):
        self.client = tasks_v2.CloudTasksClient()
        self.parent = self.client.queue_path(project, location, queue)
        self.task = {
            'app_engine_http_request': {  # Specify the type of request.
                'http_method': tasks_v2.HttpMethod.POST
            }
        }
        self.logger= logger

    def add_task(self, resource, trace_header = None):
        uri = f'/{resource}'
        self.logger.info(f'Adding task with uri: {uri}', trace_header)
        self.task['app_engine_http_request']['relative_uri'] = uri
        response = self.client.create_task(parent=self.parent, task=self.task)
        print('Created task {}'.format(response.name))
        return response
