import pytest
import logging

from locators.Privacy_and_policy_page import PrivacyAndPolicyPage
from locators.homePage import RoadSyncHomePage


@pytest.mark.usefixtures("driver")  # Ensures driver is available
class TestChangeRegions:
    """Test class for verifying region changes in the Honda RoadSync app."""

    @pytest.fixture(scope="class", autouse=True)
    def set_up(self, request, driver):
        request.cls.driver = driver
        request.cls.roadSyncH = RoadSyncHomePage(driver)
        request.cls.PAPPage = PrivacyAndPolicyPage(driver)

    @pytest.mark.order(6)
    def test_Terms_and_services_title_is_displayed(self):
        isVisible = self.PAPPage.PAPPage_terms_and_condition_heading_text_isVisible()
        assert isVisible==True,"Privacy and Policy Heading is not visible."

        welcome_message = self.PAPPage.PAPPage_terms_and_condition_heading_text()
        logging.info(f"📢 Homepage message: {welcome_message}")

        assert welcome_message == 'Privacy Policy regarding Honda RoadSync', "❌ Privacy and Policy Heading does not match!"
        logging.info("test_Terms_and_services_title_is_displayed Passed")


    @pytest.mark.order(7)
    def test_Is_next_button_enabled_without_selecting_checkbox(self):
        isCheckboxVisible = self.PAPPage.PAPPage_terms_and_condition_checkbox_text_visible()

        assert isCheckboxVisible, "Checkbox is not visible"


        isNextBtnSelected = self.PAPPage.PAPPage_next_button_isSelected()
        logging.info({isNextBtnSelected})
        assert isNextBtnSelected == False, "Next button is clickable"

        logging.info("The Next button is not Enabled when we haven't selected the checkbox")
        logging.info("test_Is_next_button_enabled_without_selecting_checkbox Passed")

    @pytest.mark.order(8)
    def test_select_checkbox_and_click_next_button(self):
        self.PAPPage.PAPPage_select_checkbox()
        isCheckboxSelected = self.PAPPage.PAPPage_terms_and_condition_Checkbox_IsChecked()
        assert isCheckboxSelected == True, "Terms and Condition Checkbox is Selected"

        isNextButtonSelected = self.PAPPage.PAPPage_next_button_isEnabled()
        assert isNextButtonSelected == True, "Next button is Enabled"

        self.PAPPage.PAPPage_click_next_button()

        logging.info("test_select_checkbox_and_click_next_button is Passed")