### 실습 한국 경제 부분
from bs4 import BeautifulSoup
import requests

keyword = input('검색어 : ')
count = 0

for page in range(1, 3):
    url = 'https://search.hankyung.com/apps.frm/search.news?query='+keyword+'&mediaid_clust=HKPAPER,HKCOM&page=' + str(page)

    response = requests.get(url)

    soup = BeautifulSoup(response.text,'html.parser')

    box = soup.find('div', {'class' : 'section_cont'})
    date_time = box.find_all('span',{'class' : 'date_time'})
    titles = box.find_all('em' ,{'class' : 'tit'})

    for i in range(0,10):
        count +=1
        title = titles[i]
        date = date_time[i]
        print(str(count)+' - { '+date.text+' } '+title.text.strip())