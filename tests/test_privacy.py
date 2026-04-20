# test_privacy.py
import unittest
from src.core.privacy_manager import PrivacyManager

class TestPrivacyManager(unittest.TestCase):
    def setUp(self):
        """Set up the PrivacyManager instance for testing."""
        self.privacy_manager = PrivacyManager()

    def test_is_input_safe_valid(self):
        """Test that valid input is considered safe."""
        safe_input = "open file"
        self.assertTrue(self.privacy_manager.is_input_safe(safe_input))

    def test_is_input_safe_invalid(self):
        """Test that invalid input (e.g., sending data) is considered unsafe."""
        unsafe_input = "send data"
        self.assertFalse(self.privacy_manager.is_input_safe(unsafe_input))

    def test_encrypt_decrypt_data(self):
        """Test that encryption and decryption work correctly."""
        data = "Sensitive data"
        encrypted_data = self.privacy_manager.encrypt_data(data)
        decrypted_data = self.privacy_manager.decrypt_data(encrypted_data)
        self.assertEqual(decrypted_data, data)
