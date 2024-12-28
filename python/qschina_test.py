import requests
from bs4 import BeautifulSoup
import io
import sys

#sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def parse_html(year):
#     url = "file://./qschina.cn_en_2023.html"
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')

    text = ''
    path = 'test.html'
    with open(path, 'r', encoding='utf-8') as file:
        text = file.read()
    soup = BeautifulSoup(text, 'html.parser')
    soup.prettify()

    ranking_data = []
    table = soup.find('table')
    if table:
        rows = table.find_all('tr')[1:]  #
        print("len:%s"%(len(rows)))
        for row in rows:
            cols = row.find_all('td')
#             print("len:%s"%(len(cols)))
            if len(cols) >= 2:
                ranking_info = {
                    "rank": cols[0].text.strip(),
                    "university": cols[1].find('a').text.strip(),
#                     "country": cols[1].find('a').text.strip(),
#                     "total_score": cols[3].text.strip(),
#                     "country_rank": cols[4].text.strip()
                }
                print(ranking_info['university'])
                ranking_data.append(ranking_info)
    return ranking_data

year = 2022
year = 2023
# year = 2024
rankings = parse_html(year)
for ranking in rankings:
#     print(ranking)
    print(ranking['rank'])
    print(ranking['university'])
