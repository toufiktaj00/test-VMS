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

        self.logger.info("*** Verifying Measure Unit page ***")

        self.itemsetup = ItemSetup(self.driver)
        self.itemsetup.clickonNavigation()
        self.itemsetup.clickSetupMenu()
        self.itemsetup.clickItemSetup()

        # Verify Dashboard Page
        dashboardpage = DB_Item_Setup(self.driver)
        dashboardpage.verifyItemSetupPage()


        self.itemsetup.clickAdd()
        time.sleep(2)

 # Dropdown
    #Item
        self.itemsetup.clickdrpItemType()

        self.itemsetup.setItemTypedrpSearchData("Product")

        self.itemsetup.clickItemTypeSearchData()


    #Material

        self.itemsetup.clickdrpMaterialType()

        self.itemsetup.setMaterialTypeDrpSearchData("Test Product")

        self.itemsetup.clickMaterialTypeSearchData()
        time.sleep(2)

    # HS Code

        self.itemsetup.clickdrpHSCode()

        self.itemsetup.setHSCodeDrpSearchData("12121")

        self.itemsetup.clickHSCodeSearchData()
        time.sleep(2)



        self.name = "test " + random_generator()
        self.itemsetup.setItemName(self.name)  # Changed method name to setConvQty
        time.sleep(1)

        self.itemsetup.clickExempt()

        #self.itemsetup.setUnitPrice("99")
        self.price = random_generator()
        self.itemsetup.setUnitPrice(self.price)  # Changed method name to setConvQty
        time.sleep(1)


    #UoM
        self.itemsetup.clickUoM()

        self.itemsetup.setUoMDrpSearchData("kg")

        self.itemsetup.clickUoMSearchData()
        time.sleep(2)

        self.itemsetup.setConvQty(1000)
        time.sleep(1)

        #UoMLow

        self.itemsetup.clickUoMLow()

        self.itemsetup.setUoMLowDrpSearchData("mg")

        self.itemsetup.clickUoMLowSearchData()
        time.sleep(2)




  # End Dropdown




        self.itemsetup.clickSave()
        time.sleep(.5)


        self.msg = self.driver.find_element(By.TAG_NAME, 'body').text

        if 'Successfully saved!' in self.msg:
            assert True == True
            print("Child Successfully Added")
            self.logger.info("** Successfully Update  **")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_error_basic_setup.png")
            assert True == False
            print("Update Button is not Working ")
            self.logger.error("****** Update is failed *****")

        self.driver.close()

def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
