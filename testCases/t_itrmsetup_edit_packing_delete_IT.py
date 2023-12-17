import random
import string
import time

import pytest
from selenium.webdriver.common.by import By
from pageObjects.Item_Setup_Page import ItemSetup
from pageObjects.DB_Item_Setup import DB_Item_Setup
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_ItemSetup:

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_login(self, setup):
        self.logger.info("*********** Test_001_Measure Unit ************")
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
        self.logger.info("** Login successful **")

        self.logger.info("*** Verifying Item Setup page ***")

        self.itemsetup = ItemSetup(self.driver)
        self.itemsetup.clickonNavigation()
        self.itemsetup.clickSetupMenu()
        self.itemsetup.clickItemSetup()

        # Verify Dashboard Page
        dashboardpage = DB_Item_Setup(self.driver)
        dashboardpage.verifyItemSetupPage()

        self.logger.info("****Select Item Type ****")
        self.itemsetup.clickItemTypeinfo()
        self.itemsetup.setItemTypeinfodrpSearchData('Packing Material')
        self.itemsetup.clickItemTypeinfoSearchData()
        time.sleep(2)



        self.logger.info("****Starting search ****")
        searchitem = ItemSetup(self.driver)
        searchitem.setSearchData("test")
        time.sleep(2)

        self.itemsetup.clickEdit()
        time.sleep(2)
        self.itemsetup.clickDelet()
        time.sleep(7)

        self.itemsetup.clickonDeletYes()
        time.sleep(.5)

        print("Ok")
        self.msg = self.driver.find_element(By.TAG_NAME, 'body').text

        if 'Successfully Deleted!' in self.msg:
            assert True == True
            print("Delete Button is Working")
            self.logger.info("** Successfully Update  **")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_error_item_setup.png")
            assert True == False
            print("Delete Button is not Working ")
            self.logger.error("******Delete is failed*****")

        self.driver.close()

