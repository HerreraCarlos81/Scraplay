import csv
import os
import sys

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
import undetected_chromedriver as uc
import time
import random

# Set the path for the Chrome WebDriver
PATH = Service("src/assets/chromedriver.exe")


# This function converts the path to a relative path for windows
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)


def run_selenium():
    # Chrome Driver options
    options = uc.ChromeOptions()
    options.add_argument('--headless')

    # Create a new Chrome browser driver
    u_driver = uc.Chrome(service=PATH, use_subprocess=True, options=options)

    # Open the Google search results page for "dentists near me"
    u_driver.get("https://www.wethrift.com/")

    u_driver.maximize_window()

    time.sleep(10)

    u_driver.save_screenshot(resource_path("./images/step1.png"))

    element_coupon = u_driver.find_element(by=By.XPATH,value='//*[contains(text(),"ODILEMONOD")]')

    element_coupon.click()

    time.sleep(10)

    u_driver.save_screenshot(resource_path("./images/step2.png"))

    element_yes = u_driver.find_element(By.XPATH, '//span[text()="Yes"]')

    element_yes.click()

    time.sleep(10)

    u_driver.save_screenshot(resource_path("./images/step3.png"))

    element_savings = u_driver.find_element(By.XPATH, '//*[@id="FKF9YVB8L"]/button/div/div/div[2]/div/input')

    # Generate a random number between 100 and 60000
    random_number = round(random.uniform(100, 60000), 2)

    # Input the generated number
    element_savings.send_keys(random_number)

    time.sleep(10)

    u_driver.save_screenshot(resource_path("./images/step4.png"))

    element_submit = u_driver.find_element(By.XPATH, '//*[@id="FKF9YVB8L"]/button/div/div/div[2]/div/div')

    element_submit.click()

    time.sleep(10)

    u_driver.save_screenshot(resource_path("./images/step5.png"))

    element_final_coupon = u_driver.find_element(by=By.XPATH, value='//*[contains(text(),"ODILEMONOD1")]')

    if element_final_coupon:
        # Create code for notifying success
        pass
    else:
        # Create code for notifying failure
        pass

    u_driver.quit()

    return 0


run_selenium()