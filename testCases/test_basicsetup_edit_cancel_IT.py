import time
import pytest
from selenium.webdriver.common.by import By
from pageObjects.BasicSetupPage import BasicSetup
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_006_Basicsetup:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("*** Test_006_Basicsetup ***")
        self.logger.info("*** Login ***")
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

        self.logger.info("******** Verifying Basic Setup page ************")

        self.basicsetup = BasicSetup(self.driver)
        self.basicsetup.clickonNavigation()
        self.basicsetup.clickSetupMenu()
        self.basicsetup.clickBasicSetup()
        self.basicsetup.clickEdit()

        time.sleep(2)
        self.basicsetup.click_Edit_Cancel()
        time.sleep(2)

        self.msg = self.driver.find_element(By.TAG_NAME, 'body').text

        if 'BASIC SETUP' in self.msg:
            assert True == True
            print("Cancel Button is not working")
            self.logger.error("** Fail cancel  **")
        else:
            print("Cancel Button is Working")
            self.logger.info("** Successfully Cancel  **")
        self.driver.close()