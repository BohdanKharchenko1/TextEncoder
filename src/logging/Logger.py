import logging
import os


class Logger:
    def __init__(self, log_dir="log", log_file="program_log.log"):
        try:
            self.log_dir = log_dir
            self.log_file = log_file
            self.log_path = os.path.join(self.log_dir, self.log_file)
            self._configure_logger()
        except Exception as e:
            self.log_error(f"Error during logger initialization: {str(e)}")

    def _configure_logger(self):
        try:
            if not os.path.exists(self.log_dir):
                os.makedirs(self.log_dir)

            logging.basicConfig(
                filename=self.log_path,
                level=logging.INFO,
                format="%(asctime)s - %(levelname)s - %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S"
            )
        except Exception as e:
            self.log_error(f"Error configuring logger: {str(e)}")

    @staticmethod
    def log(message):
        try:
            logging.info(message)
        except Exception as e:
            print(f"Error logging message: {str(e)}")

    @staticmethod
    def log_error(message):
        try:
            logging.error(message)
        except Exception as e:
            print(f"Error logging error message: {str(e)}")
