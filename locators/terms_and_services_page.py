import logging
from appium.webdriver.common.appiumby import AppiumBy
from src.mobileActions import MobileActions


class TermsAndServicesPage(MobileActions):
    def __init__(self, driver):
        super().__init__(driver)

        self.TERMS_AND_CONDITION_WELCOME_TEXT = '//android.view.View[@text="Terms of Service "]'
        self.TERMS_AND_CONDITION_CHECKBOX_TEXT= '//android.widget.TextView[@text="I agree to the Honda Terms of Service."]'
        self.TERMS_AND_CONDITION_CHECKBOX = '//android.widget.CheckBox'
        self.NEXT_BUTTON = '//android.widget.TextView[@text="Next"]'

    def TSAPage_terms_and_condition_Checkbox_IsChecked(self):
        isChecked = self.is_element_checked(AppiumBy.XPATH,self.TERMS_AND_CONDITION_CHECKBOX)
        if isChecked:
            logging.info(" checkbox from the Terms and Services Page isChecked")
            return True
        else:
            logging.info(" checkbox from the Terms and Services Page isNotChecked")
            return False

    def TSAPage_terms_and_condition_welcome_text(self):
        text = self.get_text(AppiumBy.XPATH,self.TERMS_AND_CONDITION_WELCOME_TEXT)
        logging.info(f"📜 Extracted text: {text}")
        return text

    def TSAPage_terms_and_condtion_welocme_text_isVisible(self):
        isVisible = self.is_element_visible(AppiumBy.XPATH, self.TERMS_AND_CONDITION_WELCOME_TEXT)
        logging.info(f"📜 Extracted text: {isVisible}")
        return isVisible

    def TASPage_terms_and_condition_checkbox_text_visible(self):
        return self.is_element_visible(AppiumBy.XPATH,self.TERMS_AND_CONDITION_CHECKBOX_TEXT)

    def TSAPage_select_checkbox(self):
        logging.info("Selecting checkbox from the Terms and Services Page")
        self.click(AppiumBy.XPATH,self.TERMS_AND_CONDITION_CHECKBOX)
        logging.info("Selected checkbox from the Terms and Services Page")

    def TSAPage_terms_and_condition_checkbox_isSelected(self):
        is_Selected = self.is_element_selected(AppiumBy.XPATH,self.TERMS_AND_CONDITION_CHECKBOX)
        if is_Selected:
            logging.info("The checkbox is Selected from the Terms and Services Page")
            return True
        else:
            logging.info("The checkbox is Not Selected from the Terms and Services Page")
            return False

    def TSAPage_next_button_isEnabled(self):
        is_enabled = self.is_element_enabled(AppiumBy.XPATH,self.NEXT_BUTTON)
        if is_enabled:
            logging.info("The checkbox is Enabled from the Terms and Services Page")
            return True
        else:
            logging.info("The checkbox is Not Enabled from the Terms and Services Page")
            return False

    def TSAPage_next_button_isSelected(self):
        is_enabled = self.is_element_selected(AppiumBy.XPATH,self.NEXT_BUTTON)
        logging.info({is_enabled})
        if is_enabled:
            logging.info("The checkbox is Clickable from the Terms and Services Page")
            return True
        else:
            logging.info("The checkbox is Not Clickable from the Terms and Services Page")
            return False

    def TSAPage_click_next_button(self):
        logging.info("Clicking Next Button of Terms and Services Page")
        self.click(AppiumBy.XPATH,self.NEXT_BUTTON)
        logging.info("Clicked Next Button of Terms and Services Page")


