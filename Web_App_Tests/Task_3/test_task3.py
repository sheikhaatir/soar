# Task 3 
import time
import random 
import string
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
import pytest

# generate random email, ,passwrod and security answer
def generate_random_email():
        return ''.join(random.choices(string.ascii_letters + string.digits, k=8)) + "@test.com"
def generate_random_password():
    return ''.join(random.sample(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation, 8) + 
                   [random.choice(string.ascii_lowercase), random.choice(string.ascii_uppercase), 
                    random.choice(string.digits), random.choice(string.punctuation)])
def generate_random_security_answer():
    return ''.join(random.choices(string.ascii_letters, k=10))



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
            account_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#navbarAccount')))
            account_button.click()
            time.sleep(10)
            
            login_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#navbarLoginButton')))
            login_button.click()
            time.sleep(10)
            
            registration_page =  driver.find_elements(By.CSS_SELECTOR, "#newCustomerLink > a")
            registration_page[0].click()
            time.sleep(10)
            print('✅ Registration page opened')
            
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#emailControl"))).click()
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#passwordControl"))).click()           
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#repeatPasswordControl"))).click()
            time.sleep(3)
            print('✅ All input fields clicked')
            
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#mat-slide-toggle-1 > label > span.mat-slide-toggle-bar"))).click()
            print('✅ Toggle switch clicked')  
            time.sleep(3)
            
            security_question = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="registration-form"]/div[1]/mat-form-field[1]/div/div[1]/div[3]')))
            driver.execute_script("arguments[0].scrollIntoView();", security_question)
            time.sleep(2)
            security_question.click()
            print('✅ Security question clicked')
            time.sleep(3)
            overlay = driver.find_element(By.CSS_SELECTOR, "body > div.cdk-overlay-container.bluegrey-lightgreen-theme > div")
            actions = ActionChains(driver)
            actions.double_click(overlay).perform()
            
            answer_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#securityAnswerControl')))
            driver.execute_script("arguments[0].scrollIntoView();", answer_field)
            time.sleep(3)
            answer_field.click()    
            time.sleep(3)
            element = driver.find_element(By.CSS_SELECTOR, "#registerButton").click()
            time.sleep(3)
            print('✅ Answer field clicked')
            time.sleep(3)
                         
            error_elements = driver.find_elements(By.CSS_SELECTOR, "mat-error")
            
            assert error_elements, "❌ No validation errors found!"
            print('✅ Assertion Passed: Validation errors found')
            time.sleep(3)            
        except Exception as e:
            driver.save_screenshot("debug_screenshot.png")  ##Enable in case of debugging
            pytest.fail(f"❌ Test Failed: {e}")
            
        try: 
            # Generate random user details
            email = generate_random_email()
            password = generate_random_password()
            security_answer = generate_random_security_answer()
            print(f"✅ Generated random email: {email} | password: {password} | security answer: {security_answer}")
            
            email_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#emailControl")))
            email_field.send_keys(email)
            print('✅ Email entered')
            time.sleep(3)
            
            password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#passwordControl')))
            password_field.send_keys(password)
            print('✅ Password entered')
            time.sleep(3)
            driver.save_screenshot("email_password_entered.png")
            
            repeat_password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#repeatPasswordControl')))
            repeat_password_field.send_keys(password)
            print('✅ Repeat password entered')
            print('📸 Screenshot saved: email_password_entered.png')
            time.sleep(3)
            
            security_question = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="registration-form"]/div[1]/mat-form-field[1]/div/div[1]/div[3]')))
            driver.execute_script("arguments[0].scrollIntoView();", security_question)
            time.sleep(2)
            security_question.click()
            security_options = driver.find_elements(By.CSS_SELECTOR, "mat-option")
            security_options[-1].click()
            print('✅ Security question selected')
            time.sleep(3)
            
            answer_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#securityAnswerControl')))
            driver.execute_script("arguments[0].scrollIntoView();", answer_field)
            answer_field.send_keys(security_answer)
            print('✅ Security answer entered')
            
            register_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#registerButton')))
            driver.execute_script("arguments[0].scrollIntoView();", answer_field)
            register_button.click()
            time.sleep(5)
            
            
            success_message = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".mat-snack-bar-container"))).text
            assert "Registration completed successfully. You can now log in." in success_message, "Success message did not match!"            
            print('✅ Registration successful')
            driver.save_screenshot("registration_successful_assertion.png")
            time.sleep(3)
            
        except Exception as e:
            #pytest.fail(f"❌ Test Failed: {e}")
            print('❌ Field not found')
            driver.save_screenshot("email_field_not_found.png")
            pytest.fail("ield not visible or not found on the page")
            
        try: 
            #Login
            login_email = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#email')))
            login_email.send_keys(email)
            time.sleep(1)      
            login_password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#password')))
            login_password.send_keys(password)
            time.sleep(3)
            
            login_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#loginButton')))
            login_button.click()
            time.sleep(5)
            driver.save_screenshot("login_successful.png")
            print("✅ Test Passed: Login successful")
        except Exception as e:
            pytest.fail(f"❌ Test Failed: {e}")
if __name__ == "__main__":
    pytest.main(["-v", __file__])
    
