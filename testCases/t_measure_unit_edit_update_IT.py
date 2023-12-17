import time

import pytest
from selenium.webdriver.common.by import By
from pageObjects.Measure_Unit_Page import MeasureUnit
from pageObjects.DB_MeasureUnit import DB_MeasureUnit
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

        self.measureunit = MeasureUnit(self.driver)
        self.measureunit.clickonNavigation()
        self.measureunit.clickSetupMenu()
        self.measureunit.clickMeasureUnit()

        # Verify Dashboard Page
        dashboardpage = DB_MeasureUnit(self.driver)
        dashboardpage.verifyMeasureUnitPage()

        self.logger.info("****Starting search ****")
        searchitem = MeasureUnit(self.driver)
        searchitem.setSearchData("test")
        time.sleep(2)
        # status = searchitem.searchItembydata("9988")
        # assert status is True
        # self.logger.info("********Search finished************")
        # self.driver.close()


        self.measureunit.clickEdit()
        time.sleep(2)
        self.measureunit.clickUpdate()
        time.sleep(2)


        self.measureunit.clickonDeletYes()
       # self.basicsetup.clickonDeletNo()

        time.sleep(.5)

        self.msg = self.driver.find_element(By.TAG_NAME, 'body').text

        if 'Successfully completed!' in self.msg:
            assert True == True
            print("Update & Yes Button is Working")
            self.logger.info("** Successfully Update  **")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_error_basic_setup.png")
            assert True == False
            print("Update Button is not Working ")
            self.logger.error("******Update is failed*****")


        self.driver.close()


