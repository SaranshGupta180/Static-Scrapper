from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
file = 1
driver = webdriver.Chrome()
for i in range(0,100):
    driver.get("https://www.google.com/search?sca_esv=1eda6e0add178775&sca_upv=1&tbs=lf:1,lf_ui:2&tbm=lcl&q=best+school+in+jaipur&rflfq=1&num=10&sa=X&sqi=2&ved=2ahUKEwit-_XKvq2HAxV7RWwGHUNUAOoQjGp6BAgnEAE&biw=1214&bih=681&dpr=1#rlfi=hd:;si:;mv:[[26.964656700000003,75.86407229999999],[26.7896625,75.6551236]];start:{q}")
    elems = driver.find_elements(By.CLASS_NAME,"VkpGBb")
    for elem in elems:
        d= elem.get_attribute("outerHTML")
        with open(f"School/SchoolData/{file}.html","w",encoding="utf-8" )as f:
            f.write(d)
            file += 1
    time.sleep(2)
driver.close()        