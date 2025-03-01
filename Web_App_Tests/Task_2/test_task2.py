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
            cookie_close = driver.find_element(By.CSS_SELECTOR, "body > div.cc-window.cc-floating.cc-type-info.cc-theme-classic.cc-bottom.cc-right.cc-color-override--1225450786 > div > a")
            cookie_close.click()
        except Exception as e:
            print(f"Cookie/Welcome consent not found or already closed: {e}")
            
        try: 
            first_product = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-search-result/div/div/div[2]/mat-grid-list/div/mat-grid-tile[1]/div/mat-card')))
            first_product.click()
            print("✅ First product clicked")
            
            driver.save_screenshot("after_click.png")
            print("📸 Screenshot saved: after_click.png")
            time.sleep(10)
            
            product_popup = driver.find_elements(By.CSS_SELECTOR, "mat-dialog-container")
            if driver.find_elements(By.CSS_SELECTOR, "mat-dialog-container"):
                print("✅ Popup is displayed")
            else:
                print("❌ Popup is not displayed")
            assert product_popup[0].is_displayed(), "Popup did not appear after clicking on 'Apple Juice'."
            
            time.sleep(5)
            expand_review = driver.find_element(By.CSS_SELECTOR, "#mat-expansion-panel-header-0")
            time.sleep(5)
            expand_review.click()
            print("✅ Review expanded")
            time.sleep(5)
            wait = WebDriverWait(driver, 10)
            
            close_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.mat-focus-indicator.close-dialog.buttons.mat-stroked-button.mat-button-base")))
            driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", close_button)
            time.sleep(5)
            close_button.click()
            print("✅ Popup closed")
            time.sleep(5)
        except Exception as e:
            pytest.fail(f"❌ Test Failed: {e}")

if __name__ == "__main__":
    pytest.main(["-v", __file__])
    