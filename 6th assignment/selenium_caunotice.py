#cauNotice

from selenium import webdriver
from bs4 import BeautifulSoup
import os
import time

path = os.getcwd() + "/6th assignment/chromedriver" #selenium은 '크롬 드라이버'를 가지고 크롬을 실행시킨다.

driver = webdriver.Chrome(path)

#time.sleep(3)
#driver.quit()

try:
    driver.get("https://www.cau.ac.kr/cms/FR_CON/index.do?MENU_ID=100#page1")
    time.sleep(1)
    # driver.implicitly_wait(10) #로딩 최대 10초 동안 기다렸다가 실행

    html = driver.page_source   #requests.get().text (저번시간)
    bs = BeautifulSoup(html, "html.parser")

    #맨마지막 페이지수를 받아오는 작업. (나의 경우 248개)
    pages = bs.find("div", class_="pagination").find_all("a")[-1]["href"].split("page")[1]
    # find_all은 list형태로 리턴을 해준다.
    # [-1]: 마지막 list                     <a class="btn_end" href="#page248" title="마지막 페이지로 이동"><span>End</span></a>
    # ["href"]: attribute에 접근            #page248
    # .split("page"): page를 기준으로 나눔  ['#', '248']
    # [1]: 리스트의 두번째 인덱스로 접근
    pages = int(pages) #248을 숫자로 받기
    
    title = []
    for i in range(3) :
        driver.get("https://www.cau.ac.kr/cms/FR_CON/index.do?MENU_ID=100#page" + str(i+1))
        time.sleep(3)

        html = driver.page_source
        bs = BeautifulSoup(html, "html.parser")

        conts = bs.find_all("div", class_ = "txtL") #CAU Notice에 있는 제목들의 class 이름이 txtL이다
        title.append("page" + str(i + 1)) # 

        for c in conts :
            title.append(c.find("a").text)

finally:
    # time.sleep(3)
    for t in title :
        if t.find("page") != -1: #페이지가 없지(-1) 않은(!=) 경우에만 출력 실행
            print() #한칸씩 띄워줘서 보기좋게 만듬
            print(t)
        else:
            print(t) #페이지가 없는 경우는 값들을 출력해준다
    driver.quit()