from selenium.webdriver.common.by import By

class HSCode:

    navigation= (By.XPATH,'//*[@id="t_Button_navControl"]')
    lnkSetup_module = (By.ID,'t_TreeNav_2')
    lnk_HSCode = (By.LINK_TEXT,'HS Code')
    btn_clear_id = (By.ID, "btn_add")
    text_HS_Code_id = (By.ID, "P22_HS_CODE")
    text_Description_id = (By.ID, "P22_DESCRIPTION")
    text_VAT_id = (By.ID, 'P22_VAT_PCT')
    #btn_Active_id = (By.ID, 'P102_ACTIVE_STATUS')
    btn_Save_id = (By.ID, 'btn_save')


    btn_edit_xpath = (By.XPATH, '//*[@id="872725686882185804_orig"]/tbody/tr[2]/td[1]/a/span')
    btn_update_id = (By.ID, "btn_update")
    btn_delete_id = (By.XPATH, '//*[@id="872725686882185804_orig"]/tbody/tr[2]/td[11]/a')

    #btn_e_cancel_id = (By.ID, "btn_cancel")
    alrt_btn_yes = (By.ID, 'alertify-ok')
    alrt_btn_no = (By.ID, 'alertify-cancel')

# Search
    txt_search = (By.ID,'P22_SEARCH')
    table = (By.XPATH, "//div[@class='t-fht-wrapper']") #//div[@class='t-fht-tbody']
    tableRows = (By.XPATH, "//div[@class='t-fht-tbody']//tr")  # //div[@class='t-fht-tbody']//tr
    tableColumn = (By.XPATH, "//div[@class='t-fht-tbody']//tr//td")




    def __init__(self, driver):
        self.driver = driver

    def clickonNavigation(self):
        self.driver.find_element(*self.navigation).click()

    def clickSetupMenu(self):
        self.driver.find_element(*self.lnkSetup_module).click()

    def clickHSCode(self):
        self.driver.find_element(*self.lnk_HSCode).click()

    def clickClear(self):
        self.driver.find_element(*self.btn_clear_id).click()

    def setHSCode(self, code):
        self.driver.find_element(*self.text_HS_Code_id).send_keys(code)

    def setDescription(self, description):
        self.driver.find_element(*self.text_Description_id).send_keys(description)



    # def setRemarks(self, remarks):
    #     self.driver.find_element(*self.text_Remarks_id).send_keys(remarks)

    def clickSave(self):
        self.driver.find_element(*self.btn_Save_id).click()

    # def clickCancle(self):
    #     self.driver.find_element(*self.btn_Cancel_id).click()


    def clickEdit(self):
        self.driver.find_element(*self.btn_edit_xpath).click()

    def clickUpdate(self):
        self.driver.find_element(*self.btn_update_id).click()

    def clickDelet(self):
        self.driver.find_element(*self.btn_delete_id).click()


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
