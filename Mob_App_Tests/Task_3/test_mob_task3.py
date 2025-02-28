#Task 3
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
                ellipses = driver.find_element(By.ID, "org.wikipedia.alpha:id/menu_overflow_button")
                ellipses.click()
                
                settings_option = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("org.wikipedia.alpha:id/explore_overflow_settings")')
                settings_option.click()
                
                print("✅ Settings page opened successfully")
                time.sleep(2)
                
            except Exception as e:
                pytest.fail(f"❌ Test Failed: {e}")
                
            try: 
                toggles = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.Switch")
                print('⚙️  Total toggles ', len(toggles))
                
                for toggle in toggles:
                    if toggle.get_attribute("checked") == "true":
                        toggle.click()
                        print("✅ Toggle switched off successfully")
                        
            except Exception as e:
                pytest.fail(f"❌ Test Failed: {e}")
                
            try: 
                back_button = driver.find_element(AppiumBy.CLASS_NAME, 'android.widget.ImageButton')
                back_button.click()
                print("✅ Successfully navigated back to the main screen")
            except Exception as e:
                pytest.fail(f"❌ Test Failed: {e}")
                

if __name__ == "__main__":
    pytest.main(["-v", __file__])
