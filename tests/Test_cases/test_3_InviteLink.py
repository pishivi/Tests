from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from Authorisation_functions import positive_log_in




path = "/Users/pishivi/Desktop/apk/1.apk"
copied_link = ""

class TestInviteLinks:

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

    def test_main_banner_link_comparison(self):
        copy_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "copyToBufferButton")
        copy_button.click()
        link_from_copy_button = self.driver.get_clipboard_text()

        send_link_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "sendLinkButton")
        send_link_button.click()
        sheet_copy_button = self.driver.find_element(AppiumBy.ID, "android:id/chooser_copy_button")
        sheet_copy_button.click() #tap on copy button in androind bottom sheet
        link_from_send_link_button = self.driver.get_clipboard_text()

        assert link_from_send_link_button == link_from_copy_button, "Links do not match"
        self.copied_link = link_from_copy_button



    def test_tap_link_minimized_app(self):
        copy_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "copyToBufferButton")
        copy_button.click()
        copied_link = self.driver.get_clipboard_text() #save link
        self.driver.press_keycode(3) # press home button to minimize the app
        self.driver.get(f'{copied_link}') #tap a link

        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "usernameLabel"), "Wrong username or popup is closed"

    def test_tap_link_terminated_app(self):
        copy_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "copyToBufferButton")
        copy_button.click()
        copied_link = self.driver.get_clipboard_text() #save link

        self.driver.terminate_app("com.connect.club") #terminate the app
        self.driver.get(f'{copied_link}')
        assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "usernameLabel"), "Wrong username or popup is closed"


    # def test_tap_link_deleted_app(self):
    #
    #     self.driver.get(self.copied_link) #tap a link #ПРИЛОЖЕНИЕ УСТАНАВЛИВАЕТСЯ ДО ТОГО, КАК НАЧИНАЮТСЯ ЭТИ ДЕЙСТВИЯ. Разберись.
    #
    #     assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Open in the app..."), "Landing page is not open" #check if landing is open
    #     google_play_button = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID)
    #     google_play_button.click
    #
    #     # check if google play is open
    #     assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Image of app or game icon for Connect.Club"), "Google play is not open"
    #
    #     self.driver.install_app(path) #install app
    #     assert self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "usernameLabel"), "Wrong username or popup is closed"




    def teardown_method(self):
        self.driver.quit()
