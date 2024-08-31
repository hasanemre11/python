from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()

driver = webdriver.Chrome()

driver.get("https://orteil.dashnet.org/experiments/cookie/")

while True:
    cookie = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "cookie"))
    )

    cookie.click()



