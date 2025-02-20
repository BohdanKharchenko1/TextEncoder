import unittest
from unittest.mock import patch, MagicMock
from PyQt5.QtWidgets import QFileDialog

from src.user_interface.components.File_handler import FileHandler


class TestFileHandler(unittest.TestCase):
    def setUp(self):
        self.file_handler = FileHandler()

    @patch.object(QFileDialog, 'getOpenFileName', return_value=('selected_file.txt', ''))
    def test_browse_file_input(self, mock_get_open_file_name):
        # Mock input_file_entry and output_file_entry
        input_file_entry = MagicMock()
        output_file_entry = MagicMock()

        # Call the method
        self.file_handler.browse_file('input', input_file_entry, output_file_entry)

        # Assert that QFileDialog.getOpenFileName is called
        mock_get_open_file_name.assert_called_once_with()

        # Assert that input_file_entry.setText is called with the correct file path
        input_file_entry.setText.assert_called_once_with('selected_file.txt')

        # Assert that output_file_entry.setText is not called (since entry_type is 'input')
        output_file_entry.setText.assert_not_called()

    @patch.object(QFileDialog, 'getOpenFileName', return_value=('selected_file.txt', ''))
    def test_browse_file_output(self, mock_get_open_file_name):
        # Mock input_file_entry and output_file_entry
        input_file_entry = MagicMock()
        output_file_entry = MagicMock()

        # Call the method
        self.file_handler.browse_file('output', input_file_entry, output_file_entry)

        # Assert that QFileDialog.getOpenFileName is called
        mock_get_open_file_name.assert_called_once_with()

        # Assert that output_file_entry.setText is called with the correct file path
        output_file_entry.setText.assert_called_once_with('selected_file.txt')

        # Assert that input_file_entry.setText is not called (since entry_type is 'output')
        input_file_entry.setText.assert_not_called()



