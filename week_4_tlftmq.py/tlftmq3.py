#for문을 사용한 구구단 역순
dan=int(input("구구단 단 입력: "))
for i in range(9, 1, -1):
    print("%d*%d=" %(dan, i), dan*i)

#while문을 사용한 구구단
dan1=int(input("구구단 단 입력: "))
n=2
while n<10:
    print("%d*%d=" %(dan1, n), dan1*n)
    n+=1

#if else를 사용한 학점 계산기
score=int(input("점수 입력: "))
if score >= 90:
    print("학점: A")
elif score >=80:
    print("학점: B")
elif score >=70:
    print("학점: C")
else:
    print("학점: F")
