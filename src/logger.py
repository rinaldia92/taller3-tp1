import json

class Logger():
    def __init__(self, project):
        self.project = project
        self.global_log_fields = {}

    def _log(self, message, severity, trace_header = None):
        global_log_fields = {}
        
        if trace_header:
            trace = trace_header.split("/")
            global_log_fields[
                "logging.googleapis.com/trace"
            ] = f"projects/{self.project}/traces/{trace[0]}"

        entry = dict(
            severity=severity,
            message=message,
            **global_log_fields,
        )

        print(json.dumps(entry))

    def info(self, message, trace_header):
        self._log(message, 'INFO', trace_header)

    def debug(self, message, trace_header):
        self._log(message, 'DEBUG',trace_header)

    def error(self, message, trace_header):
        self._log(message, 'ERROR', trace_header)
