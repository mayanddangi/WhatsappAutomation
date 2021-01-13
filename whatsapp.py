'''
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

name = input('Enter the name of user or group : ')
msg = input('Enter your message : ')
count = int(input('Enter the count : '))

input('Enter anything after scanning QR code')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_class_name('DuUXI')

for i in range(count):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_3qpzV')
    button.click()
'''

from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://web.whatsapp.com')

driver.find_element_by_css_selector("span[title='" + input("Enter name to spam: ") + "']").click()
inputString = input("Enter message to send: ")

for i in range(0,1000):
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(inputString)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()

    
