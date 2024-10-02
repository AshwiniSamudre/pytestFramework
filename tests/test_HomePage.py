import time

import pytest

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
from selenium.webdriver.support.select import Select


class TestHomePage(BaseClass):

    def test_FormSubmission(self,getData):

        self.driver.implicitly_wait(10)

        homepage = HomePage(self.driver)
        homepage.getName().send_keys(getData["firstname"])
        homepage.getEmail().send_keys(getData["email"])
        homepage.getPassword().send_keys(getData["password"])
        homepage.getCheckBox().click()

        sel = Select(homepage.getGender())
        sel.select_by_visible_text(getData["Gender"])

        homepage.getradioButton().click()
        homepage.getdateOfBirth().send_keys("DateofBirth")
        homepage.getsubmitButton().click()
        SuccessText=homepage.getConfirmMsg().text
        assert "Success" in SuccessText
        time.sleep(5)
        self.driver.refresh()

###reading data from the home data page keyworddriven (use dictonary for key value pairs)
    @pytest.fixture(params=HomePageData.test_homepage)
    def getData(self,request):
        return request.param




