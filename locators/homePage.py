import logging
from appium.webdriver.common.appiumby import AppiumBy
from src.mobileActions import MobileActions


class RoadSyncHomePage(MobileActions):
    def __init__(self, driver):
        super().__init__(driver)

        self.WELCOME_MSG_TEXT = '//android.widget.TextView[@text="Welcome to Honda RoadSync!"]'
        self.CHANGE_REGION_BTN = '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]/android.widget.Button'
        self.SELECTED_COUNTRY_TEXT = '//android.widget.TextView[@text="India"]'
        self.CONTINUE_WITH_SELECTED_COUNTRY = '// android.view.View[ @ content - desc = "title_change_location"] / android.view.View[2] / android.widget.Button'
        self.CHANGE_REGION_BTN_TEXT = '//android.widget.TextView[@text="Change region of residence from India"]'
        self.CLICK_NEXT_BUTTON_HOMEPAGE = '//android.widget.TextView[@text="Next"]'
        self.CLICK_CHANGE_BUTTON = '//android.view.View[@content-desc="title_change_location"]/android.view.View[2]/android.widget.Button'

    def tap_change_button_for_selecting_country(self):
        logging.info("Taping the Change button")
        self.click(AppiumBy.XPATH, self.CLICK_CHANGE_BUTTON)
        logging.info("Tapped Change button")

    def click_change_button_from_selecting_country(self):
        logging.info("Clicking the Change button")
        self.click(AppiumBy.XPATH,self.CLICK_CHANGE_BUTTON)
        logging.info("Clicked Change button")


    def click_next_button_from_homepage(self):
        logging.info("Clicking the Continue button")
        self.click(AppiumBy.XPATH,self.CLICK_NEXT_BUTTON_HOMEPAGE)
        logging.info("Clicked the Continue button")

    def get_change_region_btn_text(self):
        text=self.get_text(AppiumBy.XPATH,self.CHANGE_REGION_BTN_TEXT)
        if 'India' in text:
            logging.info(f"📜 Extracted text: {text}")
            return "India"
        else:
            logging.info(f"Not able to extract Text from the Change Region button")


    def get_welcome_message(self):
        """Fetch the welcome message text."""
        text = self.get_text(AppiumBy.XPATH, self.WELCOME_MSG_TEXT)
        logging.info(f"📜 Extracted text: {text}")
        return text

    def click_change_region(self):
        logging.info("Clicking the 'Change Region' button.")
        self.click(AppiumBy.XPATH, self.CHANGE_REGION_BTN)
        logging.info("Clicked  'Change Region' button.")

    def select_country(self):
        """Scroll to and select a country."""
        # self.scroll_into_view_and_click(AppiumBy.XPATH, self.SELECT_COUNTRY_BTN)
        self.scroll_to_text_and_click('India')

    def get_selected_country_text(self):
        """Retrieve the selected country text."""
        text = self.get_text(AppiumBy.XPATH, self.SELECTED_COUNTRY_TEXT)
        logging.info(f"📜 Extracted text: {text}")
        return text

    def click_select_country_continue_button(self):
        self.click(AppiumBy.XPATH,self.CONTINUE_WITH_SELECTED_COUNTRY)
        logging.info(f"Continue  Button Clicked")