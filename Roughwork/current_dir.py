from selenium import webdriver
import os

print(os.getcwd())
driver_loc = os.getcwd().replace("\\", "/") + "/Driver"

print(os.getcwd().replace("\\","/").replace("Mercurydemo", ""))
driver = webdriver.Chrome(executable_path=driver_loc + "/chromedriver.exe")