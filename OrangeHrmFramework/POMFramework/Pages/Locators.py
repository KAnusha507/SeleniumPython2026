from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class locators:
    def __init__(self,driver):
        self.driver=driver
        self.driver=driver
        self.wait = WebDriverWait(self.driver, 10)
        self.username_field="username"
        self.password_field= "//input[@name='password']"
        self.login_btn_click="//button[@type='submit']"
        self.welcome_link=(By.XPATH, "//img[@src='/web/index.php/pim/viewPhoto/empNumber/7']")
        self.logout_link=(By.LINK_TEXT, "Logout")