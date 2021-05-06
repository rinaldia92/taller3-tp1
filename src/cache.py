from datetime import datetime, timedelta

class Cache():
    def __init__(self, duration, logger):
        self.duration = duration
        self.cache = {}
        self.logger = logger

    def get_data(self, key, trace_header = None):
        self.logger.info(f'Trying to get data of key {key}.', trace_header)
        data = self.cache.get(key, None)
        if not data:
            return data

        now = datetime.now()
        if data['expires_at'] > now:
            return data['payload']
        else:
            self.logger.info(f'Data of key {key} has expired.', trace_header)
            self.cache[key] = None
            return None
    
    def set_data(self, key, payload, trace_header = None):
        self.logger.info(f'Trying to set data of key {key}.', trace_header)
        now = datetime.now()
        expires_at = now + timedelta(0,self.duration)
        data = {
            'payload': payload,
            'expires_at': expires_at
        }
        self.cache[key] = data
    