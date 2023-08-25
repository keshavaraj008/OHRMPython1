from selenium.webdriver.common.by import By

from Utils.keywordUtils import Utils


# Writing the test steps which will be performed in this page
class LoginPages(Utils):
    # Locators
    username = (By.NAME, 'username')
    password = (By.NAME, 'password')
    login_btn = (By.CSS_SELECTOR, "button[type='submit']")
    dashboard = (By.XPATH, "//h6[text()='Dashboard']")
    invalid = (By.XPATH, "//p[text()='Invalid credentials']")
    user_menu = (By.CSS_SELECTOR, ".oxd-userdropdown")
    logout_btn = (By.XPATH, "//a[text() = 'Logout']")

    # driver initialization for the page
    def __init__(self, driver):
        super(LoginPages, self).__init__(driver)

    # Login with the user
    def login(self, username, pwd):
        self.click_element(self.username)
        self.send_text(self.username, username)
        self.click_element(self.password)
        self.send_text(self.password, pwd)
        self.click_element(self.login_btn)
        try:
            if self.is_visible(self.dashboard):
                return True
        except Exception as e:
            print("Not a valid credential")
            self.take_screenshot()
            try:
                if self.is_visible(self.invalid):
                    return False
            except Exception as e:
                print("No element found")

                return False

    # Logout the user from the application
    def logout(self):
        try:
            self.click_element(self.user_menu)
            if self.is_visible(self.logout_btn):
                self.click_element(self.logout_btn)
                return True
        except Exception as e:
            print("Logout option not found")
            self.take_screenshot()
            try:
                if self.is_visible(self.username):
                    return False
            except Exception as e:
                print("Please check the locator for logout")

                return False