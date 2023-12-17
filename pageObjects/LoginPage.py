from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pageObjects.Dashboard import Dashboard


#from Dashboard import Dashboard

class LoginPage:
    textbox_email = (By.ID,'P136_USERNAME')
    textbox_password = (By.ID,'P136_PASSWORD')
    drp_branch = (By.ID,'P136_BRANCH')
    button_login = (By.ID,'B134425066706563581')
    user = (By.CLASS_NAME,'t-Button t-Button--icon t-Button--header t-Button--navBar')
    button_logout = (By.ID,'btn_logout')



# constructor
    def __init__(self,driver):
        self.driver= driver

# Action methods
    def setUserName(self,username):
        self.driver.find_element(*self.textbox_email).clear()
        self.driver.find_element(*self.textbox_email).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(*self.textbox_password).clear()
        self.driver.find_element(*self.textbox_password).send_keys(password)

    def setBranch(self):
        # drp = Select(self.driver.find_element(*self.drp_branch))
        # drp.select_by_value(abc)
        self.driver.find_element(*self.drp_branch).click()

    def clickLogin(self):
        self.driver.find_element(*self.button_login).click()
        return Dashboard(self.driver)

    def clickUser(self):
        self.driver.find_element(*self.user).click()

    def clickLogout(self):
        self.driver.find_element(*self.button_logout).click()
