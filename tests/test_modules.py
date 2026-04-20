# test_modules.py
import unittest
from src.modules.file_manager import FileManager
from unittest.mock import patch
import os

class TestFileManager(unittest.TestCase):
    def setUp(self):
        """Set up the FileManager instance for testing."""
        self.file_manager = FileManager()

    @patch('os.listdir')
    def test_list_files(self, mock_listdir):
        """Test listing files in a directory."""
        mock_listdir.return_value = ['file1.txt', 'file2.txt']
        with patch('builtins.print') as mock_print:
            self.file_manager.list_files()
            mock_print.assert_called_with('file1.txt')
            mock_print.assert_called_with('file2.txt')

    @patch('os.remove')
    def test_delete_file(self, mock_remove):
        """Test deleting a file."""
        mock_remove.return_value = None
        self.file_manager.delete_file('/path/to/file.txt')
        mock_remove.assert_called_once_with('/path/to/file.txt')

    @patch('subprocess.run')
    def test_open_file(self, mock_run):
        """Test opening a file."""
        mock_run.return_value = None
        self.file_manager.open_file('/path/to/file.txt')
        mock_run.assert_called_once_with('xdg-open /path/to/file.txt', shell=True)

class TestCalendarModule(unittest.TestCase):
    def setUp(self):
        """Set up the CalendarModule instance for testing."""
        self.calendar = CalendarModule()

    @patch('subprocess.check_output')
    def test_show_calendar(self, mock_check_output):
        """Test showing the calendar."""
        mock_check_output.return_value = "Calendar Output"
        with patch('builtins.print') as mock_print:
            self.calendar.show_calendar()
            mock_print.assert_called_with("Calendar Output")
