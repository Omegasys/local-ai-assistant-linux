# test_assistant.py
import unittest
from src.core.assistant import Assistant
from unittest.mock import patch

class TestAssistant(unittest.TestCase):
    def setUp(self):
        """Set up the Assistant instance for testing."""
        self.assistant = Assistant()

    @patch('src.core.assistant.Assistant.get_user_input')
    @patch('src.core.assistant.Assistant.process_input')
    def test_start(self, mock_process_input, mock_get_user_input):
        """Test the assistant start method."""
        mock_get_user_input.return_value = "open file"
        mock_process_input.return_value = None

        # Test that the assistant starts and processes the input
        self.assistant.start()
        mock_get_user_input.assert_called_once()
        mock_process_input.assert_called_once_with("open file")

    @patch('src.core.assistant.Assistant.get_user_input')
    def test_get_user_input_text(self, mock_get_user_input):
        """Test getting user input via text."""
        mock_get_user_input.return_value = "set reminder"
        user_input = self.assistant.get_user_input()
        self.assertEqual(user_input, "set reminder")

    @patch('src.core.assistant.SpeechRecognition.listen')
    def test_get_user_input_speech(self, mock_listen):
        """Test getting user input via speech."""
        mock_listen.return_value = "shutdown system"
        user_input = self.assistant.get_user_input()
        self.assertEqual(user_input, "shutdown system")
