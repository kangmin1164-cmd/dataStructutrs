class Book:
    def __init__(self, title, author):
        self.title=title
        self.author=author

b1=Book("자료구조", "홍길동")

print("제목:", b1.title)
print("저자:", b1.author)

class Student:
    def __init__(self, name, scores):
        self.name=name
        self.scores=scores

    def get_average(self):
        return sum(self.scores)/len(self.scores)

student1=Student("김철수", [85, 90, 95])
print("%s 학생의 평균 성적: %.2f점" %(student1.name, student1.get_average()))

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner=owner
        self.balance=balance

    def deposit(self, amount):
        self.balance += amount
        print("%d원 입금 완료. 현재 잔액 %d원" %(amount, self.balance))

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("%d원 출금 완료 현재 잔액: %d원" %(amount, self.balance))

        else:
            print("잔액이 부족합니다.")

acc=BankAccount("김철수", 10000)

acc.deposit(5000)
acc.withdraw(8000)
acc.withdraw(10000)