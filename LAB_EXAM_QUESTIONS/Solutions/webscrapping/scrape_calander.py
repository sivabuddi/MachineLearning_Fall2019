'''
problem : 4 - web scraping with dynamic content.
'''

from bs4 import BeautifulSoup
from selenium import webdriver
import os

dir_path = os.path.join(os.getcwd(), "chromedriver")
print(dir_path)

browser = webdriver.Chrome(executable_path=dir_path)
browser.get("https://www.umkc.edu/calendar/")

iframe = browser.find_element_by_id("trumba.spud.4.iframe")
browser.switch_to.default_content()
browser.switch_to.frame(iframe)

iframe_source = browser.page_source
browser.close()
soup = BeautifulSoup(iframe_source, 'html.parser')

for row in soup.find(class_='twSimpleTableTable').find("tbody").find_all("tr"):
    print_string = ""
    for column in row.find_all(['td', 'th']):
        print_string = print_string + column.get_text() + "\t\t\t"
    print(print_string)
