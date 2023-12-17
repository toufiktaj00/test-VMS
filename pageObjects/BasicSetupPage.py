from selenium.webdriver.common.by import By

class BasicSetup:

    navigation= (By.XPATH,'//*[@id="t_Button_navControl"]')
    lnksetup_module = (By.ID,'t_TreeNav_2')
    lnkBasicSetup = (By.LINK_TEXT,'Basic Setup')
    btn_Add_id = (By.ID,"btn_add")
    text_Name_id = (By.ID,"P102_LOOKUPMST_NAME")
    text_Code_id = (By.ID,"P102_LOOKUPMST_CODE")
    text_Description_id = (By.ID,'P102_DESCRIPTION')
    btn_Active_id = (By.ID,'P102_ACTIVE_STATUS')
    btn_Save_id = (By.ID,'btn_save')
    btn_Reset_id = (By.ID,'btn_refresh')
    btn_Cancel_id = (By.ID,'btn_cancel')

    btn_edit_xpath=(By.XPATH,"(//img)[2]")
    btn_delete_id=(By.ID,"btn_delete")
    btn_update_id=(By.ID,"btn_update1")
    btn_e_cancel_id = (By.ID, "btn_cancel") #btn_cancel

    btn_add_child_xpath=(By.XPATH,"(//i[@aria-hidden='true'])[2]")
    #btn_ac_cancel_id=(By.ID,"btn_cancel1")
    btn_ac_reset_id = (By.ID, "btn_refresh1")
    btn_ac_save_id = (By.ID, "btn_save2")

#Details
    btn_details_xpath=(By.XPATH,"(//i[@class='fa fa-eye'])[1]")
    btn_details_edit_class=(By.XPATH,'//*[@id="staticHTMLTable"]/div/table/tbody[1]/tr/td[9]/a/span/span/img')
    btn_details_edit_update_id=(By.ID,'btn_update2')
    btn_details_edit_delete_id = (By.ID, 'btn_delete1')
    btn_details_edit_cancel_id=(By.ID,"btn_cancel1")

    alrt_btn_yes=(By.ID,'alertify-ok')
    alrt_btn_no = (By.ID, 'alertify-cancel')


    #add child

    txt_child_name_id=(By.ID,'P102_LOOKUPCHD_NAME')
    txt_child_code_id=(By.ID,'P102_LOOKUPCHD_CODE')
    txt_child_remarks_id = (By.ID, 'P102_REMARKS')
    btn_child_save_id = (By.ID, 'btn_save2')
    btn_child_reset_id = (By.ID, 'btn_refresh1')
    btn_child_cancel_id = (By.ID, 'btn_cancel1')


    # constructor
    def __init__(self, driver):
        self.driver = driver
    def clickonNavigation(self):
        self.driver.find_element(*self.navigation).click()

    def clickSetupMenu(self):

        self.driver.find_element(*self.lnksetup_module).click()

    def clickBasicSetup(self):
        self.driver.find_element(*self.lnkBasicSetup).click()

    def clickAdd(self):
        self.driver.find_element(*self.btn_Add_id).click()

    def setName(self,name):
        self.driver.find_element(*self.text_Name_id).send_keys(name)

    def setCode(self,code):
        self.driver.find_element(*self.text_Code_id).send_keys(code)

    def setDescription(self,description):
        self.driver.find_element(*self.text_Description_id).send_keys(description)

    def setAction(self):
        self.driver.find_element(*self.btn_Active_id).click()

    def clickSave(self):
        self.driver.find_element(*self.btn_Save_id).click()

    def clickReset(self):
        self.driver.find_element(*self.btn_Reset_id).click()

    def clickCancle(self):
        self.driver.find_element(*self.btn_Cancel_id).click()

    def clickAddChild(self):
        self.driver.find_element(*self.btn_add_child_xpath).click()

    #Edit
    def clickEdit(self):
        self.driver.find_element(*self.btn_edit_xpath).click()
    def click_Edit_Cancel(self):
        self.driver.find_element(*self.btn_e_cancel_id).click()
    def clickonDeletYes(self):
        self.driver.find_element(*self.alrt_btn_yes).click()
    def clickonDeletNo(self):
        self.driver.find_element(*self.alrt_btn_no).click()

    #Update
    def clickUpdate(self):
        self.driver.find_element(*self.btn_update_id).click()


    #Delete
    def clickDelete(self):
        self.driver.find_element(*self.btn_delete_id).click()
    # def clickUpdate(self):
    #     self.driver.find_element(*self.btn_update_id).click()

    #Details
    def clickDetails(self):
        self.driver.find_element(*self.btn_details_xpath).click()
    def clickDetailsEdit(self):
        self.driver.find_element(*self.btn_details_edit_class).click()

    def clickDetailsEditUpdate(self):
        self.driver.find_element(*self.btn_details_edit_update_id).click()

    def clickDetailsEditDelete(self):
        self.driver.find_element(*self.btn_details_edit_delete_id).click()

    def clickDetailsEditcancel(self):
        self.driver.find_element(*self.btn_details_edit_cancel_id).click()



        # Add Child

    def setchildName(self,childname):
        self.driver.find_element(*self.txt_child_name_id).send_keys(childname)

    def setchildCode(self,childcode):
        self.driver.find_element(*self.txt_child_code_id).send_keys(childcode)
    def setchildRemarks(self,remarks):
        self.driver.find_element(*self.txt_child_remarks_id).send_keys(remarks)
    def clickchildSave(self):
        self.driver.find_element(*self.btn_child_save_id).click()

    def clickchildReset(self):
        self.driver.find_element(*self.btn_child_reset_id).click()

    def clickchildCancel(self):
        self.driver.find_element(*self.btn_child_cancel_id).click()




