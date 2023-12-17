from selenium import webdriver
from selenium.webdriver.common.by import By

class Dashboard:
    driver = None
    branch = (By.ID, "P1_COMPANY_ID")
    date = (By.XPATH, '//*[@id="P1_TODATE"]')
    #tableDashboard = (By.CLASS_NAME, "card-header")

    def __init__(self, driver):
        self.driver = driver

    # Verify Landing page title
    def veifyDashboardPage(self):
        if self.driver.find_element(*self.date) == None:
            raise Exception("This is not Dashboard Page.")
        else:
            print("I am in Dashboard page")