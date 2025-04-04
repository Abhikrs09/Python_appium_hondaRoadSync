import os
import logging

class Config:
    def __init__(self):
        """Initialize configuration settings."""
        self.resources_dir = os.path.join(os.getcwd(), "Resources")
        self.apk_filename = "Honda_RoadSync.apk"
        self.apk_path = os.path.join(self.resources_dir, self.apk_filename)

        # Validate APK path
        if not os.path.exists(self.apk_path):
            logging.error(f"❌ APK file not found at: {self.apk_path}")
            raise FileNotFoundError(f"APK file not found: {self.apk_path}")

        logging.info(f"📁 APK Path: {self.apk_path}")

    def get_android_capabilities(self):
        """Returns a dictionary of desired capabilities for Android."""
        return {
            "platformName": "Android",
            "appium:automationName": "uiautomator2",
            "appium:deviceName": "Android",
            "appium:app": self.apk_path,
            "appium:appPackage": "com.honda.ms.dm.sab",
            "appium:appActivity": "com.drivemode.sab.home.HomeActivity",
            "appium:noReset": True,
            "appium:newCommandTimeout": 600,
            "appium:ignoreHiddenApiPolicyError": True,
            "appium:skipServerInstallation": True
        }
