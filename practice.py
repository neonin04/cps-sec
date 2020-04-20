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
