import time


def contains(bag,e):
    return e in bag


def insert(bag,e):
    bag.append(e)


def remove(bag,e):
    bag.remove(e)


def count(bag):
    return len(bag)


#Bag 사용 예제
myBag = []
start=time.time()
insert(myBag,'휴대폰')
insert(myBag,"지갑")
insert(myBag,"테블릿")
insert(myBag,"교재")
insert(myBag,"필통")
insert(myBag,"충전기")
insert(myBag,"정신")

print("inMybag",myBag)

insert(myBag,"빗")
remove(myBag,"테블릿")

print("inMyBag",myBag)

def num0f(bag, e):
    count=0
    for item in bag:
        if item == e:
            count+=1
    return count

print("빗의 개수:", num0f(myBag, '빗'))

end=time.time()
print("실행시간=", end-start)