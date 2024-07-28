from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service


# Replace 'your_webdriver_path' with the path to your WebDriver
service = Service(r'C:\Program Files\Google\Chrome\Application\chrome.exe')
driver = webdriver.Chrome(service=service)


