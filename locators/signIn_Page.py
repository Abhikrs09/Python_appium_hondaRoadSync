import logging
from appium.webdriver.common.appiumby import AppiumBy
from src.mobileActions import MobileActions


class SignInPage(MobileActions):
    def __init__(self, driver):
        super().__init__(driver)

        self.SIGN_IN_HEADING = '//android.widget.TextView[@text="Sign in to start"]'
        self.SIGN_IN_BUTTON = '//android.widget.TextView[@text="Sign in with Google"]'
        self.GOOGLE_PAGE_HEADING = '//android.view.View[@resource-id="logo"]'
        self.ENTER_USERNAME = '//android.view.View[@resource-id="yDmH0d"]/android.view.View[4]/android.view.View/android.view.View[1]/android.view.View[3]'
        self.GOOGLE_PAGE_NEXT_BUTTON = '//android.widget.Button[@text="NEXT"]'
        self.GOOGLE_PAGE_SHOW_PASSWORD = '//android.view.View[@resource-id="selectionc1"]'
        self.GOOGLE_PAGE_PASSWORD = '//android.view.View[@resource-id="password"]/android.view.View/android.view.View[2]/android.view.View'

    def 