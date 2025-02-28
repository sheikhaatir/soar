# Test Case 2 
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pytest

class TestWebApp:
    def test_product_details(self, driver):
        url = "https://juice-shop.herokuapp.com/#/"
        driver.get(url)
        driver.implicitly_wait(10)

        try:
            welcome_close = driver.find_element(By.CSS_SELECTOR, "#mat-dialog-0 button.close-dialog")
            welcome_close.click()
        except Exception as e:
            print(f"Welcome banner not found or already closed: {e}")

        try:
            cookie_close = driver.find_element(By.CSS_SELECTOR, "body > div.cc-window.cc-floating.cc-type-info.cc-theme-classic.cc-bottom.cc-right.cc-color-override--1225450786 > div > a")
            cookie_close.click()
        except Exception as e:
            print(f"Cookie consent not found or already closed: {e}")


if __name__ == "__main__":
    pytest.main(["-v", __file__])
    