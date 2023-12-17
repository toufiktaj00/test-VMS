from selenium import webdriver
from selenium.webdriver.common.by import By

class DB_PackType:
    driver = None
    page_title = (By.XPATH, '//*[@id="packinfo_heading"]')

    def __init__(self, driver):
        self.driver = driver

    # Verify page
    def verifyPackTypePage(self):
        if self.driver.find_element(*self.page_title) == None:
            raise Exception("This is not the Pack Type Setup Page")
        else:
            print("You are on the Pack Type Setup page")
