import os
import unittest

from src.configuration.Configuration import ConfigurationManager


class TestConfigurationManager(unittest.TestCase):
    def setUp(self):
        # Backup the existing config file if it exists
        self.config_file_path = "config/config.ini"
        if os.path.exists(self.config_file_path):
            os.rename(self.config_file_path, self.config_file_path + ".backup")

    def tearDown(self):
        # Restore the original config file if backup exists
        backup_path = self.config_file_path + ".backup"
        if os.path.exists(backup_path):
            os.rename(backup_path, self.config_file_path)

    def test_create_config_file(self):
        # Test if the config file is created properly
        config_manager = ConfigurationManager()
        self.assertTrue(os.path.exists(config_manager.config_path))
        self.assertTrue(config_manager.config_path.endswith("config.ini"))

    def test_load_config(self):
        # Test if config is loaded successfully
        config_manager = ConfigurationManager()
        config = config_manager.load_config()
        self.assertEqual(config["input_file"], "data/example.txt")
        self.assertEqual(config["output_file"], "compressed.bin")
        self.assertEqual(config["output_file_name"], "output_file")
        self.assertEqual(config["output_directory"], "data/")

    def test_update_config(self):
        # Test if config is updated successfully
        config_manager = ConfigurationManager()
        new_config = {
            "input_file": "new_input.txt",
            "output_file": "new_compressed.bin",
            "output_file_name": "new_output_file",
            "output_directory": "new_data/"
        }
        config_manager.update_config(new_config)
        updated_config = config_manager.load_config()
        self.assertEqual(updated_config["input_file"], "new_input.txt")
        self.assertEqual(updated_config["output_file"], "new_compressed.bin")
        self.assertEqual(updated_config["output_file_name"], "new_output_file")
        self.assertEqual(updated_config["output_directory"], "new_data/")
