
import logging
import os
from datetime import datetime

class Logger:
    @staticmethod
    def setup_logger():
        # Create 'logs' directory if it doesn't exist
        log_dir = os.path.join(os.getcwd(), "logs")
        os.makedirs(log_dir, exist_ok=True)

        # Generate timestamped log filename
        log_file = os.path.join(log_dir, f"test_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")

        # Clear any existing handlers to prevent duplicate logs
        if logging.getLogger().hasHandlers():
            logging.getLogger().handlers.clear()

        # Logging format
        log_format = "%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s"

        # Create a file handler (writes to the log file)
        file_handler = logging.FileHandler(log_file, mode='w', encoding='utf-8')
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(logging.Formatter(log_format))

        # Create a console handler (outputs to the terminal)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(logging.Formatter(log_format))

        # Configure the root logger
        logging.basicConfig(level=logging.INFO, handlers=[file_handler, console_handler])

        logging.info(f"📝 Logging initialized. Logs will be saved to: {log_file}")
