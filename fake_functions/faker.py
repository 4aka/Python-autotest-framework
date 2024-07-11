import uuid
import random
import string
from faker import Faker

fake = Faker()


class Fake:

    @staticmethod
    def fake_guid():
        return str(uuid.uuid4())

    @staticmethod
    def fake_id():
        return int(fake.random_int(min=1, max=100))

    @staticmethod
    def fake_fixed_string(string_size):
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(characters) for _ in range(string_size))

    @staticmethod
    def fake_int():
        return int(fake.random_int(min=1, max=99999999999999999))
