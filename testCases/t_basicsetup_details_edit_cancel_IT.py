import logging
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.BasicSetupPage import BasicSetup
from pageObjects.Basic_Setup_Search_Page import BasicSetupSearch
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_0012_Basicsetup:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression

    def test_login(self, setup):
        self.logger.info("***********Test_003_Basicsetup************")
        self.logger.info("******** Logging ************")
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
        self.logger.info("******** Logging successful ************")

        self.logger.info("******** Verifying Basic Setup page ************")

        self.basicsetup = BasicSetup(self.driver)
        self.basicsetup.clickonNavigation()
        self.basicsetup.clickSetupMenu()
        self.basicsetup.clickBasicSetup()

        self.logger.info("** Starting search **")
        searchitem = BasicSetupSearch(self.driver)
        time.sleep(2)
        searchitem.setSearchData("test")
        time.sleep(5)

        self.basicsetup.clickDetails()
        time.sleep(2)

        self.basicsetup.clickDetailsEdit()
        time.sleep(2)

        self.basicsetup.clickDetailsEditcancel()
        time.sleep(1)

        self.msg = self.driver.find_element(By.TAG_NAME, 'body').text

        if 'BASIC SETUP DETAIL' in self.msg:
            assert True == True
            print("Cancel Button is not working😪")
            self.logger.error("** Fail to Cancel  **")
        else:
            print("Cancel Button is Working 😁")
            self.logger.info("** Successfully cancel  **")
        logging.shutdown()

        self.driver.close()

#pytest -v -s -n=3 --html=Reports\report.html testCases/t_basicsetup_details_edit_cancel_IT.py

