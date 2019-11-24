from locust import HttpLocust, TaskSet, task, between

class UserBehavior(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.login()

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        self.logout()

    def login(self):
        self.client.post("/users/login", {"username":"student", "password":"dev"})

    def logout(self):
        self.client.get("/users/logout")

    @task(1)
    def index(self):
        self.client.get("/")

    @task(2)
    def courses(self):
        self.client.get("/courses")

    @task(3)
    def course1(self):
        self.client.get("/courses/1")
    
    @task(4)
    def course1enroll(self):
        self.client.post("/courses/1/enroll")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_time = between(5, 9)