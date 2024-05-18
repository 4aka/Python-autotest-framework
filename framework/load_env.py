from dotenv import load_dotenv
import os
from os.path import join, dirname


def get_from_env(key):
    dotenv_path = join(dirname(__file__), '..env')
    load_dotenv(dotenv_path)
    load_dotenv()
    return os.environ.get(key)