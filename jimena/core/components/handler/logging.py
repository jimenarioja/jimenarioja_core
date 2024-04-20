"""
This module contains different logger handlers
Documentation: https://docs.python.org/3/library/logging.html
"""

import logging.config
from logging import Logger
from typing import Literal


class LoggingHandlerCore:
    """
    A class to manage logging configurations and logger instances.

    This class provides methods to configure logging using a dictionary-based configuration and retrieve logger
    instances.
    """

    def __init__(self):
        """
        Initialize LoggingHandler.

        Initializes the logger attribute as None.
        """
        self.logger = None

    @staticmethod
    def set_config():
        """
        Configure logging using a dictionary-based configuration.

        This method sets up logging using a predefined configuration dictionary LOGGER_CONFIG.
        """
        try:
            logging.config.dictConfig(LoggingHandlerCore.LOGGER_CONFIG)
        except Exception as e:
            raise e

    def get_logger(
        self,
        logger_name: Literal[
            "jimena-core-base", "jimena-core-advanced"
        ] = "jimena-core-base",
    ) -> Logger:
        """
        Get a logger instance with the specified name.

        If the logger with the specified name doesn't exist, it is created using the set_config method.

        :param logger_name: The name of the logger to retrieve.
        :type logger_name: Literal["jimena-core-base", "jimena-core-advanced"]
        :return: Logger instance with the specified name.
        :rtype: Logger
        """
        try:
            if not self.get_loggers().get(logger_name):
                LoggingHandlerCore.set_config()
            return logging.getLogger(logger_name)
        except Exception as e:
            raise e

    @staticmethod
    def get_loggers() -> dict:
        """
        Get all loggers registered in the root logger manager.

        :return: Dictionary containing all loggers registered in the root logger manager.
        :rtype: dict
        """
        try:
            return logging.root.manager.loggerDict
        except Exception as e:
            raise e

    # Constants
    LOGGER_BASIC_NAME = "jimena-core-base"
    LOGGER_BASIC_FORMATTER = (
        "%(asctime)s - %(filename)s - %(funcName)s - %(levelname)s - %(message)s"
    )
    LOGGER_ADVANCED_NAME = "jimena-core-advanced"
    LOGGER_ADVANCED_FORMATTER = "%(asctime)s - %(filename)s - %(module)s - %(funcName)s - %(threadName)s - %(levelname)s - %(message)s"
    LOGGER_BASIC_FORMATTER_DATE = "%Y-%m-%d %H:%M:%S"

    # config
    # TODO: to jimena-config or config file ( into resources folder )
    LOGGER_CONFIG = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "stream_formatter_basic": {
                "format": LOGGER_BASIC_FORMATTER,
                "datefmt": LOGGER_BASIC_FORMATTER_DATE,
            },
            "stream_formatter_advanced": {
                "format": LOGGER_ADVANCED_FORMATTER,
                "datefmt": LOGGER_BASIC_FORMATTER_DATE,
            },
        },
        "handlers": {
            "stream_handler_basic": {
                "level": "INFO",
                "formatter": "stream_formatter_basic",
                "class": "logging.StreamHandler",
            },
            "stream_handler_advanced": {
                "level": "DEBUG",
                "formatter": "stream_formatter_advanced",
                "class": "logging.StreamHandler",
            },
        },
        "loggers": {
            LOGGER_BASIC_NAME: {
                "handlers": ["stream_handler_basic"],
                "level": "INFO",
                "propagate": True,
            },
            LOGGER_ADVANCED_NAME: {
                "handlers": ["stream_handler_advanced"],
                "level": "DEBUG",
                "propagate": True,
            },
        },
    }
