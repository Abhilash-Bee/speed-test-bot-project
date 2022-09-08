import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from check_internet_speed import CheckSpeed

chrome_path_driver = "L:\Development\chromedriver.exe"
driver = webdriver.Chrome(service=Service(chrome_path_driver))
driver.get("https://www.speedtest.net/")

internet_speed = CheckSpeed(driver, By)

internet_speed.go()
time.sleep(60)
internet_speed.return_data()
