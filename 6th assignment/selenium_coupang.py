from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import os
import time

path = os.getcwd() + "/6th assignment/chromedriver.exe"
driver = webdriver.Chrome(path)

#쿠팡에서 '마스크' 검색

try :
    driver.get("https://www.coupang.com/") #사이트에 접속
    time.sleep(1)

    searchIndex = "마스크"                                       #검색어를 '마스크'라고 지정
    element = driver.find_element_by_id("headerSearchKeyword")   #검색창 id (여러 사이트를 해본 결과, 검색창 안에 임의로 글자가 써져있는 경우, 대부분 class가 아니라 id로 해야하는 것 같다.)
    element.send_keys(searchIndex)                               #검색어를 검색창에 넣기 (send_keys:값을 넘겨줌)
    element.send_keys(Keys.RETURN)                               #엔터를 누르라는 명령어
                                                                 #검색창 옆에 검색버튼 누르기 driver.find_element_by_class_name("ns-search")

    html = driver.page_source               #html page source를 가지고 html 파일을 받아온 다음에
    bs = BeautifulSoup(html, "html.parser") #beautifulsoup에 넣어서 찾기 쉬운 형태로 파싱 한 후 작업

    title = []
    for i in range(3) :
        html = driver.page_source
        bs = BeautifulSoup(html, "html.parser")

        conts = bs.find("ul", class_ = "search-product-list").find_all("li", class_ = "search-product")
                                        #아이템 전체 포함 박스                          #아이템 하나 박스
        title.append("page" + str(i + 1)) #제품리스트 앞에 page1, page2, ... 나오는 부분
        for c in conts :
            title.append(c.find("div", class_ = "descriptions-inner").find("div", class_ = "name").text) #제품 이름

        driver.find_element_by_class_name("btn-next").click() #다음 버튼 누르기
        #driver.find_element_by_xpath('//*[@id="product-index-content"]/div[2]/div[4]/nav/a[3]').click()

finally :
    time.sleep(3)
    for t in title :
        if t.find("page") != -1 :
            print()
            print(t)
        else :
            print(t)
    driver.quit()