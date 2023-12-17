import time
import pytest
from pageObjects.Dashboard import Dashboard
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()



    # @pytest.mark.regression
    def test_LoginPageTitle(self,setup):

        self.logger.info("**********Test_001_Login**********")
        self.logger.info("*********Verifying Login page title******")
        self.driver=setup
        self.driver.get(self.baseURL)

        act_title=self.driver.title
        if act_title=="Login Page":
            assert True
            self.driver.close()
            self.logger.info("**********Login Page Title test is passed**********")
        else:
            self.driver.save_screenshot(".//Screenshots//"+"test_login_pageTitle.png")
            self.driver.close()
            self.logger.error("******Login Page Title test is failed*****")
            assert False

    # @pytest.mark.sanity
    # @pytest.mark.regression
    def test_login(self,setup):

        self.logger.info("***********Test_001_Login ************")
        self.logger.info("******** Verifying Login test ************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)

        self.lp.setBranch()
        time.sleep(2)

        self.lp.clickLogin()
        time.sleep(3)

       #Verify Dashboard Page
        dashboardpage = Dashboard(self.driver)
        dashboardpage.veifyDashboardPage()

        act_title = self.driver.title
        if act_title == "VAT Management System":
            assert True
            self.logger.info("*********** Login test Passed ************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".//Screenshots//"+"test_login.png")
            self.driver.close()
            self.logger.error("** Login test Failed  **")
            assert False
