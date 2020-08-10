from bs4 import BeautifulSoup as bs
import requests
params = (
    ('query', '\uB178\uD2B8\uBD81'),
    ('frm', 'NVSHATC'),
    ('prevQuery', '\uB178\uC774\uC988 \uCE94\uC2AC\uB9C1'),
)

response = requests.get('https://search.shopping.naver.com/search/all', params=params)

soup = bs(response.text, 'html.parser')
list_ = soup.select_one("#__NEXT_DATA__").text

print(list_)