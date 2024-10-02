import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.HomePage import HomePage
from pageObjects.confirmPage import ConfirmPage
from utilities.BaseClass import BaseClass

class TestOne(BaseClass):
    def test_e2e(self):
        self.driver.implicitly_wait(5)
        log = self.getLogger()

        homepage = HomePage(self.driver)
        checkoutpage = CheckoutPage(self.driver)

        checkout = homepage.shopItem()
        log.info("getting all products:")
        products = checkoutpage.getProducts()
        log.info(products)

        for product in products:
            # productName = self.driver.find_element(By.XPATH,"//h4[@class='card-title']").text
            productName = product.find_element(By.XPATH, "div/h4/a").text
            # productName = checkoutpage.getProductName().text
            # productName= checkoutpage.getProductName()
            #print(productName.text)

            log.info(productName)
            if productName == "Blackberry":
                product.find_element(By.XPATH, "div/button").click()
                # checkoutpage.getProductName().click()
                time.sleep(5)


        ConfirmPage = checkout.getCheckoutButton()
        # Confirm = ConfirmPage(self.driver)
        ConfirmPage.getCheckoutButton().click()
        log.info("entering country name indi")
        ConfirmPage.getDropDownMenu().send_keys("Indi")

        action = ActionChains(self.driver)

        self.verifyLinkText("India")
        # Confirm.getSelectDropDown().click()

        checkbox = ConfirmPage.getCheckBox()
        action.move_to_element(checkbox).click(checkbox).perform()
        ConfirmPage.getPurchesButton().click()
        succucesText = ConfirmPage.getSuccessText()

        log.info(succucesText.text)
        assert "Success!" in succucesText.text
