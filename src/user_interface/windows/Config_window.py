from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFileDialog, QMessageBox
from src.configuration.Configuration import ConfigurationManager


class ConfigWindow(QDialog):
    def __init__(self):
        try:
            super().__init__()

            self.result_file_path = None
            self.result_file_name = None

            self.setWindowTitle("Configuration Window")
            self.setGeometry(100, 100, 400, 150)

            self.config_manager = ConfigurationManager()

            # Widgets
            self.path_label = QLabel("Output Directory:", self)
            self.path_entry = QLineEdit(self)
            self.path_browse_button = QPushButton("Browse", self)

            self.name_label = QLabel("Output File Name:", self)
            self.name_entry = QLineEdit(self)

            self.save_button = QPushButton("Save", self)
            self.cancel_button = QPushButton("Cancel", self)

            # Layout
            layout = QVBoxLayout(self)
            layout.addWidget(self.path_label)
            layout.addWidget(self.path_entry)
            layout.addWidget(self.path_browse_button)
            layout.addWidget(self.name_label)
            layout.addWidget(self.name_entry)
            layout.addWidget(self.save_button)
            layout.addWidget(self.cancel_button)

            # Connect signals
            self.path_browse_button.clicked.connect(self.browse_path)
            self.save_button.clicked.connect(self.save_config)
            self.cancel_button.clicked.connect(self.reject)

            # Load current configuration
            self.load_config()
        except Exception as e:
            self.show_exception_message("Error in ConfigWindow __init__", e)

    def browse_path(self):
        try:
            directory = QFileDialog.getExistingDirectory(self, "Select Output Directory")
            if directory:
                self.path_entry.setText(directory)
        except Exception as e:
            self.show_exception_message("Error in ConfigWindow browse_path", e)

    def load_config(self):
        try:
            config = self.config_manager.load_config()

            # Set current configuration values
            self.path_entry.setText(config.get("output_directory", ""))
            self.name_entry.setText(config.get("output_file_name", ""))
        except Exception as e:
            self.show_exception_message("Error in ConfigWindow load_config", e)

    def save_config(self):
        try:
            # Update configuration with new values
            new_config = {
                "output_directory": self.path_entry.text(),
                "output_file_name": self.name_entry.text(),
            }
            self.config_manager.update_config(new_config)

            # Set result variables for the main window
            self.result_file_path = new_config["output_directory"]
            self.result_file_name = new_config["output_file_name"]

            # Close the dialog
            self.accept()
        except Exception as e:
            self.show_exception_message("Error in ConfigWindow save_config", e)

    @staticmethod
    def show_exception_message(title, exception):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle(title)
        msg.setText(f"An error occurred: {str(exception)}")
        msg.exec_()
