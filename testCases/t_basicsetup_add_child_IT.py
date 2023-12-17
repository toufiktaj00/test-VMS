import random
import string
import time
import pytest
from selenium.webdriver.common.by import By
from pageObjects.BasicSetupPage import BasicSetup
from pageObjects.Basic_Setup_Search_Page import BasicSetupSearch
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_007_Basicsetup:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        # self.logger.info("***********Test_007_Basicsetup************")
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
        self.logger.info("** Logging successful **")

        self.logger.info("** Verifying Basic Setup page **")

        self.basicsetup = BasicSetup(self.driver)
        self.basicsetup.clickonNavigation()
        self.basicsetup.clickSetupMenu()
        self.basicsetup.clickBasicSetup()

        self.logger.info("** Starting search Customer By Name **")
        searchitem = BasicSetupSearch(self.driver)
        searchitem.setSearchData("Hasan")
        time.sleep(2)

        self.logger.info("** Add Child **")
        self.basicsetup.clickAddChild()
        time.sleep(2)

        self.logger.info("** Input random data **")
        #random data generator
        self.childname = random_generator()+" Yasin"
        self.basicsetup.setchildName(self.childname)

        self.childcode =random_generator()
        self.basicsetup.setchildCode(self.childcode)
        self.basicsetup.setchildRemarks("This is basic setup page automation proto type for Add Child")
        time.sleep(3)
        self.basicsetup.clickchildSave()
        time.sleep(.5)

        self.msg = self.driver.find_element(By.TAG_NAME,'body').text
       #print(self.msg)
        if 'Successfully completed!' in self.msg:
            assert True == True
            self.logger.info("** Child Added Successfully **")
            print("Child successfully Added")

           # time.sleep(2)
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_error_basic_setup.png")
            assert True == False
            self.logger.error("******Basic setup test is failed*****")
            self.driver.close()
            self.logger.error("** Failed to Add Child **")
def random_generator(size=8, chars=string.ascii_lowercase+ string.digits):
    return''.join(random.choice(chars)for x in range(size))
