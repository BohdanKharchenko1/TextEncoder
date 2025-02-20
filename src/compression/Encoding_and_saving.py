from src.compression.logic.Encoder import Encoder
from src.configuration.Configuration import ConfigurationManager
import os


def encode_and_save(input_file=None, output_file=None, output_file_name=None):
    try:
        config_manager = ConfigurationManager()
        config = config_manager.load_config()

        if not input_file:
            input_file = config.get("input_file")

        if not output_file:
            output_file = config.get("output_file")

        if not output_file_name:
            output_file_name = config.get("output_file_name") + ".bin"

        with open(input_file, "r") as input_file:
            input_text = input_file.read()

        encoder = Encoder()
        encoded_data = encoder.encode(input_text)

        with open(os.path.join(output_file, output_file_name), "wb") as output_file:
            for code in encoded_data:
                output_file.write(code.to_bytes(2, byteorder='big'))
    except Exception as e:
        print(f"Error during encoding and saving: {str(e)}")
