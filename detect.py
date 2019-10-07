import time
from bs4 import BeautifulSoup
import  requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

response = requests.get("https://web.whatsapp.com/")
soup = BeautifulSoup(response.text, 'html.parser')


driver=webdriver.Chrome("F:\chromedriver\chromedriver.exe")
driver.get("https://web.whatsapp.com/")
time.sleep(10)

item=driver.find_element_by_xpath('//span[@title="Bro"]')
item.click()
data=driver.find_element_by_xpath('//div[@class="_3u328 copyable-text selectable-text"]')
#data.send_keys("Hiii dudeeee")
last_seen_status=driver.find_element_by_xpath('//span[@class="_315-i"]')
while 1:
    if last_seen_status.text=='online':
        data.send_keys("Hiii dudeeee")
        data.send_keys(Keys.RETURN)

    time.sleep(2)







