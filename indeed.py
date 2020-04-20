import requests
import csv
from bs4 import BeautifulSoup

class Scraper() :
    def __init__(self) :
        self.url = "https://kr.indeed.com/jobs?q=python&limit=50"

    def getHTML(self, cnt):
        #1. website 연결
        res = requests.get(self.url + "&start=" + str(cnt * 50)) #string이랑 int형은 더할 수 없다 -> str 사용해서 int를 string으로 형변환 해준다.
        if res.status_code != 200 :
            print("request error : ", res.status_code)

        html = res.text #2. website에서 html 받아오기 (개발자도구에 나오는 것들)

        #3. 
        soup = BeautifulSoup(html, "html.parser") #parser의 역할은 html을 쪼개서 BeautifulSoup에서 쓰기 좋은 형태로 바꿔주기

        return soup

    def getPages(self, soup) :
        pages = soup.select(".pagination > a") #pagination은 페이지수를 담고 있다
                                       #'.'은 class명을 명시한다 -> pagination을 찾는다는 뜻
                                       #각각의 페이지수는 <a (a 태그)들로 구성이 되어있다
                                       #결론: pagination의 a태그들을 선택해서 가져온다
        return len(pages)

    def getCards(self, soup, cnt) :
        jobCards = soup.find_all("div", class_ = "jobsearch-SerpJobCard")
        #잡카드 가져오기
        #모든 카드가 jobsearch-SerpJobCard로 되어있다.
        #div라는 태그에, class가 jobsearch-SerpJobCard인 것을 모두 찾는다.

        jobID = []
        jobTitle = []
        jobLocation = []
        #개수가 많기 때문에 배열로 선언해준다.
        #data-jk라는 id값을 받아온다. 
        #id값을 받아오는 이유는 제목을 보고 링크로 들어가면 상세보기를 볼 수 있기 위해서

        for j in jobCards : #모든 jobCards에 접근
            jobID.append("https://kr.indeed.com/viewjob?jk=" + j["data-jk"])
            jobTitle.append(j.find("a").text.replace("\n", ""))
            if j.find("div", class_ = "location") != None :
                jobLocation.append(j.find("div", class_ = "location").text)
            elif j.find("span", class_ = "location") != None :
                jobLocation.append(j.find("span", class_ = "location").text)
            jobID.append("https://kr.indeed.com/viewjob?jk=" + j["data-jk"])
        #append 사용하는 이유는, 위에 빈 배열로 선언을 해주었기 때문에 값에 접근이 불가능하다. 그래서 배열의 가장 마지막에 추가를 해준다.
        #a 태그에 text를 받아온다. replace: \n를 '빈칸'으로 대체한다. (\n를 없애는 것)
        #location을 받아올때 터미널 창에 'NoneType' 뜬다 -> location을 받아올 수 없는 것도 있어서 못가져 온다.
        #그래서 if문을 사용해서 NoneType이 아니면 location 가져오라고 함
        #태그가 div와 span 두 종류라 둘 다 받아온다.
        #id 받아올 때는 div태그 안에 data-jk라는 attribute안의 값.

        self.writeCSV(jobID, jobTitle, jobLocation, cnt)

    def writeCSV(self, ID, Title, Location, cnt) : #argument 이름이 달라도 됨
        file = open("indeed.cvs", "a", newline="")

        wr = csv.writer(file)
        for i in range(len(ID)) : #셋 다 개수가 같으니 셋 중 아무거나 골라서 써도 됨. ID의 배열 개수만큼 돌아간다.
            wr.writerow([str(i + 1 + (cnt*50)), ID[i], Title[i], Location[i]]) #id, title, location 개수만큼 줄이 생긴다, i가 돌아간다.
            #13번 돌 때, i의 값이 증가한다.

        file.close

    def scrap(self) :
        soupPage = self.getHTML(0) #첫페이지니까 0
        pages = self.getPages(soupPage)

        file = open("indeed.csv", "w", newline="") #write 옵션 넣어주는 이유는, scrap 함수가 호출이 된다는 것은 이 파이썬파일을 한번 다 돌린다는 뜻. 
                                                   #근데 돌릴 때마다 a태크면 indeed.csv라는 파일에 계속 추가만 될것이다. 그래서 이건 초기화를 해주는 방법.
        wr = csv.writer(file)
        wr.writerow(["No.", "Link", "Title", "Location"])
        file.close

        for i in range(pages) :
            soupCard = self.getHTML(i) #계속 값이 변하니까 i
            self.getCards(soupCard, i)
            print(i+1, "번째 페이지 Done")

if __name__ == "__main__" :
    s = Scraper()
    s.scrap()



