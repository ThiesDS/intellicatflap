import sys
import logging
import google.cloud.logging
from typing import Callable
from google.cloud.logging.handlers import CloudLoggingHandler


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

# Define google cloud platform handler
def get_gcp_handler() -> Callable :
    """
        Get gcp handler for logging in gcp project 'intellifactflap'
    """

    # Define handler
    client = google.cloud.logging.Client(project="intellifactflap")
    cloud_handler = CloudLoggingHandler(client, name="intellicatflap_log")
    cloud_handler.setFormatter(FORMATTER)

    return cloud_handler

# Main function to get logger
def get_logger(name: str, log_level: str) -> Callable:
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
    logger.addHandler(get_gcp_handler())

    return logger

