from selenium import webdriver

def retrieve_list_of_items(url, xpath):
    driver = webdriver.Chrome()
    driver.get(url)

    element = driver.find_element_by_xpath(xpath)

    # Get the parent element that contains the list of items
    parent_element = element.find_element_by_xpath("..")

    # Get all the child elements of the parent element
    child_elements = parent_element.find_elements_by_xpath("./*")

    # Loop through the child elements and print their text
    for child in child_elements:
        print(child.text)

    driver.quit()

if __name__ == "__main__":
    retrieve_list_of_items("https://www.yourwebsite.com", '//*[@id="__next"]/div[1]/div[2]/div/div/nav/div/div/a[2]')
