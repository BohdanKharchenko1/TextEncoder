from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QTextEdit, QStackedWidget, QDialog, \
    QMessageBox
from src.configuration.Configuration import ConfigurationManager
from src.logging.Logger import Logger
from src.user_interface.components.File_handler import FileHandler
from src.user_interface.components.Methods_handler import CodeHandler
from src.user_interface.windows.Config_window import ConfigWindow
from src.user_interface.windows.Manual_window import ManualButton


class Main_UI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.manual_button = None
        self.manual_handler = ManualButton(self)
        self.config_button = None
        self.switch_button = None
        self.setWindowTitle(" Encoder and Decoder ")

        self.logger = Logger()

        self.config_manager = ConfigurationManager()

        self.input_file_entry = QLineEdit(self)
        self.output_file_entry = QLineEdit(self)

        self.stacked_widget = QStackedWidget(self)
        self.log_text = QTextEdit(self)
        self.decoded_text = QTextEdit(self)

        self.stacked_widget.addWidget(self.log_text)
        self.stacked_widget.addWidget(self.decoded_text)

        self.stacked_widget.setCurrentWidget(self.log_text)

        self.decoded_text_content = ""

        self.encode_button = QPushButton("Encode", self)
        self.decode_button = QPushButton("Decode", self)
        self.browse_input_button = QPushButton("Browse", self)
        self.browse_output_button = QPushButton("Browse", self)

        self.input_label = QLabel("Input File:", self)
        self.output_label = QLabel("Output File:", self)

        # Pack widgets
        self.pack_widgets()
        self.resize(540, 300)

    def pack_widgets(self):
        try:
            self.input_label.setGeometry(10, 10, 100, 30)
            self.browse_input_button.setGeometry(120, 10, 80, 30)
            self.input_file_entry.setGeometry(210, 10, 300, 30)

            self.output_label.setGeometry(10, 50, 100, 30)
            self.browse_output_button.setGeometry(120, 50, 80, 30)
            self.output_file_entry.setGeometry(210, 50, 300, 30)

            self.stacked_widget.setGeometry(10, 90, 500, 150)
            self.encode_button.setGeometry(10, 250, 100, 30)
            self.decode_button.setGeometry(120, 250, 100, 30)

            # Configure log_text to be read-only
            self.log_text.setReadOnly(True)
            self.log_text.insertPlainText("Log messages will be displayed here...\n")

            # Connect button signals to functions
            self.browse_input_button.clicked.connect(
                lambda: FileHandler.browse_file('input', self.input_file_entry, self.output_file_entry))
            self.browse_output_button.clicked.connect(
                lambda: FileHandler.browse_file('output', self.input_file_entry, self.output_file_entry))
            self.encode_button.clicked.connect(
                lambda: CodeHandler.encode(self.input_file_entry.text(), self.config_manager, self.input_file_entry,
                                           self.output_file_entry, self.log, self.log_error))
            self.decode_button.clicked.connect(
                lambda: CodeHandler.decode(self.output_file_entry.text(), self.config_manager, self.output_file_entry,
                                           self.input_file_entry, self.show_decoded_text, self.log, self.log_error))

            self.config_button = QPushButton("Config", self)
            self.config_button.setGeometry(240, 250, 100, 30)
            self.config_button.clicked.connect(self.open_config_window)

            # Switch button
            self.switch_button = QPushButton("Switch", self)
            self.switch_button.setGeometry(350, 250, 100, 30)
            self.switch_button.clicked.connect(self.switch_text_view)

            self.manual_button = QPushButton("Manual", self)
            self.manual_button.setGeometry(455, 250, 80, 30)
            self.manual_button.clicked.connect(self.manual_handler.open_manual_window)
        except Exception as e:
            self.show_exception_message("Error in pack_widgets", e)

    def show_decoded_text(self, decoded_text):
        try:
            self.decoded_text.setPlainText(decoded_text)
            self.stacked_widget.setCurrentWidget(self.decoded_text)
        except Exception as e:
            self.show_exception_message("Error in show_decoded_text", e)

    def log(self, message):
        try:
            self.logger.log(message)
            self.log_text.append(message)
        except Exception as e:
            self.show_exception_message("Error in log", e)

    def log_error(self, message):
        try:
            self.logger.log_error(message)
            self.log_text.append(f"Error: {message}")
        except Exception as e:
            self.show_exception_message("Error in log_error", e)

    def open_config_window(self):
        try:
            config_window = ConfigWindow()
            result = config_window.exec_()

            if result == QDialog.Accepted:
                result_file_path = config_window.result_file_path
                result_file_name = config_window.result_file_name

                new_config = {
                    "output_directory": result_file_path,
                    "output_file_name": result_file_name
                }

                self.config_manager.update_config(new_config)
                self.log(f"Configuration saved: Path={result_file_path}, Name={result_file_name}")
        except Exception as e:
            self.show_exception_message("Error in open_config_window", e)

    def switch_text_view(self):
        try:
            current_index = self.stacked_widget.currentIndex()
            new_index = 1 - current_index  # Toggle between 0 and 1
            self.stacked_widget.setCurrentIndex(new_index)

            if new_index == 0:
                self.log_text.append(self.decoded_text_content)
        except Exception as e:
            self.show_exception_message("Error in switch_text_view", e)

    @staticmethod
    def show_exception_message(title, exception):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle(title)
        msg.setText(f"An error occurred: {str(exception)}")
        msg.exec_()
