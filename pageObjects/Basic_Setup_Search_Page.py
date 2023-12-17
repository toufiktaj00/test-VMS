
from selenium.webdriver.common.by import By

class BasicSetupSearch:

    txt_search=(By.ID,'P102_SEARCH')
    #tblSearchResults=(By.CLASS_NAME,'t-fht-tbody')
    table=(By.XPATH,"//div[@class='t-fht-tbody']")
    tableRows=(By.XPATH,"//div[@class='t-fht-tbody']//tr") #//div[@class='t-fht-tbody']//tr
    tableColumn=(By.XPATH,"//div[@class='t-fht-tbody']//tr//td")

    def __init__(self,driver):
        self.driver= driver

    def setSearchData(self, data):
        self.driver.find_element(*self.txt_search).clear()
        self.driver.find_element(*self.txt_search).send_keys(data)

    def getNoOfRows(self):
        return len(self.driver.find_elements(*self.tableRows))

    def getNoOfColumns(self):
        return len(self.driver.find_elements(*self.tableColumn))

    def searchItembydata(self,sdata):
        flag = False
        for r in range(1,self.getNoOfRows()+1):
            table=self.driver.find_element(*self.table)
            inputname = table.find_element(By.XPATH,'//div[@class="t-fht-tbody"]//tr["+str(r)+"]//td[2]').text
            if inputname == sdata:
                flag = True
                break
        return flag