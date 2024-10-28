from locust import HttpUser, task, between

class WebsiteTestUser(HttpUser):
    wait_time = between(0.5, 3.0)

    data = {"CHAS": {"0": 0}, "RM": {"0": 6.575}, "TAX": {"0": 296.0}, "PTRATIO": {"0": 15.3}, "B": {"0": 396.9},
            "LSTAT": {"0": 4.98}}
    @task(1)
    def test1(self):
        with self.client.get("https://udacity2.azurewebsites.net/", catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Failed to load page")
            else:
                print(f"GET response time: {response.elapsed.total_seconds()} seconds")

    @task(2)
    def test2(self):
        with self.client.post("https://udacity2.azurewebsites.net:443/predict", json=self.data, catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Failed to post data")
            else:
                print(f"POST response time: {response.elapsed.total_seconds()} seconds")