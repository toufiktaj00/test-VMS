from selenium import webdriver
from selenium.webdriver.common.by import By

class DB_HSCode:
    driver = None
    page_title = (By.XPATH, '//*[@id="theme1_heading"]')

    def __init__(self, driver):
        self.driver = driver

    # Verify page
    def verifyHSCodePage(self):
        if self.driver.find_element(*self.page_title) == None:
            raise Exception("This is not the HS Code Setup Page")
        else:
            print("You are on the HS Code Setup page")
