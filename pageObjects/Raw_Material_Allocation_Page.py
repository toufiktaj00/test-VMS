from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Raw_Material_Allocation:

    navigation = (By.XPATH, '//*[@id="t_Button_navControl"]')
    lnkSetup_module = (By.ID, 't_TreeNav_2')
    lnk_RawMaterialAllocation = (By.LINK_TEXT, 'Raw Materials Allocation')
    btn_Add_id = (By.ID, "btn_add1")
# Dropdown
    drp_Product_Type_xpath = (By.XPATH, '//*[@id="select2-P89_PRODUCT_TYPE-container"]')
    drp_Product_Type_search_field = (By.XPATH, '//*[@id="t_PageBody"]/span/span/span[1]/input')
    drp_Product_Type_search_value = (By.XPATH, '//*[@id="select2-P89_PRODUCT_TYPE-results"]')

    drp_Item_Name_xpath = (By.XPATH, '//*[@id="select2-P89_ITEM_ID1_1-container"]')
    drp_Item_Name_search_field = (By.XPATH, '//*[@id="t_PageBody"]/span/span/span[1]/input')
    drp_Item_Name_search_value = (By.XPATH, '//*[@id="select2-P89_PRODUCT_TYPE-results"]')




    product_name = (By.XPATH, '//*[@id="P89_PRODUCT_NAME_1_LEFT"]')

    btn_slide = (By.ID, 'P89_PRODUCT_NAME_1_MOVE')

    text_total_use = (By.ID, 'P89_TOTAL_USE_1')

    text_wastage_id = (By.ID, "P89_WASTAGE_1")

    btn_Add_All_id = (By.ID, 'addall')

    btn_save_id = (By.ID, 'btn_save2')


#Search

    text_search = (By.ID,'P89_SEARCH')
    table = (By.XPATH, "//div[@class='t-fht-wrapper']")  # //div[@class='t-fht-tbody']
    tableRows = (By.XPATH, "//div[@class='t-fht-tbody']//tr")  # //div[@class='t-fht-tbody']//tr
    tableColumn = (By.XPATH, "//div[@class='t-fht-tbody']//tr//td")


# Edit item

    btn_edit_xpath = (By.XPATH, '//*[@id="613271613162254875_orig"]/tbody/tr[2]/td[5]/a/span/span')
    btn_update_id = (By.XPATH, 'btn_update')
    btn_delete_id = (By.ID,'btn_delete_1')
    btn_cancel_id = (By.ID, 'btn_cancel')


# Child Edit

    btn_details_xpath = (By.XPATH, '//*[@id="613271613162254875_orig"]/tbody/tr[2]/td[6]/a/span[1]/span/b/i')
    btn_child_edit_xpath = (By.XPATH, '//*[@id="staticHTMLTable"]/div/table/tbody[1]/tr/td[9]/a/span/span/img')
    btn_child_update_id = (By.ID, 'btn_update1')
    btn_child_delete_id = (By.ID, 'btn_delete')


# Add Child

    btn_add_child = (By.XPATH, '//*[@id="613271613162254875_orig"]/tbody/tr[2]/td[3]/a/span/span/b/i')

    text_child_total_use = (By.ID, 'P89_TOTAL_USE')
    text_child_wastage = (By.ID, 'P89_WASTAGE')
    btn_add_child_item = (By.XPATH, '//*[@id="addchd"]')
    btn_save_child = (By.ID, 'btn_save1')




# Drop Down

    drp_childItem_Name_xpath = (By.XPATH, '//*[@id="select2-P89_ITEM_ID1-container"]')
    drp_childItem_Name_search_field = (By.XPATH, '//*[@id="t_PageBody"]/span/span/span[1]/input')
    drp_childItem_Name_search_value = (By.XPATH, '//*[@id="select2-P89_ITEM_ID1-results"]')





    def __init__(self, driver):
        self.driver = driver

    def clickonNavigation(self):
        self.driver.find_element(*self.navigation).click()

    def clickSetupMenu(self):
        self.driver.find_element(*self.lnkSetup_module).click()

    def clicklnk_RawMaterialAllocation(self):
        self.driver.find_element(*self.lnk_RawMaterialAllocation).click()

    def clickAdd(self):
        self.driver.find_element(*self.btn_Add_id).click()



#Dropdown
    #ItemType

    def clickdrpProductType(self):
        self.driver.find_element(*self.drp_Product_Type_xpath).click()

    def setProductTypedrpSearchData(self, item):
        self.driver.find_element(*self.drp_Product_Type_search_field).clear()
        self.driver.find_element(*self.drp_Product_Type_search_field).send_keys(item)

    def clickProductTypeSearchData(self):
        self.driver.find_element(*self.drp_Product_Type_search_value).click()


    def clickdrpItemName(self):
        self.driver.find_element(*self.drp_Item_Name_xpath).click()

    def setItemNamedrpSearchData(self, item):
        self.driver.find_element(*self.drp_Item_Name_search_field).clear()
        self.driver.find_element(*self.drp_Item_Name_search_field).send_keys(item)
        self.driver.find_element(*self.drp_Item_Name_search_field).send_keys(Keys.ENTER)

    def clickItemNameSearchData(self):
        self.driver.find_element(*self.drp_Item_Name_search_value).click()






    def selectfromProductName(self, name):
        box=self.driver.find_element(*self.product_name)
        box.select_by_visible_test(name)


    def clickSidebtn(self):
        self.driver.find_element(*self.btn_slide).click()

    def setTotaluse(self, total):
       self.driver.find_element(*self.text_total_use).send_keys(total)


    def setwastage(self, wastage):
       self.driver.find_element(*self.text_wastage_id).send_keys(wastage)

    def clickAddAll(self):
        self.driver.find_element(*self.btn_Add_All_id).click()

    def clickSave(self):
        self.driver.find_element(*self.btn_save_id).click()


# Edit

    def clickEdit(self):
        self.driver.find_element(*self.btn_edit_xpath).click()

    def clickDelete(self):
        self.driver.find_element(*self.btn_delete_id).click()

    def clickUpdate(self):
        self.driver.find_element(*self.btn_update_id).click()

    def clickCancel(self):
        self.driver.find_element(*self.btn_cancel_id).click()


# Child Edit

    def clickDetails(self):
        self.driver.find_element(*self.btn_details_xpath).click()

    def clickChildEdit(self):
        self.driver.find_element(*self.btn_child_edit_xpath).click()

    def clickchildUpdate(self):
        self.driver.find_element(*self.btn_child_update_id).click()

    def clickchildDelete(self):
        self.driver.find_element(*self.btn_child_delete_id).click()



# Add Child

    def clickaddchild(self):
        self.driver.find_element(*self.btn_add_child).click()

    # Drop Down

    def clickchildItemName(self):
        self.driver.find_element(*self.drp_childItem_Name_xpath).click()

    def setchildItemNameSearchData(self, item):
        self.driver.find_element(*self.drp_childItem_Name_search_field).clear()
        self.driver.find_element(*self.drp_childItem_Name_search_field).send_keys(item)

    def clickchildItemNameSearchData(self):
        self.driver.find_element(*self.drp_childItem_Name_search_value).click()



    def setchildTotaluse(self, total):
        self.driver.find_element(*self.text_child_total_use).send_keys(total)

    def setchildwastage(self, wastage):
        self.driver.find_element(*self.text_child_wastage).send_keys(wastage)

    def clickAddchildItem(self):
        self.driver.find_element(*self.btn_add_child_item).click()

    def clickSavechild(self):
        self.driver.find_element(*self.btn_save_child).click()


    #Search

    def setSearchData(self, data):
        self.driver.find_element(*self.text_search).clear()
        self.driver.find_element(*self.text_search).send_keys(data)

    def getNoOfRows(self):
        return len(self.driver.find_elements(*self.tableRows))

    def getNoOfColumns(self):
        return len(self.driver.find_elements(*self.tableColumn))

    def searchItembydata(self, sdata):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element(*self.table)
            inputname = table.find_element(By.XPATH,'//*[@id="613271613162254875_orig"]/tbody/tr[2]/td[2]').text
            if inputname == sdata:
                flag = True
                break
        return flag
