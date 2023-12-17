from selenium.webdriver.common.by import By

class DB_Item_Setup:
    driver = None
    page_title = (By.XPATH, '//*[@id="setup_hst_heading"]')

    def __init__(self, driver):
        self.driver = driver

    # Verify page
    def verifyItemSetupPage(self):
        if self.driver.find_element(*self.page_title) == None:
            raise Exception("This is not the Item Setup Page")
        else:
            print("You are on the Item Setup page")
