from locust import HttpUser, TaskSet, task, between
class UserBehavior(TaskSet):

    @task
    def process_clothes(self):
        files = {'file': ('shirt.jpgg', open('/Users/onam-ui/Downloads/shirt.jpg', 'rb'), 'image/jpeg')}
        self.client.post("/clothes", files=files)

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)