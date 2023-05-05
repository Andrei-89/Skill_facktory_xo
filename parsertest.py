import requests # для отправки http запросов на сервер
from lxml import etree
import lxml.html


html = requests.get('https://www.python.org/').content  # получим html главной странички официального сайта python

tree = lxml.html.document_fromstring(html)
title = tree.xpath(
    '/html/head/title/text()')  # забираем текст тега <title> из тега <head> который лежит в свою очередь внутри тега <html> (в этом невидимом теге <head> у нас хранится основная информация о страничке. Её название и инструкции по отображению в браузере.
date_link = tree.xpath('//*[@id="content"]/div/section/div[2]/div[1]/div/ul/li[1]/time/text()')
ul = tree.findall('//*[@id="content"]/div/section/div[2]/div[1]/div/ul')
print(ul)
# print(title)
# print(date_link)

# if __name__ == '__main__':
