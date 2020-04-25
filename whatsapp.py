from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver=webdriver.Chrome("/Users/Aleti Sunil/Downloads/setupFiles/chromedriver.exe") #Enter chrome driver location
driver.maximize_window()
driver.get("https://web.whatsapp.com/")
sleep(15)
driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/div[1]/div/div/div[1]/div/div/div").click()
sleep(5)
print("done")
#Enter movie script in file variable
file="Nee kallani patuku vadalananavi Choode na kallu Aa chupulanalla thokuku vellaku Dayaleda aslu Nee kallani patuku vadalananavi Choode na kallu Aa chupulanalla thokuku vellaku Dayaleda aslu Nee kallaki kawali kasthaye Katukala na kalalu Nuvvu nulumuthunte yeraga kandhi Chindene segalu Naa opiri galiki vuyalala vuguthu Unte mungurulu Nuvvu nettesthe yela niturchavatte Nishthoorapu vila vilalu Samajavaragamana Ninu choosi aaga galana Manasu meeda vanasukunna Adhupu cheppa taguna Samajavaragamana Ninu choosi aaga galana Manasu meeda vanasukunna Adhupu cheppa taguna Nee kallani patuku vadalananavi Choode na kallu Aa chupulanalla thokuku vellaku Dayaleda aslu Mallela maasama Manjula haasama Prathi malupulona yeduru padina Vennela vanama Virisina pinchema Virula prapanchama Yenenni vanne chinnelante Ennaga vashama Arre na gaale thagilina Naa neede tharimina Vulakava palakava bhama Entho brathimalina Inthena angana Madhini meetu Madhuramaina manavini vinumá Samajavaragamana Ninu choosi aaga galana Manasu meeda vanasukunna Adhupu cheppa taguna Samajavaragamana Ninu choosi aaga galana Manasu meeda vanasukunna Adhupu cheppa taguna Nee kallani patuku vadalananavi Choode na kallu Aa chupulanalla thokuku vellaku Dayaleda aslu Nee kallaki kawali kasthaye Katukala na kalalu nuvvu nulumuthunte yeraga kandhi Chindene segalu".split(" ")
for i in file:
    driver.find_element_by_xpath("//*/footer/div[1]/div[2]/div/div[2]").send_keys(i)
    driver.find_element_by_xpath("//*/footer/div[1]/div[2]/div/div[2]").send_keys(Keys.ENTER)
    



