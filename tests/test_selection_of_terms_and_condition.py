import pytest
import logging
from locators.homePage import RoadSyncHomePage
from locators.terms_and_services_page import TermsAndServicesPage


@pytest.mark.usefixtures("driver")  # Ensures driver is available
class TestSelectionOfTermsAndCondition:
    """Test class for verifying region changes in the Honda RoadSync app."""

    @pytest.fixture(scope="class", autouse=True)
    def set_up(self, request, driver):
        request.cls.driver = driver
        request.cls.roadSyncH = RoadSyncHomePage(driver)
        request.cls.TASPage = TermsAndServicesPage(driver)

    @pytest.mark.order(3)
    def test_Terms_and_services_title_is_displayed(self):
        welcome_message = self.TASPage.TSAPage_terms_and_condition_welcome_text()
        logging.info(f"📢 Homepage message: {welcome_message}")

        assert welcome_message=='Terms of Service ', "❌ Terms and Condition message does not match!"
        logging.info("test_Terms_and_services_title_is_displayed Passed")

    @pytest.mark.order(4)
    def test_Is_next_button_enabled_without_selecting_checkbox(self):
        isCheckboxVisible = self.TASPage.TASPage_terms_and_condition_checkbox_text_visible()

        assert isCheckboxVisible, "Checkbox is not visible"
        logging.info("Checkbox is visible")

        isNextBtnVisible = self.TASPage.TSAPage_next_button_isSelected()
        logging.info({isNextBtnVisible})
        assert isNextBtnVisible==False, "Next button is clickable"

        logging.info("The Next button is not Enabled when we haven't selected the checkbox")
        logging.info("test_next_button_enabled_without_selecting_checkbox Passed")

    @pytest.mark.order(5)
    def test_select_checkbox_and_click_next_button(self):

        self.TASPage.TSAPage_select_checkbox()
        isCheckboxSelected = self.TASPage.TSAPage_terms_and_condition_Checkbox_IsChecked()
        assert isCheckboxSelected == True, "Terms and Condition Checkbox is Selected"

        isNextButtonSelected = self.TASPage.TSAPage_next_button_isEnabled()
        assert isNextButtonSelected == True, "Next button is Enabled"

        self.TASPage.TSAPage_click_next_button()

        logging.info("test_select_checkbox_and_click_next_button is Passed")