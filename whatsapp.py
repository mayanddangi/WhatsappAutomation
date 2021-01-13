from selenium import webdriver
driver = webdriver.Chrome()

driver.get('https://web.whatsapp.com')

driver.find_element_by_css_selector("span[title='" + input("Enter name to spam: ") + "']").click()
message = input("Enter message to send: ")

for i in range(0,1000):
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()

    
