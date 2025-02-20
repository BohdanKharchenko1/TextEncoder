import os
from src.compression.logic.Decoder import Decoder
from src.configuration.Configuration import ConfigurationManager


def read_and_decode(input_file=None):
    try:
        config_manager = ConfigurationManager()
        config = config_manager.load_config()

        if not input_file:
            input_file = config.get("output_file")

        if not input_file:
            raise ValueError("Input file is not provided and default output file is not configured.")

        with open(input_file, "rb") as compressed_file:
            encoded_data_from_file = [int.from_bytes(compressed_file.read(2), byteorder='big') for _ in
                                      range(os.path.getsize(input_file) // 2)]

        decoder = Decoder()
        decoded_text = decoder.decode(encoded_data_from_file)
        return decoded_text
    except Exception as e:
        print(f"Error during reading and decoding: {str(e)}")
        return None
