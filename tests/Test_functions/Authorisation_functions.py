import time
from appium.webdriver.common.appiumby import AppiumBy

def positive_log_in(self):
    get_your_username = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'WelcomeGetYourUsernameButton')
    get_your_username.click()

    text = self.driver.find_element(AppiumBy.XPATH,
                                    '//android.view.ViewGroup[@content-desc="inputPhoneCode"]/android.widget.TextView').text

    if text == "🇷🇺 +7":
        pass
    else:
        select_county = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "inputPhoneCode")
        select_county.click()
        text_field = self.driver.find_element(AppiumBy.XPATH,
                                              "//android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.EditText")
        text_field.send_keys("ru")
        country = self.driver.find_element(AppiumBy.XPATH,
                                           "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup")
        country.click()
        time.sleep(3)

    enter_field = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "phoneInput")
    enter_field.click()

    enter_field.send_keys("9079999999")
    next_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "nextButton")
    next_button.click()

    time.sleep(1)
    code_screen_text = self.driver.find_element(AppiumBy.XPATH,
                                                "//android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[1]").text  # текст экрана ввода кода

    attempts = 0

    while True and attempts <= 5:
        if code_screen_text in self.driver.page_source:
            enter_code_field = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "phoneCodeInput")
            enter_code_field.click()
            enter_code_field.send_keys("1111")
            time.sleep(3)
            attempts += 1
            if attempts == 5:
                raise Exception("Too many attempts to enter a code")
        else:
            return False

    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "myProfileButton"), "Could not find main screen element."

def log_in(self):
    get_your_username = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'WelcomeGetYourUsernameButton')
    get_your_username.click()

    text = self.driver.find_element(AppiumBy.XPATH,
                                    '//android.view.ViewGroup[@content-desc="inputPhoneCode"]/android.widget.TextView').text

    if text == "🇷🇺 +7":
        pass
    else:
        select_county = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "inputPhoneCode")
        select_county.click()
        text_field = self.driver.find_element(AppiumBy.XPATH,
                                              "//android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.EditText")
        text_field.send_keys("ru")
        country = self.driver.find_element(AppiumBy.XPATH,
                                           "//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup")
        country.click()
        time.sleep(3)

    enter_field = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "phoneInput")
    enter_field.click()

    enter_field.send_keys("9079999998")
    next_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "nextButton")
    next_button.click()

    time.sleep(1)
    code_screen_text = self.driver.find_element(AppiumBy.XPATH,
                                                "//android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView[1]").text  # текст экрана ввода кода

    attempts = 0

    while True and attempts <= 5:
        if code_screen_text in self.driver.page_source:
            enter_code_field = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "phoneCodeInput")
            enter_code_field.click()
            enter_code_field.send_keys("1111")
            time.sleep(3)
            attempts += 1
            if attempts == 5:
                raise Exception("Too many attempts to enter a code")
        else:
            return False

    assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "myProfileButton"), "Could not find main screen element."

def log_out_main_screen(self):
    profile_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "myProfileButton")
    profile_button.click()

    settings_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "settings")
    settings_button.click()

    self.driver.swipe(start_x=500, start_y=1700, end_x=500, end_y=0, duration=1100)
    time.sleep(3)

    logout_button = self.driver.find_element(AppiumBy.XPATH,
                                             "//android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[5]")
    logout_button.click()

    android_logout = self.driver.find_element(AppiumBy.ID, "android:id/button1")
    android_logout.click()
    time.sleep(1)