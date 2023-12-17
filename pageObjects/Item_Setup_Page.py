import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class ItemSetup:

    navigation= (By.XPATH,'//*[@id="t_Button_navControl"]')
    lnkSetup_module = (By.ID,'t_TreeNav_2')
    lnk_ItemSetup = (By.LINK_TEXT,'Item Setup')
    btn_Add_id = (By.ID, "btn_add")
#Dropdown
    drp_Item_Type_xpath=(By.XPATH,'//*[@id="select2-P30_ITEM_TYPE-container"]')
    drp_Item_Type_search_field = (By.XPATH, '//*[@id="t_PageBody"]/span/span/span[1]/input')
    drp_Item_Type_search_value = (By.XPATH, '//*[@id="select2-P30_ITEM_TYPE-results"]')


    drp_Material_Type_xpath=(By.XPATH,'//*[@id="select2-P30_PROD_TYPE_NO-container"]')
    drp_Raw_Material_Type_xpath=(By.XPATH,'// *[ @ id = "select2-P30_RM_TYPE-container"] / span')
    drp_Packing_Material_Type_xpath = (By.XPATH, '//*[@id="select2-P30_PACK_MAT_TYPE-container"]')

    drp_Material_Type_search_field = (By.XPATH, '//*[@id="t_PageBody"]/span/span/span[1]/input')

    drp_Material_Type_search_value_product = (By.XPATH, '//*[@id="select2-P30_PROD_TYPE_NO-results"]')
    drp_Material_Type_search_value_raw_material = (By.XPATH, '// *[ @ id = "select2-P30_RM_TYPE-results"]')
    drp_Material_Type_search_value_packing_material = (By.XPATH, '//*[@id="select2-P30_PACK_MAT_TYPE-results"]')

    drp_HS_Code_xpath=(By.XPATH,'//*[@id="select2-P30_HS_CODE-container"]')
    drp_HS_Code_search_field = (By.XPATH, '//*[@id="t_PageBody"]/span/span/span[1]/input')
    drp_HS_Code_search_value = (By.XPATH, '//*[@id="select2-P30_HS_CODE-results"]')



    drp_UoM_xpath=(By.XPATH,'//*[@id="select2-P30_MU-container"]')
    drp_UoM_search_field = (By.XPATH, '//*[@id="t_PageBody"]/span/span/span[1]/input')
    drp_UoM_search_value = (By.XPATH, '//*[@id="select2-P30_MU-results"]')


    drp_UoMLow_xpath = (By.XPATH, '//*[@id="select2-P30_LOW_UNIT_NO-container"]')
    drp_UoMLow_search_field = (By.XPATH, '//*[@id="t_PageBody"]/span/span/span[1]/input')
    drp_UoMLow_search_value = (By.XPATH, '//*[@id="select2-P30_LOW_UNIT_NO-results"]')

#information page

    drp_information_xpath = (By.XPATH, '//*[@id="select2-P30_ITEM_TYPE_DUPLICATE-container"]')
    drp_information_search_field = (By.XPATH, '//*[@id="t_PageBody"]/span/span/span[1]/input')
    drp_information_search_value = (By.XPATH, '//*[@id="select2-P30_ITEM_TYPE_DUPLICATE-results"]')

# End Dropdown
    text_ItemName_id = (By.ID, "P30_ITEM_NAME")
#Flag
    tbtn_VATFlag_xpath=(By.XPATH,'//*[@id="P30_VAT_FLAG_CONTAINER"]/div[2]/div/span/span')
    tbtn_RebatableFlag_xpath = (By.XPATH, '//*[@id="P30_REBATABLE_CONTAINER"]/div[2]/div/span/span')
    tbtn_SDFlag_xpath = (By.XPATH, '//*[@id="P30_TAX_FLAG_CONTAINER"]/div[2]/div/span/span')
    tbtn_ExemptFlag_xpath = (By.XPATH, '//*[@id="P30_EXEMPT_FLG_CONTAINER"]/div[2]/div/span/span')

    text_SalesVat_id=(By.ID,'P30_SALES_VAT_AMT')
    text_SalExpVat_id=(By.ID,'P30_SAL_EXPVAT_AMT')
    text_Purchvat_id=(By.ID,'P30_PURCH_VAT_AMT')
    text_Purch_Impvat_id=(By.ID,'P30_PURCH_IMPVAT_AMT')
    text_SD_id=(By.ID,'P30_SD_AMT')
    text_conv_qty_id=(By.ID,'P30_CONV_QTY')
    text_UnitPrice_id = (By.ID, "P30_UNIT_PRICE")


    btn_Save_id = (By.ID, 'btn_create')

# Search
#     text_search_Item=(By.XPATH,'//*[@id="t_PageBody"]/span/span/span[1]/input')
#     ItemType_data=(By.XPATH,'//*[@id="select2-P30_ITEM_TYPE-results"]')

    txt_search = (By.ID, 'P30_SEARCH')
    table = (By.XPATH, "//div[@class='t-fht-wrapper']")  # //div[@class='t-fht-tbody']
    tableRows = (By.XPATH, "//div[@class='t-fht-tbody']//tr")  # //div[@class='t-fht-tbody']//tr
    tableColumn = (By.XPATH, "//div[@class='t-fht-tbody']//tr//td")

#edit
    btn_edit_xpath = (By.XPATH, '//*[@id="1118508623707976751_orig"]/tbody/tr[2]/td[4]/a/span')
    btn_update_id = (By.ID, "btn_save")
    btn_delete_id = (By.ID, 'btn_delete')

    #btn_e_cancel_id = (By.ID, "btn_cancel")
    alrt_btn_yes = (By.ID, 'alertify-ok')
    alrt_btn_no = (By.ID, 'alertify-cancel')




    def __init__(self, driver):
        self.driver = driver

    def clickonNavigation(self):
        self.driver.find_element(*self.navigation).click()

    def clickSetupMenu(self):
        self.driver.find_element(*self.lnkSetup_module).click()

    def clickItemSetup(self):
        self.driver.find_element(*self.lnk_ItemSetup).click()

    def clickAdd(self):
        self.driver.find_element(*self.btn_Add_id).click()



#Dropdown
    #ItemType

    def clickdrpItemType(self):
        self.driver.find_element(*self.drp_Item_Type_xpath).click()

    def setItemTypedrpSearchData(self, item):
        self.driver.find_element(*self.drp_Item_Type_search_field).clear()
        self.driver.find_element(*self.drp_Item_Type_search_field).send_keys(item)

    def clickItemTypeSearchData(self):
        self.driver.find_element(*self.drp_Item_Type_search_value).click()



#Material Type
    def clickdrpMaterialType(self):
        self.driver.find_element(*self.drp_Material_Type_xpath).click()

    def clickdrpRawMaterialType(self):
        self.driver.find_element(*self.drp_Raw_Material_Type_xpath).click()

    def clickdrpPackMaterialType(self):
        self.driver.find_element(*self.drp_Packing_Material_Type_xpath).click()


    def setMaterialTypeDrpSearchData(self, data):
        self.driver.find_element(*self.drp_Material_Type_search_field).clear()
        self.driver.find_element(*self.drp_Material_Type_search_field).send_keys(data)


    def clickMaterialTypeSearchData(self):
        self.driver.find_element(*self.drp_Material_Type_search_value_product).click()

    def clickRawMaterialTypeSearchData(self):
        self.driver.find_element(*self.drp_Material_Type_search_value_raw_material).click()

    def clickPackingMaterialTypeSearchData(self):
        self.driver.find_element(*self.drp_Material_Type_search_value_packing_material).click()

        # self.drp_Item_Type_search_value
        # test = self.driver.find_element(*self.drp_Material_Type_search_value)  # .click()
        # test.select_by_visible_text(value)



# HS Code
    def clickdrpHSCode(self):
        self.driver.find_element(*self.drp_HS_Code_xpath).click()

    def setHSCodeDrpSearchData(self, code):
        self.driver.find_element(*self.drp_HS_Code_search_field).clear()
        self.driver.find_element(*self.drp_HS_Code_search_field).send_keys(code)

    def clickHSCodeSearchData(self):
        self.driver.find_element(*self.drp_HS_Code_search_value).click()


# UoM
    def clickUoM(self):
        self.driver.find_element(*self.drp_UoM_xpath).click()

    def setUoMDrpSearchData(self, code):
        self.driver.find_element(*self.drp_UoM_search_field).clear()
        self.driver.find_element(*self.drp_UoM_search_field).send_keys(code)

    def clickUoMSearchData(self):
        self.driver.find_element(*self.drp_UoM_search_value).click()


# UoMLow
    def clickUoMLow(self):
        self.driver.find_element(*self.drp_UoMLow_xpath).click()

    def setUoMLowDrpSearchData(self, code):
        self.driver.find_element(*self.drp_UoMLow_search_field).clear()
        self.driver.find_element(*self.drp_UoMLow_search_field).send_keys(code)

    def clickUoMLowSearchData(self):
        self.driver.find_element(*self.drp_UoMLow_search_value).click()


#information page

    def clickItemTypeinfo(self):
        self.driver.find_element(*self.drp_information_xpath).click()

    def setItemTypeinfodrpSearchData(self, code):
        self.driver.find_element(*self.drp_information_search_field).clear()
        self.driver.find_element(*self.drp_information_search_field).send_keys(code)

    def clickItemTypeinfoSearchData(self):
        self.driver.find_element(*self.drp_information_search_value).click()




# End of Dropdown

    def clickVatFlag(self):
        self.driver.find_element(*self.tbtn_VATFlag_xpath).click()

    def clickRebatable(self):
        self.driver.find_element(*self.tbtn_RebatableFlag_xpath).click()

    def clickSD(self):
        self.driver.find_element(*self.tbtn_SDFlag_xpath).click()

    def clickExempt(self):
        self.driver.find_element(*self.tbtn_ExemptFlag_xpath).click()





    def setItemName(self, name):
        self.driver.find_element(*self.text_ItemName_id).send_keys(name)

    def setSalesVat(self, salesvat):
        self.driver.find_element(*self.text_SalesVat_id).send_keys(salesvat)
    def setSalesExpVat(self, salesexpvat):
        self.driver.find_element(*self.text_SalExpVat_id).send_keys(salesexpvat)

    def setPurchVat(self,purchvat):
        self.driver.find_element(*self.text_Purchvat_id).send_keys(purchvat)

    def setPurchImpVat(self, purchimpvat):
        self.driver.find_element(*self.text_Purch_Impvat_id).send_keys(purchimpvat)

    def setSD(self, sd):
        self.driver.find_element(*self.text_SD_id).send_keys(sd)

    def setConvQty(self,convqty):
        self.driver.find_element(*self.text_conv_qty_id).send_keys(convqty)

    def setUnitPrice(self,price):
        self.driver.find_element(*self.text_UnitPrice_id).send_keys(price)

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
    def setSearchtemType(self, data):
        self.driver.find_element(*self.txt_search).clear()
        self.driver.find_element(*self.txt_search).send_keys(data)

    def searchItembyType(self, sdata):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element(*self.table)
            inputname = table.find_element(By.XPATH, "//span[normalize-space()='test 1d00gfkj']").text
            if inputname == sdata:
                flag = True
                break
        return flag


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
            inputname = table.find_element(By.XPATH,'//*[@id="864844768121559285_orig"]/tbody/tr[2]/td[4]/a/span').text
            if inputname == sdata:
                flag = True
                break
        return flag

#_test