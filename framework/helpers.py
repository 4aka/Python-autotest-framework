from dotenv import load_dotenv
import os
from os.path import join, dirname
import uuid
import random
import string
from faker import Faker


class Env:

    @staticmethod
    def get_from_env(key):
        dotenv_path = join(dirname(__file__), '..env')
        load_dotenv(dotenv_path)
        return os.environ.get(key)


class Fake:

    @staticmethod
    def fake_guid():
        return str(uuid.uuid4())

    @staticmethod
    def fake_id():
        fake = Faker()
        return int(fake.random_int(min=1, max=100))

    @staticmethod
    def fake_fixed_string(string_size):
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(characters) for _ in range(string_size))
