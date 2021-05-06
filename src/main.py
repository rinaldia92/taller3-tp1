from flask import Flask, request, render_template_string
import os
import logging

from counter import Counter
from task import Task
from my_html import get_html
from logger import Logger
from cache import Cache

app = Flask(__name__)

project = os.environ.get('PROJECT', 'tp3-rinaldi-backup')
location = os.environ.get('LOCATION', 'us-central1')
queue = os.environ.get('QUEUE', 'counter-task')

logger = Logger(project)
counter = Counter('Counter', 100, logger)
task = Task(project, location, queue, logger)
cache = Cache(10, logger)

host =f'https://{project}.uc.r.appspot.com'

@app.route('/')
def home():
    """Return home page"""
    trace_header = request.headers.get("X-Cloud-Trace-Context")
    logger.info('Getting home page', trace_header)
    task.add_task('home', trace_header)
    data = cache.get_data('home', trace_header)
    if not data:
        data = counter.get_by_key('home', trace_header)
        cache.set_data('home', data, trace_header)
    return render_template_string(get_html(host, 'home', data))

@app.route('/jobs')
def jobs():
    """Return jobs page"""
    trace_header = request.headers.get("X-Cloud-Trace-Context")
    logger.info('Getting jobs page', trace_header)
    task.add_task('jobs', trace_header)
    data = cache.get_data('jobs', trace_header)
    if not data:
        data = counter.get_by_key('jobs', trace_header)
        cache.set_data('jobs', data, trace_header)
    return render_template_string(get_html(host, 'jobs', data))

@app.route('/about')
def about():
    """Return about page"""
    trace_header = request.headers.get("X-Cloud-Trace-Context")
    logger.info('Getting about page', trace_header)
    task.add_task('about', trace_header)
    data = cache.get_data('about', trace_header)
    if not data:
        data = counter.get_by_key('about', trace_header)
        cache.set_data('about', data, trace_header)
    return render_template_string(get_html(host, 'about', data))

@app.route('/legals')
def legals():
    """Return legals page"""
    trace_header = request.headers.get("X-Cloud-Trace-Context")
    logger.info('Getting legals page', trace_header)
    task.add_task('legals', trace_header)
    data = cache.get_data('legals', trace_header)
    if not data:
        data = counter.get_by_key('legals', trace_header)
        cache.set_data('legals', data, trace_header)
    return render_template_string(get_html(host, 'legals', data))

@app.route('/home', methods = ['POST'])
def post_home():
    """Update home counter"""
    trace_header = request.headers.get("X-Cloud-Trace-Context")
    logger.info('Updating home counter', trace_header)
    counter.update_count('home',1, trace_header)
    return '', 204

@app.route('/jobs', methods = ['POST'])
def post_jobs():
    """Update jobs counter"""
    trace_header = request.headers.get("X-Cloud-Trace-Context")
    logger.info('Updating jobs counter', trace_header)
    counter.update_count('jobs',1, trace_header)
    return '', 204

@app.route('/about', methods = ['POST'])
def post_about():
    """Update about counter"""
    trace_header = request.headers.get("X-Cloud-Trace-Context")
    logger.info('Updating about counter', trace_header)
    counter.update_count('about',1, trace_header)
    return '', 204

@app.route('/legals', methods = ['POST'])
def post_legals():
    """Update legals counter"""
    trace_header = request.headers.get("X-Cloud-Trace-Context")
    logger.info('Updating legals counter', trace_header)
    counter.update_count('legals',1, trace_header)
    return '', 204

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)