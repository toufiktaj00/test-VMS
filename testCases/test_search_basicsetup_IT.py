import time
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.BasicSetupPage import BasicSetup
from pageObjects.Basic_Setup_Search_Page import BasicSetupSearch
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_SearchItemByName_001:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchItemByName(self, setup):
        self.logger.info("***********Test_001_Login************")
        self.logger.info("********Verifying Login test************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.setBranch()
        time.sleep(2)
        self.lp.clickLogin()
        time.sleep(3)

        self.logger.info("********Logging successful************")

        self.logger.info("********Verifying Basic Setup page************")

        self.basicsetup = BasicSetup(self.driver)
        self.basicsetup.clickonNavigation()
        self.basicsetup.clickSetupMenu()
        self.basicsetup.clickBasicSetup()

        self.logger.info("********Starting search Customer By Name************")
        searchitem = BasicSetupSearch(self.driver)
        searchitem.setSearchData("PN")
        time.sleep(5)
        status = searchitem.searchItembydata("PN")
        assert status is True
        self.logger.info("********Search finished************")
        self.driver.close()
