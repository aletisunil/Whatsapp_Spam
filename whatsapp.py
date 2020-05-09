from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


driver=webdriver.Chrome("") #Enter Location of Chrome driver
driver.maximize_window()
driver.get("https://web.whatsapp.com/")
sleep(15)
driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/div[1]/div/div/div[1]/div/div/div").click()
sleep(5)
fileLocation= ""  #Enter location of movie script file
with open(fileLocation,"r") as file:
    for line in file:
        for word in line.split(" "):
            driver.find_element_by_xpath("//*/footer/div[1]/div[2]/div/div[2]").send_keys(word)
            driver.find_element_by_xpath("//*/footer/div[1]/div[2]/div/div[2]").send_keys(Keys.ENTER)
