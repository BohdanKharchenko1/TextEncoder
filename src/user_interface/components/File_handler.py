from PyQt5.QtWidgets import QFileDialog


class FileHandler:
    @staticmethod
    def browse_file(entry_type, input_file_entry, output_file_entry):
        try:
            file_path, _ = QFileDialog.getOpenFileName()

            if entry_type == 'input':
                input_file_entry.setText(file_path)
            elif entry_type == 'output':
                output_file_entry.setText(file_path)
        except Exception as e:
            # Handle the exception, you can log or show an error message here
            print(f"Error during file browsing: {str(e)}")
