# file_manager.py
import os
import logging
import shutil

class FileManager:
    def __init__(self):
        self.home_directory = os.path.expanduser("~")

    def list_files(self, directory=None):
        """List files in the specified directory."""
        directory = directory or self.home_directory
        try:
            logging.info(f"Listing files in {directory}...")
            files = os.listdir(directory)
            for file in files:
                print(file)
        except FileNotFoundError:
            logging.error(f"Directory not found: {directory}")

    def open_file(self, file_path):
        """Open a file with the default system editor."""
        try:
            logging.info(f"Opening file: {file_path}")
            os.system(f"xdg-open {file_path}")
        except Exception as e:
            logging.error(f"Error opening file: {e}")

    def create_file(self, file_path, content=""):
        """Create a new file with the specified content."""
        try:
            with open(file_path, 'w') as f:
                f.write(content)
            logging.info(f"File created: {file_path}")
        except Exception as e:
            logging.error(f"Error creating file: {e}")

    def delete_file(self, file_path):
        """Delete a file."""
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
                logging.info(f"File deleted: {file_path}")
            else:
                logging.warning(f"File not found: {file_path}")
        except Exception as e:
            logging.error(f"Error deleting file: {e}")

    def move_file(self, src_path, dest_path):
        """Move a file from src to dest."""
        try:
            if os.path.exists(src_path):
                shutil.move(src_path, dest_path)
                logging.info(f"File moved from {src_path} to {dest_path}")
            else:
                logging.warning(f"Source file not found: {src_path}")
        except Exception as e:
            logging.error(f"Error moving file: {e}")
