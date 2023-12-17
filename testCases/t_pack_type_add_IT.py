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

        self.packtype .clickAdd()
        self.logger.info("****Input random data***")
        time.sleep(2)
        # random data generator
        self.description = random_generator() #+ "Hasan"
        self.packtype .setDescription(self.description)
        time.sleep(1)
        self.type = random_generator()
        self.packtype .setType(self.type)
        time.sleep(1)
        self.packtype .setRemarks("This is Pack Type setup page automation proto type")
        time.sleep(3)
        self.packtype .clickSave()
        time.sleep(.5)

        self.msg = self.driver.find_element(By.TAG_NAME, 'body').text
        # print(self.msg)
        if 'Successfully completed!' in self.msg:
            assert True == True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_error_Measure_unit.png")
            assert True == False
            self.logger.error("** Measure Unit setup test is failed **")
            self.driver.close()

def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
