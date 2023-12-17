import random
import string
import time

import pytest
from selenium.webdriver.common.by import By
from pageObjects.Pack_Type_Page import PackType
from pageObjects.DB_Pack_Type import DB_PackType
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_PackType:

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    #@pytest.mark.sanity
    #@pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("***********Test_001_Measure Unit  ************")
        self.logger.info("******** Loging ************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        time.sleep(1)
        self.lp.setBranch()
        time.sleep(2)
        self.lp.clickLogin()
        time.sleep(3)
        self.logger.info("** Login successful **")

        self.logger.info("*** Verifying Measure Unit page ***")

        self.packtype = PackType(self.driver)
        self.packtype.clickonNavigation()
        self.packtype.clickSetupMenu()
        self.packtype.clickPackType()

        # Verify Dashboard Page
        dashboardpage = DB_PackType(self.driver)
        dashboardpage.verifyPackTypePage()


        self.logger.info("****Starting search ****")
        searchitem = PackType(self.driver)
        searchitem.setSearchData("test")
        time.sleep(2)

        self.packtype.clickEdit()
        time.sleep(2)
        self.packtype.clickUpdate()
        time.sleep(.5)


        self.msg = self.driver.find_element(By.TAG_NAME, 'body').text

        if 'Successfully completed!' in self.msg:
            assert True == True
            print("Update Button is Working")
            self.logger.info("** Successfully Update  **")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_error_basic_setup.png")
            assert True == False
            print("Update Button is not Working ")
            self.logger.error("******Update is failed*****")

        self.driver.close()


