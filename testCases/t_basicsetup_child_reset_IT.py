import random
import string
import time
import pytest
from selenium.webdriver.common.by import By
from pageObjects.BasicSetupPage import BasicSetup
from pageObjects.Basic_Setup_Search_Page import BasicSetupSearch
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_008_Basicsetup:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression

    def test_login(self, setup):
        self.logger.info("** Login **")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        time.sleep(1)
        self.lp.setBranch()
        time.sleep(2)
        self.lp.clickLogin()
        time.sleep(3)
        self.logger.info("** Login successful **")

        self.logger.info("** Verifying Basic Setup page **")

        self.basicsetup = BasicSetup(self.driver)
        self.basicsetup.clickonNavigation()
        self.basicsetup.clickSetupMenu()
        self.basicsetup.clickBasicSetup()

        self.logger.info("** Starting search Customer By Name **")
        searchitem = BasicSetupSearch(self.driver)
        searchitem.setSearchData("Hasan")
        time.sleep(2)

        self.basicsetup.clickAddChild()
        time.sleep(2)

        self.logger.info("** Input random data **")
        #random data generator
        self.childname = random_generator()+" Yasin"
        self.basicsetup.setchildName(self.childname)
        self.childcode =random_generator()
        self.basicsetup.setchildCode(self.childcode)
        self.basicsetup.setchildRemarks("This is basic setup page automation proto type for Add Child")
        time.sleep(3)
        self.basicsetup.clickchildReset()
        time.sleep(.5)

        # Retrieve the entered name value
        child_name_box = self.driver.find_element(By.ID, "P102_LOOKUPCHD_NAME")
        child_name_value = child_name_box.get_attribute("value")
        print("Entered Name Value:", child_name_value)

        # Retrieve the entered code value
        child_code_box = self.driver.find_element(By.ID, "P102_LOOKUPCHD_CODE")
        child_code_value = child_code_box.get_attribute("value")
        print("Entered Code Value:", child_code_value)

        # Retrieve the entered description value
        child_remarks_box = self.driver.find_element(By.ID, "P102_REMARKS")
        child_remarks_value = child_remarks_box.get_attribute("value")
        print("Entered Description Value:", child_remarks_value)
        time.sleep(2)

        if child_name_value == "" and child_code_value == "" and child_remarks_value == "":
            print("Successfully Reset.")
            self.logger.info("** Successfully Reset  **")
        else:
            print("Reset Button is not working.")
            self.logger.error("** Failed to Reset  **")

        self.driver.close()

def random_generator(size=8, chars=string.ascii_lowercase+ string.digits):
    return''.join(random.choice(chars)for x in range(size))

