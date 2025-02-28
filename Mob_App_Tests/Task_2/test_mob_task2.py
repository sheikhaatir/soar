#Task 2 
import time
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.options.common import AppiumOptions
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from appium.webdriver.common.appiumby import AppiumBy
import pytest

desired_cap = {
    "appium:automationName": "UiAutomator2",
    "appium:platformName": "Android",
    "appium:platformVersion": "15",
    "appium:deviceName": "1cd698977d77",
    "appium:app": "C:\\Users\\mahum\\OneDrive\\Desktop\\Automation\\soar\\app\\org.wikipedia.alpha.apk",
    "appium:noReset": True
    
}

# Load Capabilities
appium_options = AppiumOptions()
appium_options.load_capabilities(desired_cap)

class TestMobileApp:
    @pytest.fixture
    def driver(self):
        try:
            self.driver = webdriver.Remote("http://127.0.0.1:4723", options=appium_options)
            print(f"Connected to Appium server with session ID: {self.driver.session_id}")
            self.driver.implicitly_wait(20)
            yield self.driver  
        except WebDriverException as e:
            pytest.fail(f"Error connecting to Appium server: {e}")
        finally:
            if hasattr(self, "driver"):
                self.driver.quit()

    def test_search_bar(self, driver):
            try:
                search_tab = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("org.wikipedia.alpha:id/fragment_feed_header")')))
                search_tab.click() 
                search_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("org.wikipedia.alpha:id/search_src_text")')))
                search_input.click()
                search_input.clear()
                time.sleep(3)
                search_input.send_keys("New York")
                print("✅ Successfully entered 'New York' in the search bar")
                #ASSERTION 
                search_results = WebDriverWait(driver, 10).until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("org.wikipedia.alpha:id/page_list_item_title")')))
                assert search_results.is_displayed(), "❌ Search results did not appear!"
                print("✅ Search results appeared successfully!")

            except Exception as e:
                pytest.fail(f"❌ Test Failed: {e}")
            try:
                close_button = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("org.wikipedia.alpha:id/search_close_btn")')
                close_button.click()
                time.sleep(3)
                close_button.click()
                print("✅ Successfully clicked the close button")
                print("✅ Returned to Home Page!")
            except Exception as e:
                pytest.fail(f"❌ Test Failed: {e}")
                

if __name__ == "__main__":
    pytest.main(["-v", __file__])
