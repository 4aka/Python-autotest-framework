from env_preferences import load_env
import os


def get_env_variable(var_name: str):
    try:
        from env_preferences import load_env
        return load_env.get_from_env(var_name)
    except ImportError:
        return os.getenv(var_name)


BROWSER_NAME = get_env_variable('BROWSER_NAME')
BASE_URL = get_env_variable('BASE_URL')
UI_BASE_URL = get_env_variable('UI_BASE_URL')
LOG_LEVEL = get_env_variable('LOG_LEVEL')
API_KEY = get_env_variable('API_KEY')
PHONE_NUMBER = get_env_variable('PHONE_NUMBER')
NP_BASE_URL = get_env_variable('NP_BASE_URL')


# BASE_URL = load_env.get_from_env('BASE_URL')
# NP_BASE_URL = load_env.get_from_env('NP_BASE_URL')
# UI_BASE_URL = load_env.get_from_env('UI_BASE_URL')
# BROWSER_NAME = load_env.get_from_env('BROWSER_NAME')
# LOG_LEVEL = load_env.get_from_env('LOG_LEVEL')
# API_KEY = load_env.get_from_env('API_KEY')
# PHONE_NUMBER = load_env.get_from_env('PHONE_NUMBER')
