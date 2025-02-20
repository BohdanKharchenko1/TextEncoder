import unittest
from unittest.mock import patch
import os

from src.logging.Logger import Logger

class TestLogger(unittest.TestCase):
    def setUp(self):
        # Backup the existing log file if it exists
        self.log_file_path = "log/program_log.log"
        if os.path.exists(self.log_file_path):
            os.rename(self.log_file_path, self.log_file_path + ".backup")

    def tearDown(self):
        # Restore the original log file if backup exists
        backup_path = self.log_file_path + ".backup"
        if os.path.exists(backup_path):
            os.rename(backup_path, self.log_file_path)

    def test_configure_logger(self):
        # Test if the logger is configured properly
        logger = Logger()
        self.assertTrue(os.path.exists(logger.log_path))
        self.assertTrue(logger.log_path.endswith("program_log.log"))

    def test_log(self):
        # Test if log messages are written successfully
        logger = Logger()
        logger.log("Test log message")

        with open(logger.log_path, "r") as log_file:
            log_content = log_file.read()
            self.assertIn("Test log message", log_content)

    def test_log_error(self):
        # Test if error messages are written successfully
        logger = Logger()
        logger.log_error("Test error message")

        with open(logger.log_path, "r") as log_file:
            log_content = log_file.read()
            self.assertIn("Test error message", log_content)

    def test_log_exception_during_logging(self):
        # Test if an exception during logging is caught and printed
        logger = Logger()

        with patch("src.logging.Logger.logging.info", side_effect=Exception("Mocked Error")):
            with self.assertLogs(logger.log_path, level="ERROR") as log_context:
                logger.log("Test log message")

            self.assertIn("Error logging message: Mocked Error", log_context.output[0])

        with patch("src.logging.Logger.logging.error", side_effect=Exception("Mocked Error")):
            with self.assertLogs(logger.log_path, level="ERROR") as log_context:
                logger.log_error("Test error message")

            self.assertIn("Error logging error message: Mocked Error", log_context.output[0])
