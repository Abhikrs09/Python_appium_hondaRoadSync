# import pytest
# import logging
# import subprocess
# import time
# import allure
# from Utilities.logger import Logger
# from src.driver import Driver
# from Utilities.takeScreenshot import TakeScreenshot
# from Utilities.slack import slack_notify
#
#
# Logger.setup_logger()
#
# @pytest.fixture(scope="session", autouse=True)
# def appium_server():
#     logging.info("🚀 Starting the Appium server.")
#     server = subprocess.Popen(
#         [r'C:\Program Files\nodejs\node.exe', r'C:\Users\abhik\AppData\Roaming\npm\node_modules\appium\build\lib\main.js']
#     )
#     time.sleep(10)  # Allow time for Appium server to start
#     logging.info("✅ Appium server started successfully.")
#
#     TakeScreenshot.clear_screenshots()
#     logging.info("🧹 Old screenshots removed.")
#
#     yield
#
#     logging.info("🛑 Stopping the Appium server.")
#     server.terminate()
#     logging.info("✅ Appium server stopped.")
#
# @pytest.fixture(scope="class")
# def driver():
#     logging.info("📱 Initializing Appium driver.")
#     driver = Driver().getAndroidDriver()
#     yield driver
#     logging.info("🛑 Quitting Appium driver.")
#     driver.quit()
#
# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()
#
#     if report.when == "call" and report.failed:
#         test_name = item.name
#         error_msg = str(call.excinfo.value)
#
#         driver = item.funcargs.get("driver")
#         if driver:
#             screenshot_path = TakeScreenshot.capture(driver, test_name)
#
#             # ✅ Add screenshot as an Allure attachment
#             if screenshot_path:
#                 logging.info("📌 Attaching screenshot to Allure report.")
#                 pytest.allure.attach.file(screenshot_path, name="Failure Screenshot", attachment_type=pytest.allure.attachment_type.PNG)
#
#         slack_notify(f"❌ Test Failed: {test_name}\n\nError: {error_msg}")
#
# # ✅ Customize Allure report title
# def pytest_html_report_title(report):
#     report.title = "Android Automation Test Report"
#
# @pytest.hookimpl(optionalhook=True)
# def pytest_html_results_summary(prefix, summary, postfix):
#     prefix.extend([f"🗒️ Environment: Android | Appium 2.15.0"])
#     prefix.extend([f"📅 Test Run Time: {time.strftime('%Y-%m-%d %H:%M:%S')}"])



import pytest
import logging
import subprocess
import time
import allure
from Utilities.logger import Logger
from src.driver import Driver
from Utilities.takeScreenshot import TakeScreenshot
from Utilities.slack import slack_notify

Logger.setup_logger()

@pytest.fixture(scope="session", autouse=True)
def appium_server():
    logging.info("Starting the Appium server.")
    server = subprocess.Popen(
        [r'C:\Program Files\nodejs\node.exe', r'C:\Users\abhik\AppData\Roaming\npm\node_modules\appium\build\lib\main.js']
    )
    time.sleep(10)  # Allow time for Appium server to start
    logging.info(" Appium server started successfully.")

    TakeScreenshot.clear_screenshots()
    logging.info(" Old screenshots removed.")

    yield

    logging.info(" Stopping the Appium server.")
    server.terminate()
    logging.info("Appium server stopped.")

@pytest.fixture(scope="class")
def driver():
    logging.info("Initializing Appium driver.")
    driver = Driver.get_android_driver()
    yield driver
    logging.info(" Quitting Appium driver.")
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        test_name = item.name
        error_msg = str(call.excinfo.value)

        driver = item.funcargs.get("driver")
        if driver:
            screenshot_path = TakeScreenshot.capture(driver, test_name)

            # ✅ Add screenshot as an Allure attachment
            if screenshot_path:
                logging.info("\ud83d\udccc Attaching screenshot to Allure report.")
                allure.attach.file(screenshot_path, name="Failure Screenshot", attachment_type=allure.attachment_type.PNG)

        slack_notify(f"❌ Test Failed: {test_name}\n\nError: {error_msg}")

# ✅ Customize Allure report title
def pytest_html_report_title(report):
    report.title = "Android Automation Test Report"

@pytest.hookimpl(optionalhook=True)
def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([f"🗒️ Environment: Android | Appium 2.15.0"])
    prefix.extend([f"📅 Test Run Time: {time.strftime('%Y-%m-%d %H:%M:%S')}"])



