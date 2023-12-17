import random
import string
import time

import pytest
from selenium.webdriver.common.by import By
from pageObjects.Raw_Material_Allocation_Page import Raw_Material_Allocation
from pageObjects.DB_Raw_Material_Allocation import DB_Raw_Material_Allocation
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Raw_Material_Allocation:

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

        self.logger.info("*** Verifying Measure Unit page ***")

        self.rawmaterialallocation = Raw_Material_Allocation(self.driver)
        self.rawmaterialallocation.clickonNavigation()
        self.rawmaterialallocation.clickSetupMenu()
        self.rawmaterialallocation.clicklnk_RawMaterialAllocation()

        # Verify Dashboard Page
        dashboardpage = DB_Raw_Material_Allocation(self.driver)
        dashboardpage.verifyRaw_Material_Allocation_Page()


        self.rawmaterialallocation.clickAdd()
        time.sleep(2)

 # Dropdown
    #Item
        self.rawmaterialallocation.clickdrpProductType()

        self.rawmaterialallocation.setProductTypedrpSearchData("Product")

        self.rawmaterialallocation.clickProductTypeSearchData()

        self.rawmaterialallocation.product_name('test 94td3848 (Test Product Type)')


        self.rawmaterialallocation.