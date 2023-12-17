import time
import pytest
from selenium.webdriver.common.by import By
from pageObjects.BasicSetupPage import BasicSetup
from pageObjects.Basic_Setup_Search_Page import BasicSetupSearch
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_005_Basicsetup:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("** Test_003_Basicsetup **")
        self.logger.info("*** Logging ***")
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
        self.logger.info("*** Logging successful ***")

        self.logger.info("*** Verifying Basic Setup page ***")

        self.basicsetup = BasicSetup(self.driver)
        self.basicsetup.clickonNavigation()
        self.basicsetup.clickSetupMenu()
        self.basicsetup.clickBasicSetup()

        self.logger.info("*** Starting search ***")
        searchitem = BasicSetupSearch(self.driver)
        searchitem.setSearchData("Hasan")
        time.sleep(2)
        # status = searchitem.searchItembydata("9988")
        # assert status is True
        # self.logger.info("********Search finished************")
        # self.driver.close()


        self.basicsetup.clickEdit()
        time.sleep(2)
        self.basicsetup.clickDelete()
        time.sleep(2)


        self.basicsetup.clickonDeletYes()
       # self.basicsetup.clickonDeletNo()

        time.sleep(.5)

        self.msg = self.driver.find_element(By.TAG_NAME, 'body').text

        if 'Successfully Deleted..' in self.msg:
            assert True == True
            print("Delete & Yes Button is Working 😁")
            self.logger.info("** Successfully Delete  **")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_error_basic_setup.png")
            assert True == False
            self.logger.error("******Delete is failed*****")
            print("Delete & Yes Button is not Working ")
            self.logger.info("** Fail to Delete  **")

        self.driver.close()


