import requests
import csv
from bs4 import BeautifulSoup

def PageScrap(req):
    if req.status_code != 200 :
        print("failed", req.status_code)
    html = req.text
    bs = BeautifulSoup(html, "html.parser")

    box = bs.find_all("td", class_ = "goodsTxtInfo")

    title = []
    author = []
    review = []

    for b in box :
        title.append(b.find("p").find("a").text)
        author.append(b.find("div", class_ = "aupu").find("a").text)
        review.append(b.find("p", class_ = "review").find("a").text)

    file = open("daumtravel.csv", "a", newline="")
    wr = csv.writer(file)
    wr.writerow(["Title", "Author", "Review"])

    for i in range(len(box)) :
        wr.writerow([title[i],author[i],review[i]])

    file.close()


for i in range(10):
    res = requests.get("http://www.yes24.com/24/category/bestseller?CategoryNumber=001&sumgb=03&PageNumber=" + str(i+1))
    PageScrap(res)
