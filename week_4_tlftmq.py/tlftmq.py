student_name="홍길동"
student_id=20260101
gpa=4.1

print("이름: ", student_name)
print("학번: ", student_id)
print("학점: ", gpa)


#성인, 미성년자 구분
name=input("당신의 이름을 입력하세요: ")
age=int(input("당신의 나이를 입력하세요: "))

if (age) >= 20:
    print("%s님은 성인입니다." %name)
else:
    print("%s님은 미성년자입니다." %name)


