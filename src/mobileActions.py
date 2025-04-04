import logging

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException, NoSuchElementException, \
    ElementNotVisibleException
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



class MobileActions:
    """Base class for all mobile actions, including element interactions, gestures, and alerts."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20, poll_frequency=2,
                                  ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])

    # General Element Actions
    def click(self, locator_type, locator_value):
        """Clicks on an element when it becomes clickable."""
        try:
            el = self.wait.until(EC.element_to_be_clickable((locator_type, locator_value)))
            el.click()
        except TimeoutException:
            logging.error(f"❌ Timeout: Could not click on element {locator_value}")

    def fill_text(self, locator_type, locator_value, text):
        """Fills a text field with the given input."""
        try:
            el = self.wait.until(EC.presence_of_element_located((locator_type, locator_value)))
            el.clear()
            el.send_keys(text)
        except TimeoutException:
            logging.error(f"❌ Timeout: Could not fill text in element {locator_value}")

    def get_text(self, locator_type, locator_value):
        """Returns the text of a given element."""
        try:
            element = self.wait.until(EC.visibility_of_element_located((locator_type, locator_value)))
            element_text = element.text
            logging.info(f"📝 Element text: {element_text}")
            return element_text
        except TimeoutException:
            logging.error(f"❌ Timeout: Could not get text from element {locator_value}")
            return None

    def is_element_visible(self, locator_type, locator_value, timeout=10):
        """Checks if an element is visible."""
        try:
            self.wait.until(EC.visibility_of_element_located((locator_type, locator_value)))
            return True
        except TimeoutException:
            return False

    def is_element_selected(self, locator_type, locator_value, timeout=10):
        """Checks if an element is selected."""
        try:
            element = self.wait.until(EC.presence_of_element_located((locator_type, locator_value)))
            return element.is_selected()
        except TimeoutException:
            return False

    def is_element_enabled(self, locator_type, locator_value, timeout=10):
        """Checks if an element is enabled."""
        try:
            element = self.wait.until(EC.presence_of_element_located((locator_type, locator_value)))
            return element.is_enabled()
        except TimeoutException:
            return False

    def is_element_clickable(self, locator_type, locator_value, timeout=10):
        """Checks if an element is clickable."""
        element = self.wait.until(EC.element_to_be_clickable((locator_type, locator_value)))
        if element==True:
            return True
        else:
            return False

    def is_element_checked(self, locator_type, locator_value, timeout=10):
        """Checks if a checkbox or toggle button is checked."""
        try:
            element = self.wait.until(EC.presence_of_element_located((locator_type, locator_value)))
            return element.get_attribute("checked") == "true"
        except TimeoutException:
            return False

    # Scrolling & Gestures
    def scroll_into_view_and_click(self, locator_type, locator_value):
        """Scrolls to an element and clicks it."""
        try:
            element = self.wait.until(EC.presence_of_element_located((locator_type, locator_value)))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            element.click()
            logging.info(f"✅ Clicked on element {locator_value} after scrolling into view.")
        except TimeoutException:
            logging.error(f"❌ Timeout: Could not scroll to and click element {locator_value}")

    def swipe(self, start_x, start_y, end_x, end_y, duration=800):
        """Swipes from one coordinate to another."""
        pointer = PointerInput("touch", "finger")
        actions = ActionBuilder(self.driver, mouse=pointer)
        actions.pointer_action.move_to_location(start_x, start_y)
        actions.pointer_action.pointer_down()
        actions.pointer_action.move_to_location(end_x, end_y)
        actions.pointer_action.pointer_up()
        actions.perform()

    def tap(self, x, y):
        """Taps on the screen at specific coordinates."""
        pointer = PointerInput("touch", "finger")
        actions = ActionBuilder(self.driver, mouse=pointer)
        actions.pointer_action.move_to_location(x, y)
        actions.pointer_action.pointer_down()
        actions.pointer_action.pointer_up()
        actions.perform()

    # Alert Handling
    def handle_alert_accept(self):
        """Accepts an alert if present."""
        try:
            self.driver.switch_to.alert.accept()
        except Exception as e:
            logging.warning("No alert to accept: %s", e)

    def handle_alert_dismiss(self):
        """Dismisses an alert if present."""
        try:
            self.driver.switch_to.alert.dismiss()
        except Exception as e:
            logging.warning("No alert to dismiss: %s", e)

    def get_alert_text(self):
        """Retrieves text from an alert."""
        try:
            return self.driver.switch_to.alert.text
        except Exception as e:
            logging.warning("No alert to get text from: %s", e)
            return None

    def send_text_to_alert(self, text):
        """Sends text to an alert input field."""
        try:
            self.driver.switch_to.alert.send_keys(text)
        except Exception as e:
            logging.warning("Unable to send text to alert: %s", e)

    def scroll_to_text_and_click(self, text):
        """Scroll to a specific text and click it."""
        try:
            element = self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiScrollable(new UiSelector().scrollable(true)).scrollTextIntoView("{text}")'
            )
            if element:
                element.click()
                print(f"✅ Clicked on '{text}' successfully.")
        except Exception as e:
            print(f"❌ Could not find '{text}'. Error: {str(e)}")

    def scroll_up_down_by_pixels(self, pixels, direction="down", duration=1000):
        """
        Scroll up or down by a specified number of pixels.
        :param pixels: Number of pixels to scroll.
        :param direction: "down" for scrolling down, "up" for scrolling up.
        :param duration: Duration of the scroll action in milliseconds.
        """
        window_size = self.driver.get_window_size()
        start_x = window_size["width"] // 2  # Scroll from the center of the screen

        if direction == "down":
            start_y = int(window_size["height"] * 0.8)  # Start near the bottom
            end_y = start_y - pixels  # Move up
        elif direction == "up":
            start_y = int(window_size["height"] * 0.2)  # Start near the top
            end_y = start_y + pixels  # Move down
        else:
            print("❌ Invalid direction. Use 'up' or 'down'.")
            return

        self.driver.swipe(start_x, start_y, start_x, end_y, duration)
        print(f"✅ Scrolled {direction} by {pixels} pixels.")