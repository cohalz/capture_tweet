from selenium import webdriver
from PIL import Image

tweet = "https://twitter.com/_sham258/status/690422084724461569"

driver = webdriver.Firefox()
driver.get(tweet)
driver.save_screenshot('./screen.png')
driver.quit()

image =  Image.open('screen.png')
left = 0
top = 70
right = 590
bottom = 310

image = image.crop((left, top, right, bottom))
image.save('pic.png')
