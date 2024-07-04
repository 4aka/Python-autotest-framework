import requests
from env_preferences import global_vars


BASE_URL = global_vars.BASE_URL


class Request:

    @staticmethod
    def send_get_request(string_path):
        response = requests.get(f"{URL}{string_path}")
        return response

    @staticmethod
    def send_get_request_with_parameters(string_path, parameters):
        response = requests.get(f"{URL}{string_path}", params=parameters)
        return response

    @staticmethod
    def send_post_request(string_path, body):
        response = requests.post(f"{BASE_URL}{string_path}", json=dict(body))
        return response

    @staticmethod
    def send_post_request_with_parameters(string_path, body):
        response = requests.post(f"{BASE_URL}{string_path}", json=dict(body))
        return response

    @staticmethod
    def send_delete_request(string_path: str):
        response = requests.delete(f"{BASE_URL}{string_path}")
        return response

    @staticmethod
    def send_put_request(string_path, body):
        response = requests.put(f"{BASE_URL}{string_path}", json=dict(body))
        return response
