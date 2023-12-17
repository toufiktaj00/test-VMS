from selenium.webdriver.common.by import By

class PackType:

    navigation= (By.XPATH,'//*[@id="t_Button_navControl"]')
    lnkSetup_module = (By.ID,'t_TreeNav_2')
    lnkPackType = (By.LINK_TEXT,'Pack Type Setup')
    btn_Add_id = (By.ID, "btn_add")
    text_Description_id = (By.ID, "P207_DESCRIPTION")
    text_Type_id = (By.ID, "P207_TYPE")
    text_Remarks_id = (By.ID, 'P207_REMARKS')
    #btn_Active_id = (By.ID, 'P102_ACTIVE_STATUS')
    btn_Save_id = (By.ID, 'btn_save')
    #btn_Reset_id = (By.ID, 'btn_refresh')
    btn_Cancel_id = (By.ID, 'btn_cancel')
    btn_edit_xpath = (By.XPATH, '//*[@id="1061207970263399882_orig"]/tbody/tr[2]/td[7]/a/span/img')
    btn_update_id = (By.ID, "btn_update")
    btn_delete_id = (By.ID, "btn_delete")
    btn_e_cancel_id = (By.ID, "btn_cancel")
    alrt_btn_yes = (By.ID, 'alertify-ok')
    alrt_btn_no = (By.ID, 'alertify-cancel')

# Search
    txt_search = (By.ID,'P207_SEARCH')
    table = (By.XPATH, "//div[@class='t-fht-tbody']") #//div[@class='t-fht-tbody']
    tableRows = (By.XPATH, "//div[@class='t-fht-tbody']//tr")  # //div[@class='t-fht-tbody']//tr
    tableColumn = (By.XPATH, "//div[@class='t-fht-tbody']//tr//td")





    def __init__(self, driver):
        self.driver = driver

    def clickonNavigation(self):
        self.driver.find_element(*self.navigation).click()

    def clickSetupMenu(self):
        self.driver.find_element(*self.lnkSetup_module).click()

    def clickPackType(self):
        self.driver.find_element(*self.lnkPackType).click()

    def clickAdd(self):
        self.driver.find_element(*self.btn_Add_id).click()

    def setDescription(self, description):
        self.driver.find_element(*self.text_Description_id).send_keys(description)

    def setType(self, type):
        self.driver.find_element(*self.text_Type_id).send_keys(type)

    def setRemarks(self, remarks):
        self.driver.find_element(*self.text_Remarks_id).send_keys(remarks)

    def clickSave(self):
        self.driver.find_element(*self.btn_Save_id).click()

    def clickCancle(self):
        self.driver.find_element(*self.btn_Cancel_id).click()


    def clickEdit(self):
        self.driver.find_element(*self.btn_edit_xpath).click()

    def clickUpdate(self):
        self.driver.find_element(*self.btn_update_id).click()

    def clickDelet(self):
        self.driver.find_element(*self.btn_delete_id).click()

    def clickCancel(self):
        self.driver.find_element(*self.btn_e_cancel_id).click()

    def clickonDeletYes(self):
        self.driver.find_element(*self.alrt_btn_yes).click()

    def clickonDeletNo(self):
        self.driver.find_element(*self.alrt_btn_no).click()

# Search

    def setSearchData(self, data):
        self.driver.find_element(*self.txt_search).clear()
        self.driver.find_element(*self.txt_search).send_keys(data)

    def getNoOfRows(self):
        return len(self.driver.find_elements(*self.tableRows))

    def getNoOfColumns(self):
        return len(self.driver.find_elements(*self.tableColumn))

    def searchItembydata(self, sdata):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element(*self.table)
            inputname = table.find_element(By.XPATH,'//*[@id="1061207970263399882_orig"]/tbody/tr[2]/td[2]').text
            if inputname == sdata:
                flag = True
                break
        return flag
