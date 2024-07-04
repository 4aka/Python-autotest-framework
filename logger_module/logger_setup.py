import logging
from envs import global_vars as global_vars

log_level = global_vars.LOG_LEVEL


def setup_logger(name=__name__, log_file='pytest.log'):
    logger = logging.getLogger(name)
    level = logging.INFO

    if log_level == 'DEBUG':
        level = logging.DEBUG

    logger.setLevel(level)

    if not logger.handlers:
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(level)
        file_formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)
        console_formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
        console_handler.setFormatter(console_formatter)
        logger.addHandler(console_handler)

    return logger


def print(message: str):
    logger = setup_logger(name=__name__)

    if log_level == 'DEBUG':
        logger.debug(f'{message}')
    elif log_level == 'INFO':
        logger.info(f'{message}')
