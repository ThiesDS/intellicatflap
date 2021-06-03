import sys
import logging
import google.cloud.logging
from typing import Callable
from logging import FileHandler
from google.cloud.logging.handlers import CloudLoggingHandler
from datetime import datetime


# Logger config
FORMATTER = logging.Formatter("%(asctime)s|%(name)s|%(levelname)s|%(funcName)s:%(lineno)d|%(message)s")


# Define console handler
def get_console_handler() -> Callable:
    """
        Get console handler.
    """

    # Define console handler and formatting
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)

    return console_handler

# Define file handler
def get_file_handler(log_file_path: str, log_file_name: str) -> Callable:
    """
    Create a file_handler for logging
    """
    
    # Set log file name: timestamp for totday
    today = datetime.today()
    log_file_name = log_file_name.replace('<YYYYmmddHMS>', today.strftime('%Y%m%d%H%M%S'))

    # Define handler
    file_handler = FileHandler(log_file_path + log_file_name)
    file_handler.setFormatter(FORMATTER)
    return file_handler

# Define google cloud platform handler
def get_gcp_handler() -> Callable :
    """
        Get gcp handler for logging in gcp project 'intellifactflap'
    """

    # Define handler
    client = google.cloud.logging.Client(project="intellicatflap")
    cloud_handler = CloudLoggingHandler(client, name="intellicatflap_log")
    cloud_handler.setFormatter(FORMATTER)

    return cloud_handler

# Main function to get logger
def get_logger(name: str, log_level: str, log_file_path: str, log_file_name: str) -> Callable:
    """
        Main functionto get a logger with a specified log level. 
    """

    # Get logger
    logger = logging.getLogger(name)

    # Set log level
    if log_level == 'DEBUG':
        logger.setLevel(logging.DEBUG)
    elif log_level == 'INFO':
        logger.setLevel(logging.INFO)
    elif log_level == 'WARN':
        logger.setLevel(logging.WARN)
    elif log_level == 'ERROR':
        logger.setLevel(logging.ERROR)
    elif log_level  == 'CRITICAL':
        logger.setLevel(logging.CRITICAL)

    # Add handler
    logger.addHandler(get_console_handler())
    logger.addHandler(get_file_handler(log_file_path,log_file_name))
    logger.addHandler(get_gcp_handler())

    return logger

