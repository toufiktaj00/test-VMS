import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
class MeasureUnit:

    navigation= (By.XPATH,'//*[@id="t_Button_navControl"]')
    lnksetup_module = (By.ID,'t_TreeNav_2')
    lnkMeasureUnit = (By.LINK_TEXT,'Measure Unit')
    btn_Add_id = (By.ID, "btn_add")
    text_Unit_Name_id = (By.ID, "P205_DESCRIPTION")
    text_Fr_Digit_id = (By.ID, "P205_FR_DIGIT")
    text_Remarks_id = (By.ID, 'P205_REMARKS')
    #btn_Active_id = (By.ID, 'P102_ACTIVE_STATUS')
    btn_Save_id = (By.ID, 'btn_create')
    #btn_Reset_id = (By.ID, 'btn_refresh')
    btn_Cancel_id = (By.ID, 'btn_cancel')

    btn_edit_xpath = (By.XPATH, '//*[@id="1182719120165680752_orig"]/tbody/tr[2]/td[8]/a/span/img')
    btn_update_id = (By.ID, "btn_update")
    btn_delete_id = (By.ID, "btn_delete")
    btn_e_cancel_id = (By.ID, "btn_cancel")
    alrt_btn_yes = (By.ID, 'alertify-ok')
    alrt_btn_no = (By.ID, 'alertify-cancel')


    btn_add_child_xpath = (By.XPATH, '//*[@id="1062213110421634007_orig"]/tbody/tr[2]/td[7]')

    txt_Conv_Qty_id=(By.ID,"P205_CONV_QTY")
    btn_create_id=(By.ID,"btn_create_chd")
#Dropdown
    dropdown=(By.XPATH,'//*[@id="P205_UNIT_TO_CONTAINER"]/div[2]/div/span/span[1]/span/span[2]')
    drp_search=(By.XPATH,'//*[@id="t_PageBody"]/span/span/span[1]/input')
    drp_search_value=(By.XPATH,'//*[@id="select2-P205_UNIT_TO-results"]')

#SEarch
    txt_search = (By.ID, 'P205_SEARCH')
    table = (By.XPATH, "//div[@class='t-fht-tbody']")
    tableRows = (By.XPATH, "//div[@class='t-fht-tbody']//tr")  # //div[@class='t-fht-tbody']//tr
    tableColumn = (By.XPATH, "//div[@class='t-fht-tbody']//tr//td")

#Child Edit

    btn_details=(By.XPATH,'//*[@id="1062213110421634007_orig"]/tbody/tr[2]/td[9]/a/span[1]/span/b/i')
    btn_child_edit=(By.XPATH,'//*[@id="staticHTMLTable"]/div/table/tbody[1]/tr/td[5]/a/span/span')
    btn_child_update=(By.ID,'btn_update1')
    btn_child_delete=(By.ID,'btn_delete1')


    def __init__(self, driver):
        self.driver = driver
    def clickonNavigation(self):
        self.driver.find_element(*self.navigation).click()

    def clickSetupMenu(self):

        self.driver.find_element(*self.lnksetup_module).click()

    def clickMeasureUnit(self):
        self.driver.find_element(*self.lnkMeasureUnit).click()

    def clickAdd(self):
        self.driver.find_element(*self.btn_Add_id).click()

    def setUnitName(self,name):
        self.driver.find_element(*self.text_Unit_Name_id).send_keys(name)

    def setFrDigit(self,digit):
        self.driver.find_element(*self.text_Fr_Digit_id).send_keys(digit)

    def setRemarks(self,remarks):
        self.driver.find_element(*self.text_Remarks_id).send_keys(remarks)

    def clickSave(self):
        self.driver.find_element(*self.btn_Save_id).click()

    def clickCancle(self):
        self.driver.find_element(*self.btn_Cancel_id).click()

    def clickAddchild(self):
        self.driver.find_element(*self.btn_add_child_xpath).click()

#Dropdown
    def clickUnitTo(self):
        self.driver.find_element(*self.dropdown).click()

    def setdrpSearchData(self, data):
        self.driver.find_element(*self.drp_search).clear()
        self.driver.find_element(*self.drp_search).send_keys(data)

    def clickSearchData(self):
        self.driver.find_element(*self.drp_search_value).click()




    def setConvQty(self,qty):
        self.driver.find_element(*self.txt_Conv_Qty_id).send_keys(qty)

    def clickCreate(self):
        self.driver.find_element(*self.btn_create_id).click()





    # def clickDropdown(self):
    #     self.driver.find_element(*self.dropdown).click()
    #Search

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
            inputname = table.find_element(By.XPATH, '//*[@id="1182719120165680752_orig"]/tbody/tr["+str(r)+"]//td[2]').text
            if inputname == sdata:
                flag = True
                break
        return flag





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

    def clickDetails(self):
        self.driver.find_element(*self.btn_details).click()

    def clickChildEdit(self):
        self.driver.find_element(*self.btn_child_edit).click()

    def clickChildUpdate(self):
        self.driver.find_element(*self.btn_child_update).click()

    def clickChildDelete(self):
        self.driver.find_element(*self.btn_child_delete).click()

