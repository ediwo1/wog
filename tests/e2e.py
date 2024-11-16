import sys
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_scores_service(url):
    opt = webdriver.ChromeOptions()
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome(options=opt)
    driver.get(url)
    score_txt = driver.find_element(By.ID, 'header').text
    print(score_txt)
    return int(score_txt)

def main_function():
    score_value = test_scores_service('http://localhost:8777')
    if 1 <= score_value <= 1000:
        print(f"The value {score_value} is within the range 1 to 1000.")
    else:
        print(f"Error: The value {score_value} is out of range (1 to 1000). Exiting...")
        sys.exit(1)

main_function()