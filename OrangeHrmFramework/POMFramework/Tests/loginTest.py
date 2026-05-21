from unittest import TestCase

from selenium import webdriver
import time

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import HtmlTestRunner

class LoginPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Setting up the test environment")
        cls.correct_path="/Users/anusha/Downloads/chromedriver-mac-x64/chromedriver"
        cls.my_path=Service(executable_path=cls.correct_path)
        cls.driver=webdriver.Chrome(service=cls.my_path)
        cls.driver.implicitly_wait(10)


    def test_loginPage(self):
        print("Testing started")
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.find_element(By.NAME,"username").send_keys("Admin")
        self.driver.find_element(By.XPATH,"//input[@name='password']").send_keys("admin123")
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,"//button[@type='submit']"))).click()
        time.sleep(2)
        print(self.driver.title)
        self.driver.find_element(By.XPATH,"//img[@src='/web/index.php/pim/viewPhoto/empNumber/7']").click()
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.LINK_TEXT,"Logout"))).click()
        self.assertEqual("OrangeHRM", "OrangeHRM")
        time.sleep(2)
        print("Testing completed")

    @classmethod
    def tearDownClass(cls):
        print("Tearing down the test environment")
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/anusha/Documents/SeleniumPython2026/OrangeHrmFramework/HtmlReportsGenerated'))