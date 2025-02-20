import unittest
from unittest.mock import patch

from PyQt5.QtCore import Qt
from PyQt5.QtTest import QTest
from PyQt5.QtWidgets import QApplication, QMessageBox

from src.user_interface.windows.Config_window import ConfigWindow


class TestConfigWindow(unittest.TestCase):
    def setUp(self):
        self.app = QApplication([])

    def tearDown(self):
        self.app.exit()

    @patch('src.configuration.Configuration.ConfigurationManager.load_config')
    def test_load_config(self, mock_load_config):
        mock_load_config.return_value = {
            "output_directory": "mock_directory",
            "output_file_name": "mock_file_name",
        }

        config_window = ConfigWindow()

        self.assertEqual(config_window.path_entry.text(), "mock_directory")
        self.assertEqual(config_window.name_entry.text(), "mock_file_name")

    @patch('src.configuration.Configuration.ConfigurationManager.update_config')
    def test_save_config(self, mock_update_config):
        config_window = ConfigWindow()

        config_window.path_entry.setText("new_directory")
        config_window.name_entry.setText("new_file_name")

        QTest.mouseClick(config_window.save_button, Qt.LeftButton)

        mock_update_config.assert_called_once_with({
            "output_directory": "new_directory",
            "output_file_name": "new_file_name",
        })

        self.assertEqual(config_window.result_file_path, "new_directory")
        self.assertEqual(config_window.result_file_name, "new_file_name")

    @patch('src.configuration.Configuration.ConfigurationManager.update_config', side_effect=Exception("Mock Error"))
    def test_save_config_exception(self, mock_update_config):
        config_window = ConfigWindow()

        config_window.path_entry.setText("new_directory")
        config_window.name_entry.setText("new_file_name")

        with patch.object(QMessageBox, 'exec_') as mock_msg_exec:
            QTest.mouseClick(config_window.save_button, Qt.LeftButton)

            mock_msg_exec.assert_called_once_with()

    @patch('PyQt5.QtWidgets.QFileDialog.getExistingDirectory', return_value='selected_directory')
    def test_browse_path(self, mock_get_existing_directory):
        config_window = ConfigWindow()

        QTest.mouseClick(config_window.path_browse_button, Qt.LeftButton)

        mock_get_existing_directory.assert_called_once_with(config_window, "Select Output Directory")
        self.assertEqual(config_window.path_entry.text(), "selected_directory")
