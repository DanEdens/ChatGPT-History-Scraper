import os
import requests
import zipfile
import io
from selenium import webdriver

class RetrieveListOfItems:
    def __init__(self, url, xpath):
        self.url = url
        self.xpath = xpath
        self.driver = webdriver.Chrome()

    def __enter__(self):
        self.driver.get(self.url)
        element = self.driver.find_element_by_xpath(self.xpath)
        parent_element = element.find_element_by_xpath("..")
        self.child_elements = parent_element.find_elements_by_xpath("./*")
        return self

    def __exit__(self, type, value, traceback):
        self.driver.quit()

    def print_items(self):
        for child in self.child_elements:
            print(child.text)


def check_and_download_webdriver(webdriver_path):
    if os.path.exists(webdriver_path):
        return
    
    URL = "https://sites.google.com/a/chromium.org/chromedriver/downloads"
    r = requests.get(URL)

    # Extract the download link for the Chrome webdriver
    download_link = None
    for line in r.iter_lines():
        line = line.decode("utf-8")
        if "chromedriver_linux64.zip" in line:
            download_link = line.split("href=\"")[1].split("\"")[0]
            break

    # Download the Chrome webdriver
    r = requests.get(download_link)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall(os.path.dirname(webdriver_path))

if __name__ == "__main__":
    check_and_download_webdriver("/usr/local/bin/chromedriver")
    with RetrieveListOfItems("https://chat.openai.com/chat", '//*[@id="__next"]/div[1]/div[2]/div/div/nav/div/div/a[2]') as items:
        items.print_items()