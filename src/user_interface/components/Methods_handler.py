from src.compression.Decoding_and_displaying import read_and_decode
from src.compression.Encoding_and_saving import encode_and_save


class CodeHandler:
    @staticmethod
    def encode(input_file, config_manager, input_file_entry, output_file_entry, log_callback, log_error_callback):
        try:
            # Set default output_file_name and output_directory based on config
            output_file_name = config_manager.load_config().get("output_file_name") + ".bin"
            output_directory = config_manager.load_config().get("output_directory")

            encode_and_save(input_file, output_directory, output_file_name)
            log_callback("Encoding completed successfully.")
        except Exception as e:
            log_error_callback(f"Error during encoding: {str(e)}")
        finally:
            input_file_entry.clear()
            output_file_entry.clear()

    @staticmethod
    def decode(output_file, config_manager, output_file_entry, input_file_entry, show_decoded_text_callback,
               log_callback, log_error_callback):
        try:
            if not output_file:
                output_file = config_manager.load_config().get("output_file")

            decoded_text = read_and_decode(output_file)
            show_decoded_text_callback(decoded_text)  # Show decoded text in the designated field
            log_callback("Decoding completed successfully.")  # Log the success message
        except Exception as e:
            log_error_callback(f"Error during decoding: {str(e)}")
        finally:
            output_file_entry.clear()
            input_file_entry.clear()
