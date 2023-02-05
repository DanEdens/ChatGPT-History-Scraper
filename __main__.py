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

if __name__ == "__main__":
    with RetrieveListOfItems("https://chat.openai.com/chat", '//*[@id="__next"]/div[1]/div[2]/div/div/nav/div/div/a[2]') as items:
        items.print_items()