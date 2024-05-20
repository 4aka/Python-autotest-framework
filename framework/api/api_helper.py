import requests
from framework import load_env as env


URL = env.get_from_env('API_URL')


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
        response = requests.post(f"{URL}{string_path}", body)
        return response

    @staticmethod
    def send_post_request_with_parameters(string_path, body):
        response = requests.post(f"{URL}{string_path}", body)
        return response

    @staticmethod
    def send_delete_request(string_path):
        response = requests.delete(f"{env.get_from_env('API_URL')}{string_path}")
        return response

    @staticmethod
    def send_put_request(string_path, body):
        response = requests.put(f"{env.get_from_env('API_URL')}{string_path}", data=body)
        return response

