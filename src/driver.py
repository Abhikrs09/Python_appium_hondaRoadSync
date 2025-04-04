import logging
from appium.webdriver import Remote
from appium.options.common.base import AppiumOptions
from Utilities.configurations import Config

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class Driver:
    @staticmethod
    def get_android_driver():
        """Initializes and returns an Appium driver for Android."""
        config = Config()
        capabilities = config.get_android_capabilities()

        if not isinstance(capabilities, dict):
            logging.error("❌ Invalid capabilities format. Expected a dictionary.")
            raise ValueError("Capabilities should be a dictionary.")

        logging.info(f"📋 Android Capabilities: {capabilities}")

        try:
            options = AppiumOptions().load_capabilities(capabilities)
            app_driver = Remote("http://127.0.0.1:4723", options=options)
            logging.info("✅ Appium driver initialized successfully.")
            return app_driver
        except Exception as e:
            logging.error(f"❌ Failed to initialize Appium driver: {e}")
            raise
