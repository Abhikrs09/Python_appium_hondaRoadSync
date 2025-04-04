import pytest
import logging
from locators.homePage import RoadSyncHomePage


@pytest.mark.usefixtures("driver")  # Ensures driver is available
class TestChangeRegions:
    """Test class for verifying region changes in the Honda RoadSync app."""

    @pytest.fixture(scope="class", autouse=True)
    def set_up(self, request, driver):
        request.cls.driver = driver
        request.cls.roadSyncH = RoadSyncHomePage(driver)

    @pytest.mark.order(1)
    def test_homepage_welcome_message_is_displayed(self):
        """Verify that the welcome message is displayed on the homepage."""
        logging.info("🛠 Running test_homepage_welcome_message_is_displayed...")

        message = self.roadSyncH.get_welcome_message()
        logging.info(f"📢 Homepage message: {message}")

        assert message == "Welcome to Honda RoadSync!", "❌ Text does not match!"
        logging.info("✅ Homepage message test passed!")

    @pytest.mark.order(2)
    def test_changing_of_regions(self):
        """Test the ability to change regions and verify the selected country."""
        logging.info("🛠 Running test_changing_of_regions...")

        assert self.roadSyncH is not None, "❌ roadSyncH is None! Fixture might not be working."

        logging.info("📍 Navigating to Change Region page...")
        self.roadSyncH.click_change_region()
        logging.info("✅ Change Region page opened.")

        logging.info("🌍 Selecting a country...")
        self.roadSyncH.select_country()
        logging.info("✅ Country selected.")

        selected_country = self.roadSyncH.get_selected_country_text()
        logging.info(f"📢 Selected Country: {selected_country}")

        assert selected_country and selected_country.strip(), "❌ No country selected!"

        self.roadSyncH.click_change_button_from_selecting_country()

        country = self.roadSyncH.get_change_region_btn_text()
        assert country == 'India', '❌ Not able to fetch country from Change Region button'

        self.roadSyncH.click_next_button_from_homepage()
        logging.info("✅ Region change test passed!")

