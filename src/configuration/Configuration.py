import configparser
import os


class ConfigurationManager:
    def __init__(self, config_dir="config", config_file="config.ini"):
        try:
            self.config_dir = config_dir
            self.config_file = config_file
            self.config_path = os.path.join(self.config_dir, self.config_file)
            self._create_config_file()
        except Exception as e:
            print(f"Error during ConfigurationManager initialization: {str(e)}")

    def _create_config_file(self):
        try:
            if not os.path.exists(self.config_dir):
                os.makedirs(self.config_dir)

            if not os.path.exists(self.config_path):
                config = configparser.ConfigParser()
                config["DEFAULT"] = {
                    "input_file": "data/example.txt",
                    "output_file": "compressed.bin",
                    "output_file_name": "output_file",
                    "output_directory": "data/"
                }
                with open(self.config_path, "w") as configfile:
                    config.write(configfile)
        except Exception as e:
            print(f"Error creating config file: {str(e)}")

    def load_config(self):
        try:
            config = configparser.ConfigParser()
            config.read(self.config_path)
            return config["DEFAULT"]
        except Exception as e:
            print(f"Error loading config: {str(e)}")
            return {}

    def update_config(self, new_config):
        try:
            config = configparser.ConfigParser()
            config.read(self.config_path)

            for key, value in new_config.items():
                config["DEFAULT"][key] = str(value)

            with open(self.config_path, "w") as configfile:
                config.write(configfile)
        except Exception as e:
            print(f"Error updating config: {str(e)}")
