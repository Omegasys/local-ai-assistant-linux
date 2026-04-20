# logger.py
import logging

class Logger:
    @staticmethod
    def setup_logger(log_level=logging.DEBUG):
        """Sets up the logging configuration."""
        logging.basicConfig(
            format='%(asctime)s - %(levelname)s - %(message)s',
            level=log_level
        )
        logger = logging.getLogger()
        logger.setLevel(log_level)
        return logger

    @staticmethod
    def get_logger():
        """Returns the logger instance."""
        return logging.getLogger()
