# Naver Blog Crawler

import requests
from bs4 import BeautifulSoup
from urllib.parse import quote
import re
import pandas as pd

#함수 정의
def delete_iframe(url): #iframe 제거 후 blog.naver.com 붙이기
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"}
    res = requests.get(url,headers=headers)
    res.raise_for_status()
    src_url = "https://blog.naver.com/"+soup.iframe["src"]
    soup = BeautifulSoup(res.text, "lxml")
    return src_url

def scraping(url): #본문 스크랩하는 함수
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"}
    res = requests.get(url,headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    if soup.find("div", attrs={"class":"se-main-container"}): #본문 내용 있으면
        text = soup.find("div", attrs={"class":"se-main-container"}).get_text()
        text = text.replace("\n", "")
        return text
    else:
        return "text 없음"

#메인 코드
contents = pd.DataFrame([[0,0,0,0]],columns=['주제','제목','링크', '내용'])

querys = ["여행", "음식", "운동", "공부", "예술", "음악", "독서", "영화", "드라마", "사진", "봉사활동", "공연", "기술", "게임", "요리", "환경", "패션", "자기계발", "건강", "취미", "여가활동", "맛집", "인터뷰", "연예인", "아이돌", "반려동물", "명상", "스포츠", "건축", "식물" ] #검색할 주제 #quote()로 16진수 ASCII 값으로 바꾼후 %붙임

for query in querys:
    url = "https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query="+quote(query) #querys로 안해서 결과가 이상했다

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"}
    res = requests.get(url,headers=headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")

    blogs = soup.find_all("li", attrs={'class':'bx'}) #class에 'bx' 들어가는 것
    #class가 <li class="bx">가 아닌 <li class="bx lineup">, <li class="bx term"> 들은 TypeError 발생


    for blog in blogs:
        try:
            blog_link = blog.find("a", attrs={'class':'title_link'})["href"]
            blog_name = blog.find("a", attrs={'class':'title_link'}).get_text()
            # print(blog_name, blog_link)

            blog_p = re.compile("blog.naver.com")
            blog_m = blog_p.search(blog_link)

            if blog_m:
                blog_text = scraping(delete_iframe(blog_link))
                content = {'주제': query, '제목': blog_name, '링크': blog_link, '내용': blog_text}
                contents = contents._append(content, ignore_index=True)

        except TypeError: #TypeError: 'NoneType' object is not subscriptable 인 경우 무시
            pass

# contents.to_csv("blog_crawling_new.csv", encoding="utf8")