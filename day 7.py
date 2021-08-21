from bs4 import BeautifulSoup #bs4 에서 BeautifulSoup 메소드 import
import requests # HTML코드를 불러오기 위해 import

url = 'https://dhlottery.co.kr/gameResult.do?method=byWin' # 정적크롤링할 주소

raw = requests.get(url) # get()함수로 HTML 코드 문자열로 저장

soup = BeautifulSoup(raw.text,'html.parser') # 문자열로 저장된 HTML코드를 실제 HTML코드로 변환

box = soup.find('div',{'class' : 'nums'}) # HTML 코드에서 'div'태그이고 class가 'nums'인 부분을 찾음
print(box)
numbers = box.find_all('span') # 'box'에서 'span' 태그로 표시된 내용을 모두 찾음, 리스트 형식으로 반환
for n in numbers:
    print(n.text) # 반환된 리스트를 텍스트 형식으로 출력