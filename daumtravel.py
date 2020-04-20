import requests
import csv
from bs4 import BeautifulSoup

req = requests.get("http://www.yes24.com/24/category/bestseller?CategoryNumber=001&sumgb=03")
if req.status_code != 200 :
    print("failed", req.status_code)

html = req.text

bs = BeautifulSoup(html, "html.parser")

#pages = bs.select(".page > a")
#print(len(pages))

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



