from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import os
import time 

path = os.getcwd() + "/6th assignment/chromedriver.exe"
driver = webdriver.Chrome(path)

try :
    driver.get("http://www.kyobobook.co.kr/index.laf?OV_REFFER=https://www.google.com/") #사이트에 접속
    time.sleep(1)

    searchIndex = "파이썬"                                      #검색어를 '파이썬'이라고 지정
    element = driver.find_element_by_class_name("main_input")   #검색창 class 이름은 main_input
    element.send_keys(searchIndex)                              #검색어를 검색창에 넣기 (send_keys:값을 넘겨줌)
    driver.find_element_by_class_name("btn_search").click()     #검색창 옆에 검색버튼 누르기

    html = driver.page_source
    bs = BeautifulSoup(html, "html.parser")

    pages = int(bs.find("span", id = "totalpage").text)
    print(pages)

    title=[]

    for i in range(2) :
        time.sleep(1)

        time.sleep(1) #페이지 1초 기다렸다가 페이지 로딩이 되면 

        html = driver.page_source               #html page source를 가지고 html 파일을 받아온 다음에 
        bs = BeautifulSoup(html, "html.parser") #beautifulsoup에 넣어서 찾기 쉬운 형태로 파싱 한 후 작업

        conts = bs.find("div", class_ = "list_search_result").find_all("td", class_ = "detail") #책 정보 전체:list_search_result, 책 정보 하나 전체 부분: detail

        title.append("page" + str(i + 1)) 
        for c in conts : #한 페이지에 나와있는 모든 제목을 for문을 통해 다 접근
            title.append(c.find("div", class_ = "title").find("strong").text)

        driver.find_element_by_xpath('//*[@id="contents_section"]/div[9]/div[1]/a[3]').click()


finally :
    #time.sleep(3)
    for t in title :
        if t.find("page") != -1 :
            print()
            print(t)
        else :
            print(t)
    driver.quit()

#mango mood
#ginger snap
#current appair
#smoothie move