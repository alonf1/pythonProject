from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/cookieclicker/")
sleep(5)
st = driver.find_element(by="xpath", value="//*[@id=\"langSelect-EN\"]")
st.click()
sleep(5)
c = driver.find_element(by="xpath", value="//*[@id=\"bigCookie\"]")
for i in range(500):
    c.click()
    sleep(0.1)
driver.close()