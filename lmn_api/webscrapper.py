# pip install requests
# pip install b24

import requests
from time import sleep
from bs4 import BeautifulSoup


def main():
    getMPLS()


def getMPLS():
    # http://minneapolis.eventful.com/events/categories/music#!page_number=1&category=music

    for page in range(1, 10):
        # result = requests.get("http://minneapolis.eventful.com/events/categories/music")
        httpString = "http://minneapolis.eventful.com/events/categories/music?page_number=" + str(
            page) + "&category=music"
        print(httpString)
        result = requests.get(httpString)
        sleep(1)
        print(result.status_code)

        c = result.content
        soup = BeautifulSoup(c, "html.parser")
        # print(soup)

        samples = soup.find_all("h4")

        # print()
        # print("Page Set Number: " + str(page))
        # for item in samples:
        #     print(item)
        # print()
        # print()

        # soup = BeautifulSoup(c, "html.parser")

        samples2 = soup.find_all("a", 'tn-frame')
        print()
        print('inner loop through page number: ' + str(page))
        for item in samples2:
            myURL = item.get('href')
            myURL = "http:" + myURL
            result = requests.get(myURL)
            c = result.content
            minisoup = BeautifulSoup(c, "html.parser")
            samples3 = minisoup.find("meta", {"name": "description"})['content']
            print(samples3)
        print()
        print()


main()

# https://stackoverflow.com/questions/11205386/python-beautifulsoup-get-an-attribute-value-based-on-the-name-attribute/11205758
