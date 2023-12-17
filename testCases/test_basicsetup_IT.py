import random
import string
import time

import pytest
from selenium.webdriver.common.by import By
from pageObjects.BasicSetupPage import BasicSetup
from pageObjects.DB_BasicSetup import DB_BasicSetup
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Basicsetup:

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    #@pytest.mark.sanity
    #@pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("***********Test_001_Basicsetup  ************")
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

        self.logger.info("*** Verifying Basic Setup page ***")

        self.basicsetup = BasicSetup(self.driver)
        self.basicsetup.clickonNavigation()
        self.basicsetup.clickSetupMenu()
        self.basicsetup.clickBasicSetup()

        # Verify Dashboard Page
        dashboardpage = DB_BasicSetup(self.driver)
        dashboardpage.verifyBasicSetupPage()

        # self.basicsetup.clickAdd()
        # self.logger.info("****Input data***")

        # random data generator
        # self.name = "Hasan"
        # self.basicsetup.setName(self.name)
        # self.code = 9985
        # self.basicsetup.setCode(self.code)
        # self.basicsetup.setDescription("This is basic setup page automation proto type")
        # time.sleep(3)
        # self.basicsetup.clickSave()
        # time.sleep(.5)

        self.basicsetup.clickAdd()
        self.logger.info("****Input random data***")
        #random data generator
        self.name=random_generator()+"Hasan"
        self.basicsetup.setName(self.name)
        self.code=random_generator()
        self.basicsetup.setCode(self.code)
        self.basicsetup.setDescription("This is basic setup page automation proto type")
        time.sleep(3)
        self.basicsetup.clickSave()
        time.sleep(.5)

        self.msg = self.driver.find_element(By.TAG_NAME,'body').text
       #print(self.msg)
        if 'Successfully completed!' in self.msg:
            assert True == True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_error_basic_setup.png")
            assert True == False
            self.logger.error("** Basic setup test is failed **")
            self.driver.close()

def random_generator(size=8, chars=string.ascii_lowercase+ string.digits):
    return''.join(random.choice(chars)for x in range(size))
