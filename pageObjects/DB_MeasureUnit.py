from selenium import webdriver
from selenium.webdriver.common.by import By

class DB_MeasureUnit:
    driver = None
    page_title = (By.XPATH, '//*[@id="uomrt_heading"]')

    def __init__(self, driver):
        self.driver = driver

    # Verify page
    def verifyMeasureUnitPage(self):
        if self.driver.find_element(*self.page_title) == None:
            raise Exception("This is not the Measure Unit Page")
        else:
            print("You are on the Measure Unit page")
