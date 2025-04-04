import logging
from appium.webdriver.common.appiumby import AppiumBy
from src.mobileActions import MobileActions


class ServicesAgreementPage(MobileActions):
    def __init__(self, driver):
        super().__init__(driver)

        self.SA_WELCOME_TEXT = '//android.widget.TextView[@text="Service Agreement"]'
        self.SA_LOCATION_DATA_CHECKBOX = '//android.widget.ScrollView/android.widget.CheckBox[1]'
        self.SA_PRIVACY_POLICY_CHECKBOX = '//android.widget.ScrollView/android.widget.CheckBox[2]'
        self.SA_NEXT_BUTTON = '//android.widget.TextView[@text="Next"]'

    def SAPage_Welcome_text_isVisible(self):
        isVisible = self.is_element_visible(AppiumBy.XPATH,self.SA_WELCOME_TEXT)
        if isVisible:
            logging.info("The Service Agreement Welcome Message is Visible")
            return True
        else:
            logging.info("The Service Agreement Welcome Message is not Visible")
            return False

    def SAPage_get_Welcome_text(self):
       message = self.get_text(AppiumBy.XPATH,self.SA_WELCOME_TEXT)
       logging.info(f"📜Heading Text for Service Agreement Page : {message}")
       return message

    def SAPage_locationData_checkbox_isChecked(self):
        isChecked= self.is_element_checked(AppiumBy.XPATH,self.SA_LOCATION_DATA_CHECKBOX)
        if isChecked:
            logging.info("The Location Data Checkbox is Checked or is Selected")
            return True
        else:
            logging.info("The Location Data Checkbox is Checked or is not Selected")
            return False

    def SAPage_Select_location_data_checkbox(self):
        logging.info("Selecting the LocationData Checkbox")
        self.click(AppiumBy.XPATH,self.SA_LOCATION_DATA_CHECKBOX)
        logging.info("Selected LocationData Checkbox")

    def SAPage_privacyPolicy_checkbox_isChecked(self):
        isChecked = self.is_element_checked(AppiumBy.XPATH, self.SA_LOCATION_DATA_CHECKBOX)
        if isChecked:
            logging.info("The Privacy Policy Checkbox is Checked or is Selected")
            return True
        else:
            logging.info("The Privacy Policy Checkbox is Checked or is not Selected")
            return False

    def SAPage_privacyPolicy_checkbox_isEnabled(self):
        isEnabled = self.is_element_enabled(AppiumBy.XPATH, self.SA_LOCATION_DATA_CHECKBOX)
        if isEnabled:
            logging.info("The Privacy Policy Checkbox is Enabled")
            return True
        else:
            logging.info("The Privacy Policy Checkbox is not enabled")
            return False

    def SAPage_privacyPolicy_checkbox_isSelected(self):
        isSelected = self.is_element_selected(AppiumBy.XPATH, self.SA_LOCATION_DATA_CHECKBOX)
        if isSelected:
            logging.info("The Privacy Policy Checkbox is Checked or is Selected")
            return True
        else:
            logging.info("The Privacy Policy Checkbox is Checked or is not Selected")
            return False

    def SAPage_Select_privacyPolicy_checkbox(self):
        logging.info("Selecting the privacyPolicy Checkbox")
        self.click(AppiumBy.XPATH,self.SA_PRIVACY_POLICY_CHECKBOX)
        logging.info("Selected privacyPolicy Checkbox")

    def SAPage_next_button_isSelected(self):
        isSelected = self.is_element_selected(AppiumBy.XPATH,self.SA_NEXT_BUTTON)
        if isSelected:
            logging.info("Next button is Selected")
            return True
        else:
            logging.info("Next button is not Selected")
            return False

    def SAPage_next_button_isClickable(self):
        isClickable = self.is_element_clickable(AppiumBy.XPATH,self.SA_NEXT_BUTTON)
        if isClickable:
            logging.info("Next button is Clickable")
            return True
        else:
            logging.info("Next button is not Clickable")
            return False

    def SAPage_next_button_isEnabled(self):
        isClickable = self.is_element_enabled(AppiumBy.XPATH,self.SA_NEXT_BUTTON)
        if isClickable:
            logging.info("Next button is Enabled")
            return True
        else:
            logging.info("Next button is not Enabled")
            return False

    def SAPage_click_next_button(self):
        logging.info("Clicking the next button from Services Agreement Page.")
        self.click(AppiumBy.XPATH,self.SA_NEXT_BUTTON)
        logging.info("Clicked the next button from Services Agreement Page.")