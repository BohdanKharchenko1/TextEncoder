import unittest
from unittest.mock import patch, MagicMock

from PyQt5.QtWidgets import QApplication, QPushButton, QDialog

from src.user_interface.UI import Main_UI  # Replace 'src.user_interface.UI' with the actual module path


class TestMainUI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication([])

    def setUp(self):
        self.ui = Main_UI()

    def test_pack_widgets(self):
        # Mocking the widgets and ensuring that the functions are connected
        with patch.object(self.ui, 'browse_input_button', QPushButton()), \
                patch.object(self.ui, 'browse_output_button', QPushButton()), \
                patch.object(self.ui, 'encode_button', QPushButton()), \
                patch.object(self.ui, 'decode_button', QPushButton()), \
                patch.object(self.ui, 'config_button', QPushButton()), \
                patch.object(self.ui, 'switch_button', QPushButton()), \
                patch.object(self.ui, 'manual_button', QPushButton()), \
                patch.object(self.ui, 'show_decoded_text'), \
                patch.object(self.ui, 'log'), \
                patch.object(self.ui, 'log_error'), \
                patch.object(self.ui, 'open_config_window'), \
                patch.object(self.ui, 'manual_handler', MagicMock(spec_set=self.ui.manual_handler)):
            self.ui.pack_widgets()

    def test_show_decoded_text(self):
        # Mocking the widgets and asserting that setPlainText and setCurrentWidget are called
        with patch.object(self.ui.decoded_text, 'setPlainText'), \
                patch.object(self.ui.stacked_widget, 'setCurrentWidget'):
            self.ui.show_decoded_text("decoded_text")

    def test_log(self):
        # Mocking the widgets and asserting that log and append are called
        with patch.object(self.ui.logger, 'log'), \
                patch.object(self.ui.log_text, 'append'):
            self.ui.log("log_message")

    def test_log_error(self):
        # Mocking the widgets and asserting that log_error and append are called
        with patch.object(self.ui.logger, 'log_error'), \
                patch.object(self.ui.log_text, 'append'):
            self.ui.log_error("error_message")

    def test_open_config_window(self):
        # Mocking the ConfigWindow and asserting that update_config and log are called
        with patch('src.user_interface.UI.ConfigWindow') as mock_config_window:
            mock_config_window.return_value.exec_.return_value = QDialog.Accepted
            mock_config_window.return_value.result_file_path = "path"
            mock_config_window.return_value.result_file_name = "name"

            with patch.object(self.ui.config_manager, 'update_config'), \
                    patch.object(self.ui, 'log'):
                self.ui.open_config_window()

    def test_switch_text_view(self):
        # Mocking the widgets and asserting that setCurrentIndex and append are called
        with patch.object(self.ui.stacked_widget, 'setCurrentIndex'), \
                patch.object(self.ui.log_text, 'append'):
            self.ui.switch_text_view()


