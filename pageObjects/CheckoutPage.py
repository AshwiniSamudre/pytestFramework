from selenium.webdriver.common.by import By

from pageObjects.confirmPage import ConfirmPage


class CheckoutPage:

    def __init__(self,driver):
        self.driver = driver

    products = (By.XPATH, "//div[@class='card h-100']")
    productName = (By.XPATH, "//div[@class='card h-100']//div/h4/a")
    # productName = (By.XPATH, "div/h4/a")
    checkoutButton = (By.XPATH,"//a[@class='nav-link btn btn-primary']")


    def getProducts(self):
        return self.driver.find_elements(*CheckoutPage.products)

    def getProductName(self):
        return self.driver.find_element(*CheckoutPage.productName)

    def getCheckoutButton(self):
        # return self.driver.find_element(*CheckoutPage.checkoutButton)
        self.driver.find_element(*CheckoutPage.checkoutButton).click()
        Confirm = ConfirmPage(self.driver)
        return Confirm

