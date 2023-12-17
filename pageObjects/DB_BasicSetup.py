from selenium import webdriver
from selenium.webdriver.common.by import By

class DB_BasicSetup:
    driver = None
    page_title = (By.XPATH, '//*[@id="lookuprt"]/div[1]/div[1]')

    def __init__(self, driver):
        self.driver = driver

    # Verify page
    def verifyBasicSetupPage(self):
        if self.driver.find_element(*self.page_title) == None:
            raise Exception("This is not the Basic Setup Page")
        else:
            print("You are on the Basic Setup page")
