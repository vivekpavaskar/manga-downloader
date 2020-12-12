from selenium import webdriver
import requests
import shutil
import time
import os


# Getting Image URLS from the Chapter Page
def get_img_url(url):
    driver = webdriver.Firefox()
    driver.get(url)
    # To complete rendering of page in driver
    time.sleep(7)
    urls = driver.find_elements_by_class_name('img-fluid')
    url_list = []
    for u in urls:
        url_list.append(u.get_attribute('src'))
    driver.close()
    return url_list


# Downloading Images
def image_download(download_location, image_url):
    filename = download_location + image_url.split("/")[-1]
    # Open the url image, set stream to True, this will return the stream content.
    r = requests.get(image_url, stream=True)
    # Check if the image was retrieved successfully
    if r.status_code == 200:
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        r.raw.decode_content = True
        # Open a local file with wb ( write binary ) permission.
        with open(filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)
        print('Image sucessfully Downloaded: ', filename)
    else:
        print('Image Couldn\'t be retreived')


# main
manga_title = str(input("Enter Manga Title : "))
chapter_start = int(input("Download Chapter From : "))
chapter_end = int(input("Download Chapter To : "))

# creating download directory
try:
    os.mkdir("./downloads/")
except OSError as error:
    print(error)

# creating manga directory
try:
    os.mkdir("./downloads/" + manga_title.title() + "/")
except OSError as error:
    print(error)

manga_url_title = "-".join(manga_title.split())
for i in range(chapter_start, chapter_end + 1):
    chapter_url = "https://mangasee123.com/read-online/" + manga_url_title.title() + "-chapter-" + str(i) + ".html"
    # creating chapter directory
    path = "./downloads/" + manga_title.title() + "/" + manga_title.title() + " C" + str(i).zfill(4) + "/"
    try:
        os.mkdir(path)
    except OSError as error:
        print(error)
    img_url_list = get_img_url(chapter_url)
    for img in img_url_list:
        image_download(path, img)
