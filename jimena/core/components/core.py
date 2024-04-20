import logging


class JCore:

    def __init__(self):
        """TODO to LoggerHandler"""
        self.logger = logging
        self.logger.basicConfig(
            level=logging.DEBUG, format="%(name)s - %(levelname)s - %(message)s"
        )

    def get_logger(self):
        return self.logger
