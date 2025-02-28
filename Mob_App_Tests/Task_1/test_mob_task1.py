import time
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
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

    def test_app_navigation(self, driver):
        #Scroll Down
            try:
                time.sleep(5) 
                driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().scrollable(true)).scrollToEnd(2)')
                print("✅ Scrolled down successfully!")
            except Exception as e:
                pytest.fail(f"❌ Test Failed: {e}")
 
            try:
                my_list_icon = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("org.wikipedia.alpha:id/icon").instance(1)')
                my_list_icon.click()
                time.sleep(3)
                print("✅ Successfully clicked My List icon and stayed for 3 seconds!")
            except Exception as e:
                pytest.fail(f"❌ Test Failed: {e}")
                
            try: 
                history_icon = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("org.wikipedia.alpha:id/icon").instance(2)')
                history_icon.click()
                time.sleep(3)
                print("✅ Successfully clicked History icon and stayed for 3 seconds!")
            except Exception as e:
                pytest.fail(f"❌ Test Failed: {e}")     
                
            try: 
                nearby_icon = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("org.wikipedia.alpha:id/icon").instance(3)')
                nearby_icon.click() 
                time.sleep(3)
                print("✅ Successfully clicked Nearby icon and stayed for 3 seconds!")
            except Exception as e:
                pytest.fail(f"❌ Test Failed: {e}")
            
            try: 
                home_icon = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("org.wikipedia.alpha:id/icon").instance(0)') 
                home_icon.click()
                print("✅ Successfully returned to Home Page!")
            except Exception as e:
                pytest.fail(f"❌ Test Failed: {e}")
            try: 
                # Scroll Up 
                driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().scrollable(true)).scrollToBeginning(2)')

                print("✅ Scrolled up successfully!")       

            except Exception as e:
                pytest.fail(f"❌ Test Failed: {e}")
                

if __name__ == "__main__":
    pytest.main(["-v", __file__])
