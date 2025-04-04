import logging
from appium.webdriver.common.appiumby import AppiumBy
from src.mobileActions import MobileActions


class PrivacyAndPolicyPage(MobileActions):
    def __init__(self, driver):
        super().__init__(driver)

        self.PRIVACY_AND_POLICY_WELCOME_TEXT = '//android.view.View[@text="Privacy Policy regarding Honda RoadSync"]'
        self.PRIVACY_AND_POLICY_CHECKBOX_TEXT = '//android.widget.TextView[@text="I have read the Honda Privacy Policy."]'
        self.PRIVACY_AND_POLICY_CHECKBOX = '//android.widget.CheckBox'
        self.NEXT_BUTTON = '//android.widget.TextView[@text="Next"]'

    def PAPPage_terms_and_condition_heading_text(self):
        text = self.get_text(AppiumBy.XPATH, self.PRIVACY_AND_POLICY_WELCOME_TEXT)
        logging.info(f"📜 Extracted text: {text}")
        return text

    def PAPPage_terms_and_condition_heading_text_isVisible(self):
        isVisible = self.is_element_visible(AppiumBy.XPATH, self.PRIVACY_AND_POLICY_WELCOME_TEXT)
        if isVisible:
            logging.info(f"📜Is Privacy and Policy Heading Visible : {isVisible}")
            return True
        else:
            logging.info(f"📜Is Privacy and Policy Heading Visible : {isVisible}")
            return False

    def PAPPage_select_checkbox(self):
        logging.info("Selecting checkbox from the Privacy and Policy Page")
        self.click(AppiumBy.XPATH,self.PRIVACY_AND_POLICY_CHECKBOX)
        logging.info("Selected checkbox from the Privacy and Policy Page")


    def PAPPage_next_button_isSelected(self):
        is_enabled = self.is_element_selected(AppiumBy.XPATH,self.NEXT_BUTTON)
        logging.info({is_enabled})
        if is_enabled:
            logging.info("The checkbox is Clickable from the Terms and Services Page")
            return True
        else:
            logging.info("The checkbox is Not Clickable from the Terms and Services Page")
            return False

    def PAPPage_privacy_and_policy_checkbox_isSelected(self):
        is_Selected = self.is_element_selected(AppiumBy.XPATH,self.PRIVACY_AND_POLICY_CHECKBOX)
        if is_Selected:
            logging.info("The checkbox is Selected from the Privacy and Policy Page")
            return True
        else:
            logging.info("The checkbox is Not Selected from the Privacy and Policy Page")
            return False

    def PAPPage_terms_and_condition_checkbox_text_visible(self):
        isVisible = self.is_element_visible(AppiumBy.XPATH, self.PRIVACY_AND_POLICY_CHECKBOX_TEXT)
        if isVisible:
            logging.info(f"📜Is Privacy and Policy Heading Visible : {isVisible}")
            return isVisible
        else:
            logging.info(f"📜Is Privacy and Policy Heading Visible : False")
            return False






    def PAPPage_next_button_isEnabled(self):
        is_enabled = self.is_element_enabled(AppiumBy.XPATH, self.NEXT_BUTTON)
        if is_enabled:
            logging.info("The checkbox is Enabled from the Privacy and Policy Page")
            return True
        else:
            logging.info("The checkbox is Not Enabled from the Privacy and Policy Page")
            return False

    def PAPPage_click_next_button(self):
        logging.info("Clicking Next Button of Privacy and Policy Page")
        self.click(AppiumBy.XPATH, self.NEXT_BUTTON)
        logging.info("Clicked Next Button of Terms and Services Page")


    def PAPPage_terms_and_condition_Checkbox_IsChecked(self):
        isChecked = self.is_element_checked(AppiumBy.XPATH,self.PRIVACY_AND_POLICY_CHECKBOX)
        if isChecked:
            logging.info(" checkbox from the Privacy and Policy Page isChecked")
            return True
        else:
            logging.info(" checkbox from the Privacy and Policy Page isNotChecked")
            return False

