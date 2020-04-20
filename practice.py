#함수와 클래스
#4/20 tuto

def arry2D() :
    a=[]
    for i in range(5) :
        b=[] #안에 선언해줌, 
        for j in range(3) :
            b.append(j)
        a.append(b)
    print(a)

for i in range(20) :
    arry2D()




airline = []
time = []
cost = []

for b in box :
    airline.append(b.find("div", class_ = "info_air").find("span", class_ = "txt_airline").text)
    time.append(b.find("dl", class_ = "list_time").find("dd", class_ = "time_required").text)
    cost.append(b.find("div", class_ = "info_price").find("span", class_ = "txt_price").text)
    print(airline)