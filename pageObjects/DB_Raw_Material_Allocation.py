from selenium import webdriver
from selenium.webdriver.common.by import By

class DB_Raw_Material_Allocation:
    driver = None
    page_title = (By.XPATH, '//*[@id="rmai_heading"]')

    def __init__(self, driver):
        self.driver = driver

    # Verify page
    def verifyRaw_Material_Allocation_Page(self):
        if self.driver.find_element(*self.page_title) == None:
            raise Exception("This is not the Raw Materials Allocation Page")
        else:
            print("You are on the Raw Materials Allocation page")
