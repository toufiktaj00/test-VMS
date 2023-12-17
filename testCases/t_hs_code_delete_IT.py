import random
import string
import time

import pytest
from selenium.webdriver.common.by import By
from pageObjects.HS_Code_Page import HSCode
from pageObjects.DB_HS_Code import DB_HSCode
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_MeasureUnit:

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

        self.hscode = HSCode(self.driver)
        self.hscode.clickonNavigation()
        self.hscode.clickSetupMenu()
        self.hscode.clickHSCode()

        # Verify Dashboard Page
        dashboardpage = DB_HSCode(self.driver)
        dashboardpage.verifyHSCodePage()

        self.logger.info("****Starting search ****")
        searchitem = HSCode(self.driver)
        searchitem.setSearchData("test")
        time.sleep(3)

        self.hscode.clickDelet()
        time.sleep(1)

        self.hscode.clickonDeletYes()
        time.sleep(.5)

        self.msg = self.driver.find_element(By.TAG_NAME, 'body').text
        # print(self.msg)
        if 'Successfully completed!' in self.msg:
            assert True == True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_error_Measure_unit.png")
            assert True == False
            self.logger.error("** HS Code setup test is failed **")
            self.driver.close()

def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
