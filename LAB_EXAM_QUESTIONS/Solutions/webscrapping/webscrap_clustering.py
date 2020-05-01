'''
problem : 4 - web scraping with for clustering models
'''
from webscrapping.webreader import read_web_page
from bs4 import BeautifulSoup


def web_scrap():
    raw_html = read_web_page("https://scikit-learn.org/stable/modules/clustering.html#clustering")
    soup = BeautifulSoup(raw_html, 'html.parser')
    table = soup.find("table", {"class": "colwidths-given docutils"})
    for head in table.find_all("th", {"class": "head"}):
        print(head.text, end="\t\t\t")
    print("\n---------------------------------------------------------------------------------------------------")
    for tr in table.find("tbody").find_all("tr"):
        for td in tr.find_all("td"):
            print(td.text, end="\t\t\t")
        print()


web_scrap()
