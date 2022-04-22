import time

from appium.webdriver.common.appiumby import AppiumBy


def create_Large_broadcasting_room(self):

    start_room_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "mainFeedStartRoomButton")
    start_room_button.click()
    time.sleep(1)

    create_room_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "mainFeedStartRoomButton")
    create_room_button.click()

    phone_calls_permittion_allowance = self.driver.find_element(AppiumBy.ID,
                                                                "com.android.permissioncontroller:id/permission_allow_button")
    phone_calls_permittion_allowance.click()

    record_audio_permition_allowance = self.driver.find_element(AppiumBy.ID,
                                                                "com.android.permissioncontroller:id/permission_allow_foreground_only_button")
    record_audio_permition_allowance.click()