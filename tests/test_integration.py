# test_integration.py
import unittest
from unittest.mock import patch
from src.core.assistant import Assistant
from src.modules.file_manager import FileManager
from src.modules.calendar import CalendarModule
from src.utils.encryption import Encryption

class TestIntegration(unittest.TestCase):
    @patch('src.modules.file_manager.FileManager.list_files')
    @patch('src.modules.calendar.CalendarModule.show_calendar')
    def test_assistant_integration(self, mock_show_calendar, mock_list_files):
        """Test the integration of multiple components."""
        # Mock behaviors
        mock_list_files.return_value = ['file1.txt', 'file2.txt']
        mock_show_calendar.return_value = "Mock Calendar Output"
        
        assistant = Assistant()
        
        # Test Assistant with integrated modules
        assistant.action_executor.execute("list files")
        mock_list_files.assert_called_once()

        assistant.action_executor.execute("show calendar")
        mock_show_calendar.assert_called_once()

    @patch('src.utils.encryption.Encryption.encrypt')
    @patch('src.utils.encryption.Encryption.decrypt')
    def test_encryption_integration(self, mock_decrypt, mock_encrypt):
        """Test encryption and decryption integration."""
        mock_encrypt.return_value = b'encrypted_data'
        mock_decrypt.return_value = 'Sensitive data'

        encryption = Encryption()
        encrypted_data = encryption.encrypt('Sensitive data')
        decrypted_data = encryption.decrypt(encrypted_data)

        self.assertEqual(decrypted_data, 'Sensitive data')
        mock_encrypt.assert_called_once_with('Sensitive data')
        mock_decrypt.assert_called_once_with(encrypted_data)
