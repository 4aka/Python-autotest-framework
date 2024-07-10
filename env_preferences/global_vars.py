from env_preferences import load_env

BASE_URL = load_env.get_from_env('BASE_URL')
NP_BASE_URL = load_env.get_from_env('NP_BASE_URL')
UI_BASE_URL = load_env.get_from_env('UI_BASE_URL')
BROWSER_NAME = load_env.get_from_env('BROWSER_NAME')
LOG_LEVEL = load_env.get_from_env('LOG_LEVEL')
API_KEY = load_env.get_from_env('API_KEY')
PHONE_NUMBER = load_env.get_from_env('PHONE_NUMBER')
