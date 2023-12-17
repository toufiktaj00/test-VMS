import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import time

class Test_002_DDT_Login:

    baseURL = ReadConfig.getApplicationURL()
    path = ".\\TestData\\vms_testdata.xlsx"

    logger = LogGen.loggen()


    @pytest.mark.regression
    def test_login_ddt(self, setup):

        self.logger.info("***********Test_002_DDT_Login ************")
        self.logger.info("******** Verifying Login DDT test ************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.rows = XLUtils.getRowCount(self.path,'Sheet1')
        print("Number of Rows in Excel:",self.rows)

        lst_status = []   #empty list

        for r in range(2, self.rows+1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.setBranch()
            time.sleep(2)
            self.lp.clickLogin()
            time.sleep(3)
            act_title = self.driver.title
            exp_title = "VAT Management System"

            if act_title == exp_title:
                if self.exp == "pass":
                    self.logger.info("Passed")

                    self.lp.clickUser()
                    self.lp.clickLogout()
                    lst_status.append("Pass")

                elif self.exp == "Fail":
                    self.logger.error("****Failed****")
                    self.lp.clickUser()
                    self.lp.clickLogout()
                    lst_status.append("Fail")

            elif act_title != exp_title:
                if self.exp == 'Pass':
                    self.logger.error("**Fail**")
                    lst_status.append("Fail")
                elif self.exp == 'Fail':
                    self.logger.info("***passed***")
                    lst_status.append("Pass")
            # self.driver.save_screenshot(".//Screenshots//" + "test_login.png")


        if "Fail" not in lst_status:
            self.logger.info("***Loging DDT test passed***")
            self.driver.close()
            assert True

        else:
            self.logger.error("***DDT test failed***")
            self.driver.close()
            assert False
        self.logger.info("***End of Loging DDT Test***")
        self.logger.info("*****Completed TC_LogingDDT_002*****")










