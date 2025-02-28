import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import pytest

class TestWebApp:
    def test_display_all_items(self, driver):
        url = "https://juice-shop.herokuapp.com/#/"
        driver.get(url)
        driver.implicitly_wait(10)

        try:
            welcome_close = driver.find_element(By.CSS_SELECTOR, "#mat-dialog-0 button.close-dialog")
            welcome_close.click()
        except:
            pass

        try:
            cookie_close = driver.find_element(By.CSS_SELECTOR, "body > div.cc-window.cc-floating.cc-type-info.cc-theme-classic.cc-bottom.cc-right.cc-color-override--1225450786 > div > a")
            cookie_close.click()
        except:
            pass

        time.sleep(5)
        ActionChains(driver).scroll_by_amount(0, 1200).perform()
        time.sleep(5)
        
        dropdown = driver.find_element(By.CSS_SELECTOR, "#mat-select-value-1")
        dropdown.click()
        
        explicit_wait = WebDriverWait(driver, 10)
        explicit_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "mat-option")))
        
        options = driver.find_elements(By.CSS_SELECTOR, "mat-option")
        options[-1].click() 
        max_value_text = options[-1].text
        max_value = int(max_value_text) # Clicks the last option (max value)
        time.sleep(5)
        ActionChains(driver).scroll_by_amount(0, 3900).perform()
        time.sleep(10)
        paginator_text = driver.find_element(By.CSS_SELECTOR, "div.mat-paginator-range-label").text 
        total_items = int(paginator_text.split()[-1]) 
        print(f"ℹ️  Selected {max_value} items per page, Total items: {total_items}")
        items = driver.find_elements(By.TAG_NAME, "mat-card")
        
        assert len(items) == total_items, f"Expected {total_items} items but found {len(items)} items"
        
        print(f"✅ Assertion Passed: All {total_items} items are displayed!")

        time.sleep(5)

if __name__ == "__main__":
    pytest.main(["-v", __file__])
