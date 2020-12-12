from selenium import webdriver
import  time

URL = "https://mangasee123.com/read-online/Naruto-chapter-1.html"


def get_url():
    driver = webdriver.Firefox()
    driver.get(URL)
    time.sleep(10)
    images = driver.find_elements_by_class_name('img-fluid')
    for image in images:
        print(image.get_attribute('alt'),image.get_attribute('src'))
    driver.close()

get_url()
