from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QDialog, QTextEdit, QMessageBox


class ManualButton:
    def __init__(self, parent):
        try:
            self.parent = parent
            self.manual_button = QPushButton("Manual", parent)
            self.manual_button.setGeometry(455, 250, 80, 30)
            self.manual_button.clicked.connect(self.open_manual_window)
        except Exception as e:
            self.show_exception_message("Error in ManualButton __init__", e)

    def open_manual_window(self):
        try:
            manual_dialog = QDialog(self.parent)
            manual_dialog.setWindowTitle("Manual")
            manual_dialog.resize(400, 300)

            manual_layout = QVBoxLayout(manual_dialog)

            manual_text = QTextEdit(manual_dialog)
            manual_text.setPlainText(
                "Welcome to the Encoder and Decoder!\n\n"
                "Instructions:\n"
                "- Choose input or output file using the 'Browse' buttons.\n"
                "- Before starting, ensure you've assigned your output folder and output file name in the configuration "
                "window (click 'Config').\n"
                "- Press 'Encode' to convert the input file.\n"
                "- Click 'Decode' to revert the output file.\n"
                "- Toggle between log and decoded text views with 'Switch.'\n"


            )
            manual_text.setReadOnly(True)

            manual_layout.addWidget(manual_text)

            manual_dialog.exec_()
        except Exception as e:
            self.show_exception_message("Error in ManualButton open_manual_window", e)

    @staticmethod
    def show_exception_message(title, exception):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle(title)
        msg.setText(f"An error occurred: {str(exception)}")
        msg.exec_()
