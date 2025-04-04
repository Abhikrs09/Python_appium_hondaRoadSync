import os
import allure
import logging
from datetime import datetime


class TakeScreenshot:
    @staticmethod
    def clear_screenshots():
        """Clear all PNG screenshots in the 'Screenshots' directory."""
        screenshot_dir = os.path.join(os.getcwd(), "Screenshots")

        if not os.path.exists(screenshot_dir):
            logging.info("📂 No 'Screenshots' directory found. Skipping cleanup.")
            return

        png_files = [f for f in os.listdir(screenshot_dir) if f.endswith(".png")]
        if not png_files:
            logging.info("🗑️ No old screenshots to clear.")
            return

        for file in png_files:
            os.remove(os.path.join(screenshot_dir, file))

        logging.info(f"🗑️ Cleared {len(png_files)} old screenshots.")

    @staticmethod
    def capture(driver, test_name):
        """Capture a screenshot, save it to the 'Screenshots' directory, and attach it to Allure."""
        screenshot_dir = os.path.join(os.getcwd(), "Screenshots")
        os.makedirs(screenshot_dir, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_path = os.path.join(screenshot_dir, f"{test_name}_{timestamp}.png")

        try:
            if driver.save_screenshot(screenshot_path):
                logging.info(f"📸 Screenshot captured: {screenshot_path}")

                # ✅ Attach screenshot to Allure report
                with open(screenshot_path, "rb") as image:
                    allure.attach(image.read(), name=f"{test_name}_screenshot",
                                  attachment_type=allure.attachment_type.PNG)

                return screenshot_path
            else:
                logging.error("❌ Failed to capture screenshot. Driver may be inactive.")
                return None
        except Exception as e:
            logging.error(f"❌ Error capturing screenshot: {e}")
            return None
