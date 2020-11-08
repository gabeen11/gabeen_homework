#네이버 날씨 크롤링
from urllib.request import urlopen, Request
import urllib
import bs4

location = input()
enc_location = urllib.parse.quote(location + '+ 날씨')

url = "https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=" + enc_location

req = Request(url)
page = urlopen(req)
html = page.read()
soup = bs4.BeautifulSoup(html,"html.parser")


# 기온별 옷차림 정보

if temperature <= 4:
    print("적당한 옷차림은 패딩, 두꺼운 코트, 누빔 옷, 기모, 목도리 입니다.")

elif 5 <= temperature <= 8:
    print("적당한 옷차림은 울 코트, 히트텍, 가죽 옷, 기모 입니다.")

elif 9 <= temperature <= 11:
    print("적당한 옷차림은 트렌치 코트, 야상, 점퍼, 스타킹, 기모바지 입니다.")

elif 12 <= temperature <= 16:
    print("적당한 옷차림은 자켓, 가디건, 청자켓, 니트, 스타킹, 청바지 입니다.")

elif 17 <= temperature <= 19:
    print("적당한 옷차림은 얇은 가디건, 얇은 니트, 맨투맨, 후드, 긴 바지 입니다.")

elif 20 <= temperature <= 22:
    print("적당한 옷차림은 블라우스, 긴팔 티, 면바지, 슬랙스 입니다.")
    
elif 23 <= temperature <= 27:
    print("적당한 옷차림은 반팔, 얇은 셔츠, 반바지, 면바지 입니다.")
    
elif 28 <= temperature:
    print("적당한 옷차림은 민소매, 반팔, 반바지, 짧은 치마, 린넨 옷 입니다.")
   