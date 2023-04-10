from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.get("file://C:/Users/Alon/Downloads/tip_calc/tip_calc/index.html")
billamt = driver.find_element(by="id", value="billamt")
billamt.send_keys("100")
s = driver.find_element(by="xpath", value="//*[@id=\"serviceQual\"]/option[5]")
s.click()
peopleamt = driver.find_element(by="id", value="peopleamt")
peopleamt.send_keys(5)
musicamt = driver.find_element(by="id", value="musicamt")
musicamt.send_keys(5)
finish = driver.find_element(by="xpath", value="//*[@id=\"calculate\"]")
finish.click()
excpected = "7.00"
actual = driver.find_element(by="id", value="tip").text
# assert excpected == actual
if excpected == actual:
    print("tip calculation is ok")
sleep(5)
driver.close()

