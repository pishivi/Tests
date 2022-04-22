import time
from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from Authorisation_functions import *
from Create_room import create_Large_broadcasting_room




path = "/Users/pishivi/Desktop/apk/1.apk"
copied_link = ""

class TestRoomInviteLinks:

    def setup_method(self):
        desired_capabilities = {
            "platformName": "Android",
            "appium:platformversion": "11",
            "appium:deviceName": "f194a46f",
            "appium:app": path

        }

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_capabilities)
        self.driver.implicitly_wait(10)
        positive_log_in(self)
        create_Large_broadcasting_room(self)

    def test_room_invite_link_comparison(self):

        pick_into_the_room_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "InviteFriendToRoomButton")
        pick_into_the_room_button.click()

        copy_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID,'copyToBufferButtonPing')
        time.sleep(1)
        copy_button.click()
        link_from_copy_button = self.driver.get_clipboard_text()

        send_link_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "sendLinkButtonPing")
        time.sleep(2)
        send_link_button.click()
        sheet_copy_button = self.driver.find_element(AppiumBy.ID, "android:id/chooser_copy_button")
        sheet_copy_button.click()
        link_from_send_link_button = self.driver.get_clipboard_text()

        assert link_from_send_link_button == link_from_copy_button, "Links do not match"

    def test_room_invite_link_minimized_app(self):

        pick_into_the_room_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "InviteFriendToRoomButton")
        pick_into_the_room_button.click()

        copy_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID,'copyToBufferButtonPing')
        copy_button.click()
        copied_link = self.driver.get_clipboard_text()

        # close ping popup
        popup_head = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Bottom Sheet handle, Drag up or down to extend or minimize the Bottom Sheet").location
        time.sleep(5)
        self.driver.swipe(popup_head["x"], popup_head["y"], popup_head["x"], end_y=1200, duration=800)

        #log out
        minimize_room = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "collapseRoom")
        minimize_room.click()

        profile_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "myProfileButton")
        profile_button.click()

        settings_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID,"settings")
        settings_button.click()

        self.driver.swipe(start_x = 500, start_y = 1700, end_x = 500, end_y = 0, duration =1100)
        time.sleep(3)

        logout_button = self.driver.find_element(AppiumBy.XPATH, "//android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[5]")
        logout_button.click()

        android_logout = self.driver.find_element(AppiumBy.ID, "android:id/button1")
        android_logout.click()

        # tap on a link and login
        self.driver.press_keycode(3)
        self.driver.get(f'{copied_link}')

        log_in(self)

        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "shareScreenButton"), "No share screen available"

    def test_room_invite_link_terminated_app(self):

        pick_into_the_room_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "InviteFriendToRoomButton")
        pick_into_the_room_button.click()

        copy_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID,'copyToBufferButtonPing')
        copy_button.click()
        copied_link = self.driver.get_clipboard_text()

        # close ping popup
        popup_head = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Bottom Sheet handle, Drag up or down to extend or minimize the Bottom Sheet").location
        time.sleep(5)
        self.driver.swipe(popup_head["x"], popup_head["y"], popup_head["x"], end_y=1200, duration=800)

        #log out
        minimize_room = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "collapseRoom")
        minimize_room.click()

        profile_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "myProfileButton")
        profile_button.click()

        settings_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID,"settings")
        settings_button.click()

        self.driver.swipe(start_x = 500, start_y = 1700, end_x = 500, end_y = 0, duration =1100)
        time.sleep(3)

        logout_button = self.driver.find_element(AppiumBy.XPATH, "//android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[5]")
        logout_button.click()

        android_logout = self.driver.find_element(AppiumBy.ID, "android:id/button1")
        android_logout.click()
        time.sleep(1)

        # tap on a link and login
        self.driver.terminate_app("com.connect.club")
        time.sleep(1)
        self.driver.get(f'{copied_link}')

        log_in(self)

        assert self.driver.find_element(AppiumBy.ID, "com.connect.club:id/headerView"), "No share screen available"





