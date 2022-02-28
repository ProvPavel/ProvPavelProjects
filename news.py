from requests import request
from bs4 import BeautifulSoup

url = 'https://yandex.ru/news?msid=1645874415555541-10935585541354775902-sas5-9946-38a-sas-l7-balancer-8080-BAL-8146&mlid=1645873938.glob_225&utm_source=morda_desktop&utm_medium=topnews_news'
html = request(method='GET', url=url).content.decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')
for i in soup.find_all('div', class_='mg-card__annotation'):
    print(i.text)
