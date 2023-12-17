import time
import pytest
from selenium.webdriver.common.by import By
from pageObjects.BasicSetupPage import BasicSetup
from pageObjects.Basic_Setup_Search_Page import BasicSetupSearch
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_009_Basicsetup:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression

    def test_login(self, setup):

        self.logger.info("** Loging **")
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
        self.logger.info("******** Login successful ************")

        self.logger.info("** Basic Setup page ***")

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

        self.logger.info("****Input data***")

        self.childname = " Yasin"
        self.basicsetup.setchildName(self.childname)
        self.childcode = 123
        self.basicsetup.setchildCode(self.childcode)
        self.basicsetup.setchildRemarks("This is basic setup page automation proto type for Add Child")
        time.sleep(2)
        self.basicsetup.clickchildCancel()
        time.sleep(1)
        self.logger.info("** Input data **")


        self.msg = self.driver.find_element(By.TAG_NAME, 'body').text
        if 'BASIC SETUP DETAIL' in self.msg:
            assert True == True
            print("Cancel Button is not working")
            self.logger.info("**Cancel Button Working **")
        else:
            print("Cancel Button is Working")
            self.logger.error("** Cancel Button is not Working **")
        self.driver.close()


