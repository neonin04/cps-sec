import requests
from bs4 import BeautifulSoup

req = requests.get("https://movie.naver.com/movie/running/current.nhn")
if req.status_code != 200 :
    print("failed", req.status_code)

html = req.text

bs = BeautifulSoup(html, "html.parser")

box = bs.find_all("dl", class_ = "lst_dsc")

title = []
ratio = []
reserve = []
for b in box :
    title.append(b.find("dt", class_ = "tit").find("a").text) #제목
    ratio.append(b.find("div", class_ = "star_t1").find("span", class_ = "num").text) #평점
    if b.find("div", class_ = "star_t1 b_star") != None :
        reserve.append(b.find("div", class_ = "star_t1 b_star").find("span", class_ = "num").text) #예매율
    else:
        reserve.append("0")

movieInfo = []
for i in range(len(box)) :
    movie = []
    #movie.append(title[i])
    #movie.append(ratio[i])
    #movie.append(reserve[i])
    #movieInfo.append(movie)
    movieInfo.append([title[i],ratio[i],reserve[i]]) #위에 4줄이 이 한줄이랑 같다
    
for i in movieInfo :
    print(i)





