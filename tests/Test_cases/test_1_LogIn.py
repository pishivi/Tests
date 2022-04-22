import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from Authorisation_functions import positive_log_in


class TestLogIn:

    driver = ''
    def setup_method(self):
        desired_capabilities = {
            "platformName": "Android",
            "appium:platformversion": "11",
            "appium:deviceName": "f194a46f",
            "appium:app": "/Users/pishivi/Desktop/apk/1.apk"

        }

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_capabilities)
        self.driver.implicitly_wait(10)


    def test_positive_log_in(self):
        positive_log_in(self)

    def teardown_method(self):
        self.driver.quit()