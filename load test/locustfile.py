from locust import HttpUser, TaskSet, task, between, LoadTestShape
from locust.contrib.fasthttp import FastHttpUser

def get_resources(client):
    client.get('/static/css/bootstrap.min.css')
    client.get('/static/css/style.css')
    client.get('/static/css/normalize.css')
    client.get('/static/css/animate.min.css')
    client.get('/static/css/owl.carousel.min.css')
    client.get('/static/css/meanmenu.css')
    client.get('/static/css/slick.css')
    client.get('/static/css/jquery-ui.css')
    client.get('/static/css/nice-select.css')
    client.get('/static/images/search_icon.png')
    client.get('/static/images/about.png')
    client.get('/static/images/uba.jpg')
    client.get('/static/images/favicon.ico')


class MyTasks(HttpUser):
    host = 'https://tp3-rinaldi-backup.uc.r.appspot.com'
    wait_time = between(1, 2.5)
    # network_timeout = 15.0
    # connection_timeout = 15.0

    @task(5)
    def home(self):
        self.client.get('/')
        get_resources(self.client)

    @task(4)
    def jobs(self):
        self.client.get('/jobs')
        get_resources(self.client)

    @task(2)
    def about(self):    
        self.client.get('/about')
        get_resources(self.client)

    @task
    def legals(self):
        self.client.get('/legals')
        get_resources(self.client)

class StagesShape(LoadTestShape):
    """
    A simply load test shape class that has different user and spawn_rate at
    different stages.
    Keyword arguments:
        stages -- A list of dicts, each representing a stage with the following keys:
            duration -- When this many seconds pass the test is advanced to the next stage
            users -- Total user count
            spawn_rate -- Number of users to start/stop per second
            stop -- A boolean that can stop that test at a specific stage
        stop_at_end -- Can be set to stop once all stages have run.
    """

    # stages = [
    #     {"duration": 180, "users": 100, "spawn_rate": 1},
    #     {"duration": 300, "users": 500, "spawn_rate": 10},
    #     {"duration": 600, "users": 1000, "spawn_rate": 10},
    #     {"duration": 800, "users": 300, "spawn_rate": 20},
    #     {"duration": 900, "users": 1000, "spawn_rate": 20},
    #     {"duration": 1100, "users": 1, "spawn_rate": 20},
    # ]



    stages = [
        {"duration": 30, "users": 50, "spawn_rate": 10},
        {"duration": 70, "users": 500, "spawn_rate": 30},
        {"duration": 120, "users": 1000, "spawn_rate": 50},
        {"duration": 350, "users": 2000, "spawn_rate": 50},
        {"duration": 450, "users": 300, "spawn_rate": 20},
        {"duration": 500, "users": 2000, "spawn_rate": 50},
        {"duration": 800, "users": 1, "spawn_rate": 20},
    ]


    def tick(self):
        run_time = self.get_run_time()

        for stage in self.stages:
            if run_time < stage["duration"]:
                tick_data = (stage["users"], stage["spawn_rate"])
                return tick_data

        return None
