import time
import pytest
from selenium.webdriver.common.by import By
from pageObjects.BasicSetupPage import BasicSetup
from pageObjects.DB_BasicSetup import DB_BasicSetup
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_002_Basicsetup:

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("***********Test_003_Basicsetup************")
        self.logger.info("******** Login ************")
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
        self.logger.info("******** Login successful ************")

        self.logger.info("******** Verifying Basic Setup page ************")

        self.basicsetup = BasicSetup(self.driver)
        self.basicsetup.clickonNavigation()
        self.basicsetup.clickSetupMenu()
        self.basicsetup.clickBasicSetup()


        # Verify Dashboard Page
        dashboardpage = DB_BasicSetup(self.driver)
        dashboardpage.verifyBasicSetupPage()


        self.basicsetup.clickAdd()
        self.logger.info("****Input data***")
        self.name = "Hasan"
        self.basicsetup.setName(self.name)
        self.code = 9986
        self.basicsetup.setCode(self.code)
        self.basicsetup.setDescription("This is basic setup page automation prototype")
        time.sleep(3)
        self.basicsetup.clickReset()
        time.sleep(2)

        # Retrieve the entered name value
        name_box = self.driver.find_element(By.ID, "P102_LOOKUPMST_NAME")
        name_value = name_box.get_attribute("value")
        print("Entered Name Value:", name_value)

        # Retrieve the entered code value
        code_box = self.driver.find_element(By.ID, "P102_LOOKUPMST_CODE")
        code_value = code_box.get_attribute("value")
        print("Entered Code Value:", code_value)

        # Retrieve the entered description value
        description_box = self.driver.find_element(By.ID, "P102_DESCRIPTION")
        description_value = description_box.get_attribute("value")
        print("Entered Description Value:", description_value)
        time.sleep(2)
        self.driver.close()

        if name_value == "" and code_value == "" and description_value == "":
            print("Successfully Reset.")
            self.logger.info("** Successfully Reset  **")
        else:
            print("Reset Button is not working.")
            self.logger.error("** Fail ro reset  **")
