from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Automatically download correct ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    driver.get("https://the-internet.herokuapp.com/login")
    driver.maximize_window()

    wait = WebDriverWait(driver, 10)

    username = wait.until(EC.presence_of_element_located((By.ID, "username")))
    username.send_keys("tomsmith")

    password = driver.find_element(By.ID, "password")
    password.send_keys("SuperSecretPassword!")

    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()

    success_message = wait.until(
        EC.presence_of_element_located((By.ID, "flash"))
    )

    print("Login Test Passed")
    time.sleep(3)

except Exception as e:
    print("Test Failed:", e)

finally:
    driver.quit()