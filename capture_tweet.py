from selenium import webdriver

driver = webdriver.Firefox()

driver.get('https://twitter.com/monoa22s/status/580976044758282240')

driver.save_screenshot('/home/shamison/nbi.png')



