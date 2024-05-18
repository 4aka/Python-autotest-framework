import requests
from framework import load_env as env
from dotenv import load_dotenv
from os.path import join, dirname

URL = env.get_from_env('API_URL')

class Request:

    @staticmethod
    def send_get_request(string_path):
        response = requests.get(f"{URL}{string_path}")
        return response


    @staticmethod
    def send_post_request(string_path, body):
        response = requests.post(f"{URL}{string_path}", body)
        return response


    @staticmethod
    def send_delete_request(string_path):
        response = requests.delete(f"{env.get_from_env('API_URL')}{string_path}")
        return response

    @staticmethod
    def send_put_request(string_path, body):
        response = requests.put(f"{env.get_from_env('API_URL')}{string_path}", body)
        return response

