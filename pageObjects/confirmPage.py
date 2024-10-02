from selenium.webdriver.common.by import By


class ConfirmPage():

    def __init__(self,driver):
        self.driver = driver

    CheckoutButton = (By.XPATH, "//button[@class='btn btn-success']")
    dropDown = (By.ID, "country")
    # selectDropDown = (By.XPATH, "//div[@class='suggestions']//li/a")
    selectDropDown = (By.LINK_TEXT,"India")
    checkBox = (By.XPATH, "//input[@id='checkbox2']")
    purchesbutton = (By.XPATH, "//input[@type='submit']")
    succesText = (By.CLASS_NAME, "alert")

    def getCheckoutButton(self):
        return self.driver.find_element(*ConfirmPage.CheckoutButton)

    def getDropDownMenu(self):
        return self.driver.find_element(*ConfirmPage.dropDown)

    def getSelectDropDown(self):
        return self.driver.find_element(*ConfirmPage.selectDropDown)

    def getCheckBox(self):
        return self.driver.find_element(*ConfirmPage.checkBox)

    def getPurchesButton(self):
        return self.driver.find_element(*ConfirmPage.purchesbutton)

    def getSuccessText(self):
        return self.driver.find_element(*ConfirmPage.succesText)