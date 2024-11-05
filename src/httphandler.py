import requests


class HttpHandler:
    def __init__(self, url: str):
        self.url = url

    def get_status_code(self) -> int:
        return requests.get(self.url).status_code
