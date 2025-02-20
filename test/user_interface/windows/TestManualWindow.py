import unittest
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
from unittest.mock import patch

from src.user_interface.windows.Manual_window import ManualButton


class TestManualButton(unittest.TestCase):
    def setUp(self):
        self.app = QApplication([])

    def tearDown(self):
        self.app.exit()

    @patch('PyQt5.QtWidgets.QMessageBox.exec_')
    def test_open_manual_window(self, mock_msg_exec):
        manual_button = ManualButton(None)

        with patch.object(QDialog, 'exec_') as mock_dialog_exec:
            QTest.mouseClick(manual_button.manual_button, Qt.LeftButton)

            mock_dialog_exec.assert_called_once()
            mock_msg_exec.assert_not_called()

    @patch('PyQt5.QtWidgets.QDialog.exec_', side_effect=Exception("Mock Error"))
    @patch('PyQt5.QtWidgets.QMessageBox.exec_')
    def test_open_manual_window_exception(self, mock_msg_exec, mock_dialog_exec):
        manual_button = ManualButton(None)

        with patch.object(QMessageBox, 'exec_') as mock_exception_msg_exec:
            QTest.mouseClick(manual_button.manual_button, Qt.LeftButton)

            mock_exception_msg_exec.assert_called_once()
            mock_msg_exec.assert_not_called()
            mock_dialog_exec.assert_called_once()

    def test_show_exception_message(self):
        manual_button = ManualButton(None)

        with patch.object(QMessageBox, 'exec_') as mock_msg_exec:
            manual_button.show_exception_message("Test Title", Exception("Test Exception"))

            mock_msg_exec.assert_called_once_with()
