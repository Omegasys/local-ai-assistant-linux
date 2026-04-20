# test_utils.py
import unittest
from src.utils.encryption import Encryption
from src.utils.logger import Logger
import logging

class TestEncryption(unittest.TestCase):
    def setUp(self):
        """Set up the Encryption instance for testing."""
        self.encryption = Encryption()

    def test_encrypt_decrypt(self):
        """Test encryption and decryption."""
        data = "Test data"
        encrypted_data = self.encryption.encrypt(data)
        decrypted_data = self.encryption.decrypt(encrypted_data)
        self.assertEqual(decrypted_data, data)

    def test_encryption_key_save_load(self):
        """Test saving and loading encryption keys."""
        self.encryption.save_key('test_key.key')
        self.encryption.load_key('test_key.key')
        self.assertIsNotNone(self.encryption.key)

class TestLogger(unittest.TestCase):
    def setUp(self):
        """Set up the Logger instance for testing."""
        self.logger = Logger.get_logger()

    def test_logger_level(self):
        """Test setting the logger level."""
        logger = Logger.setup_logger(logging.INFO)
        self.assertEqual(logger.level, logging.INFO)

    def test_log_message(self):
        """Test if the logger can log messages."""
        with self.assertLogs(self.logger, level='INFO') as log:
            self.logger.info('Test log message')
            self.assertIn('Test log message', log.output[0])
