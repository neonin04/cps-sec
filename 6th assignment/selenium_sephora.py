from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import os
import time

path = os.getcwd() + "/6th assignment/chromedriver.exe"
driver = webdriver.Chrome(path)

try :
    driver.get("https://www.sephora.kr/pages/just-for-you-online?EKAMS=google.985.6765.21832.2039371.600585018&trackingDays=30&utm_source=google&utm_medium=cpc&utm_term=%EC%84%B8%ED%8F%AC%EB%9D%BC&utm_campaign=SA_KR_PC_SEPHORA&utm_content=SEPHORA_PureBrand&gclid=Cj0KCQjwhZr1BRCLARIsALjRVQOpmB2iiP884cLxHlGnQkL76bIMXG09UIsJi6m85Sawj3gik7q52KkaAlIFEALw_wcB") #사이트에 접속
    time.sleep(1)

    searchIndex = "파운데이션"                                         #검색어를 '틴트'라고 지정
    element = driver.find_element_by_class_name("search-input")  #검색창 class 이름은 search-input
    element.send_keys(searchIndex)                               #검색어를 검색창에 넣기 (send_keys:값을 넘겨줌)
    element.send_keys(Keys.RETURN)     #검색창 옆에 검색버튼 누르기
    #driver.find_element_by_class_name("ns-search::before")

    html = driver.page_source               #html page source를 가지고 html 파일을 받아온 다음에
    bs = BeautifulSoup(html, "html.parser") #beautifulsoup에 넣어서 찾기 쉬운 형태로 파싱 한 후 작업

    title = []
    for i in range(5) :
        html = driver.page_source
        bs = BeautifulSoup(html, "html.parser")

        conts = bs.find("div", class_ = "products-grid").find_all("div", class_ = "product-card")
                                        #아이템 전체 포함 박스                      #아이템 하나 박스
        title.append("page" + str(i + 1)) #제품리스트 앞에 page1, page2 나오는 부분
        for c in conts :
            title.append(c.find("a", class_ = "product-card-description").find("p", class_ = "product-card-product").text) #제품이름

        driver.find_element_by_class_name("page next").click()
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