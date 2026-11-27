
import requests

from config.config import BASE_URL, REQUEST_TIMEOUT


class APIClient:

    def __init__(self):
        self.base_url = BASE_URL
        self.timeout = REQUEST_TIMEOUT
        self.session = requests.Session()

    def get(self, endpoint, **kwargs):
        return self.session.get(
            f"{self.base_url}{endpoint}",
            timeout=self.timeout,
            **kwargs
        )

    def post(self, endpoint, **kwargs):
        return self.session.post(
            f"{self.base_url}{endpoint}",
            timeout=self.timeout,
            **kwargs
        )

    def put(self, endpoint, **kwargs):
        return self.session.put(
            f"{self.base_url}{endpoint}",
            timeout=self.timeout,
            **kwargs
        )

    def patch(self, endpoint, **kwargs):
        return self.session.patch(
            f"{self.base_url}{endpoint}",
            timeout=self.timeout,
            **kwargs
        )

    def delete(self, endpoint, **kwargs):
        return self.session.delete(
            f"{self.base_url}{endpoint}",
            timeout=self.timeout,
            **kwargs
        )

    def close(self):
        self.session.close()
