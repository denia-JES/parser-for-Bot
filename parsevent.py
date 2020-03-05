from requests_html import HTMLSession
from bs4 import BeautifulSoup as bs
import sys
import re


class Parser():

    def take_url(self, url):
        session = HTMLSession()
        self.url = url
        self.page = session.get(self.url)
        print(self.page)
        if self.page.status_code == 404:
            sys.exit('Error')
        return self.page.text

    def take_name(self):
        listofNames = []
        soup = bs(self.page.text, "html.parser")
        names = soup.find_all('img', class_='logo')
        for name in names:
            listofNames.append(name['alt'])
        return listofNames

    def take_time(self):
        listofDate = []
        soup = bs(self.page.text, "html.parser")
        dates = soup.find_all('span', class_='date')
        for date in dates:
            if date:
                listofDate.append(date.get_text())
        return listofDate

    def take_description(self):
        listofDescr = []
        soup = bs(self.page.text, "html.parser")
        descript = soup.find_all('p', class_='b-typo')
        for descr in descript:
            if descr:
                listofDescr.append(descr.get_text())
        listofDescr = str(listofDescr)
        listofDescr = listofDescr.replace(r'\n', '')
        listofDescr = listofDescr.replace(r'\t', ' ')
        listofDescr = listofDescr.replace(r'\xa0', ' ')
        listofDescr = listofDescr.replace(r'[', '')
        listofDescr = listofDescr.replace(r']', '')
        listofDescr = listofDescr.replace("', '", 'qwer')

        list = listofDescr.split("qwer")
        print(list)

    def take_town(self):
        listofCity = []
        soup = bs(self.page.text, "html.parser")
        cities=soup.find_all('div', class_='when-and-where')
        for city in cities:
            if city:
                listofCity.append(city.get_text())
        listofCity=str(listofCity)
        print(listofCity)


proces = Parser()
proces.take_url('https://dou.ua/calendar/')
proces.take_town()
