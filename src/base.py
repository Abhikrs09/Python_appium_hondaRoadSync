# import time
#
# from appium.webdriver.common.appiumby import AppiumBy
# from selenium.common import ElementNotVisibleException, NoSuchElementException
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.support.expected_conditions import (
#     StaleElementReferenceException,
# )
# from selenium.webdriver.support.wait import WebDriverWait
#
#
# class BasePage:
#     """Wrapper for operations."""
#
#     def __init__(self, driver):
#         self.driver = driver
#         self.wait = WebDriverWait(self.driver,20,poll_frequency=2,
#                                   ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
#
#     def click(self, locator):
#         try:
#             el = self.wait.until(ec.element_to_be_clickable(locator))
#             el.click()
#         except TimeoutException:
#             print("Timeout Error!")
#         # time.sleep(2)
#
#     def fill_text(self, locator, txt):
#         try:
#             el = self.wait.until(ec.presence_of_element_located(locator))
#             el.send_keys(txt)
#         except TimeoutException:
#             print("Timeout Error!")
#         # time.sleep(2)
#
#     def is_elem(self, locator):
#         try:
#             el = self.wait.until(ec.presence_of_element_located(locator))
#             time.sleep(2)
#             return el
#         except TimeoutException:
#             print("Timeout Error!")
#             return None
#
#     def is_elem_displayed(self, locator) -> bool:
#         try:
#             el = self.wait.until(ec.presence_of_element_located(locator))
#             result = el.is_displayed()
#         except (StaleElementReferenceException, TimeoutException):
#             result = False
#         return result
#
#
#
#     def scroll_into_view_and_click(self, xpath):
#         try:
#             print(f"🔍 Scrolling to element with XPath: {xpath}")
#
#             self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
#                 f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().xpath("{xpath}"))'
#             )
#
#             el = self.wait.until(ec.element_to_be_clickable((AppiumBy.XPATH, xpath)))
#             el.click()
#             print(f"✅ Clicked on the element with XPath: {xpath}")
#
#         except TimeoutException:
#             print(f"❌ Timeout: Could not scroll to and click element with XPath: {xpath}")
#
