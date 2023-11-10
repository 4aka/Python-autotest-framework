import requests
from framework import LoadEnv as env
from dotenv import load_dotenv
import os
from os.path import join, dirname

class Request:

    @staticmethod
    def send_get_request(string_path):
        return requests.get(f"{env.get_from_env('API_URL')}{string_path}")


    @staticmethod
    def send_post_request(string_path, post_data):
        return requests.post(f"{env.get_from_env('API_URL')}{string_path}", post_data)


    @staticmethod
    def send_delete_request(string_path):
        return requests.delete(f"{env.get_from_env('API_URL')}{string_path}")