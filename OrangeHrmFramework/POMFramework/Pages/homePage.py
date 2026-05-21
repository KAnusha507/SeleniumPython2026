from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class HomePage:
    def __init__(self,driver):
        self.driver=driver
        self.welcome_link=(By.XPATH, "//img[@src='/web/index.php/pim/viewPhoto/empNumber/7']")
        self.logout_link=(By.LINK_TEXT, "Logout")

    def click_welcome(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.welcome_link)).click()

    def click_logout(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.logout_link)).click()