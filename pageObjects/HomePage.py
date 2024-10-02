from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageObjects.CheckoutPage import CheckoutPage

class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.LINK_TEXT, "Shop")
    Name = (By.NAME,"name")
    Email =(By.NAME,"email")
    Password = (By.ID,"exampleInputPassword1")
    checkBox = (By.ID,"exampleCheck1")
    GenderSelect = (By.ID,"exampleFormControlSelect1")
    radioButton = (By.ID,"inlineRadio2")
    dateOfBirth = (By.NAME,"bday")
    submitButton = (By.XPATH,"//input[@type='submit']")
    confirmMsg = (By.CLASS_NAME,"alert")


    def shopItem(self):
        # return self.driver.find_element(*HomePage.shop)
        self.driver.find_element(*HomePage.shop).click()
        checkout = CheckoutPage(self.driver)
        return checkout

    def getName(self):
        return self.driver.find_element(*HomePage.Name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.Email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.Password)

    def getCheckBox(self):
        return self.driver.find_element(*HomePage.checkBox)

    def getGender(self):
        return self.driver.find_element(*HomePage.GenderSelect)

    def getradioButton(self):
        return self.driver.find_element(*HomePage.radioButton)

    def getdateOfBirth(self):
        return self.driver.find_element(*HomePage.dateOfBirth)

    def getsubmitButton(self):
        return self.driver.find_element(*HomePage.submitButton)

    def getConfirmMsg(self):
        return self.driver.find_element(*HomePage.confirmMsg)
