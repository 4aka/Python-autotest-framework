import requests
from env_preferences import global_vars


BASE_URL = global_vars.NP_BASE_URL


class Request:

    @staticmethod
    def send_post_request(body):
        body_dict = body.dict()
        response = requests.post(BASE_URL, json=body_dict)
        return response
