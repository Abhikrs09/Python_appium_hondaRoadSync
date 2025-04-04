import pytest
import logging

from locators.services_agreement import ServicesAgreementPage

@pytest.mark.usefixtures("driver")
class TestServicesAgreement:

    @pytest.fixture(scope="class", autouse=True)
    def set_up(self, request, driver):
        request.cls.driver = driver
        request.cls.SAPage = ServicesAgreementPage(driver)

    @pytest.mark.order(9)
    def test_Service_Agreement_title_is_displayed(self):
        isHeadingVisible = self.SAPage.SAPage_Welcome_text_isVisible()
        assert isHeadingVisible==True, "Heading Text is not Visible."

        headingText = self.SAPage.SAPage_get_Welcome_text()
        assert headingText=='Service Agreement', "Heading Text is not Matching."
        logging.info("test_Service_Agreement_title_is_displayed Passed")

    @pytest.mark.order(10)
    def test_Is_next_button_enabled_without_selecting_both_checkbox(self):
        isLocatDataCheckboxChecked = self.SAPage.SAPage_locationData_checkbox_isChecked()
        assert isLocatDataCheckboxChecked==False,"The Location Data Checkbox is Checked"

        isPrivacyPolicyCheckboxChecked= self.SAPage.SAPage_privacyPolicy_checkbox_isChecked()
        assert isPrivacyPolicyCheckboxChecked==False,'The Privacy Policy Checkbox is Checked'

        isNextButtonClickable = self.SAPage.SAPage_next_button_isSelected()
        assert isNextButtonClickable==False,'The Next button From Service Agreement Page is Clickable'

        logging.info("test_Is_next_button_enabled_without_selecting_both_checkbox Passed")

    @pytest.mark.order(11)
    def test_Is_next_button_enabled_without_selecting_Only_locationData_checkbox(self):
        self.SAPage.SAPage_Select_location_data_checkbox()
        isLocatedDataCheckboxChecked = self.SAPage.SAPage_locationData_checkbox_isChecked()
        assert isLocatedDataCheckboxChecked == True, "The Location Data Checkbox is not Checked"

        isPrivacyPolicyCheckboxChecked = self.SAPage.SAPage_privacyPolicy_checkbox_isSelected()
        assert isPrivacyPolicyCheckboxChecked == False, 'The Privacy Policy Checkbox is Checked'

        isNextButtonClickable = self.SAPage.SAPage_next_button_isSelected()
        assert isNextButtonClickable == False, 'The Next button From Service Agreement Page is Clickable'
        self.SAPage.SAPage_Select_location_data_checkbox()

        logging.info("test_Is_next_button_enabled_without_selecting_Only_locationData_checkbox Passed")

    @pytest.mark.order(12)
    def test_Is_next_button_enabled_without_selecting_Only_privacyPolicy_checkbox(self):
        isLocatedDataCheckboxChecked = self.SAPage.SAPage_locationData_checkbox_isChecked()
        assert isLocatedDataCheckboxChecked == False, "The Location Data Checkbox is Checked"

        self.SAPage.SAPage_Select_privacyPolicy_checkbox()
        isPrivacyPolicyCheckboxEnabled = self.SAPage.SAPage_privacyPolicy_checkbox_isEnabled()
        assert isPrivacyPolicyCheckboxEnabled == True, 'The Privacy Policy Checkbox is Checked'

        isNextButtonClickable = self.SAPage.SAPage_next_button_isSelected()
        assert isNextButtonClickable == False, 'The Next button From Service Agreement Page is Clickable'
        self.SAPage.SAPage_Select_privacyPolicy_checkbox()

        logging.info("test_Is_next_button_enabled_without_selecting_Only_privacyPolicy_checkbox Passed")

    @pytest.mark.order(13)
    def test_Is_next_button_enabled_While_selecting_both_checkbox(self):
        self.SAPage.SAPage_Select_location_data_checkbox()
        isLocatedDataCheckboxChecked = self.SAPage.SAPage_locationData_checkbox_isChecked()
        assert isLocatedDataCheckboxChecked == True, "The Location Data Checkbox is not Checked"

        self.SAPage.SAPage_Select_privacyPolicy_checkbox()
        isPrivacyPolicyCheckboxChecked = self.SAPage.SAPage_privacyPolicy_checkbox_isChecked()
        assert isPrivacyPolicyCheckboxChecked == True, 'The Privacy Policy Checkbox is Checked'

        isNextButtonClickable = self.SAPage.SAPage_next_button_isEnabled()
        assert isNextButtonClickable == True, 'The Next button From Service Agreement Page is Not Enabled'

        self.SAPage.SAPage_click_next_button()

        logging.info("test_Is_next_button_enabled_While_selecting_both_checkbox Passed")
