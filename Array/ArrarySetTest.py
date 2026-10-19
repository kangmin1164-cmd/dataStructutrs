from ArraySet import ArraySet

setA = ArraySet()
setA.insert('휴대폰')
setA.insert('지갑')
setA.insert('손수건')
print('Set A:', setA)

setB = ArraySet()
setB .insert('빗')
setB .insert('파이썬 자료구조')
setB .insert('야구공')
setB .insert('지갑')
print('Set B:', setB)

setB.insert('빗')
setA.delete('손수건')
setA.delete('발수건')
print('Set A:', setA)
print('Set B:', setB)

print('A U B:', setA.union(setB))
print('A ^ B:', setA.intersect(setB))
print('A - B:', setA.difference(setB))

'''
s1 = { 1,2,3 }
s2 = { 2,3,4,5 }
s3 = s1.union(s2)
s4 = s1.intersection(s2)
print("s1:", s1)
print("s2:", s2)
print("s3:", s3)
print("s4:", s4)
print("range(1,9):", range(1,9))
c1 = 1 + 2j
#c1 = complex(1,2)
c2 = complex(3,4)
c3 = c1 + c2
print("c1:",c1)
print("c2:",c2)
print("c3:",c3)
'''

print()
print("========== 도전 문제 ==========")


# ==================================================
# 도전 문제 1 : equals()
# ==================================================

A = ArraySet()

A.insert(3)
A.insert(5)
A.insert(1)


B = ArraySet()

B.insert(1)
B.insert(3)
B.insert(5)


C = ArraySet()

C.insert(1)
C.insert(3)


print()
print("[문제 1 : equals()]")

print("A =", A)
print("B =", B)
print("C =", C)

# A와 B는 원소의 순서는 다르지만
# {1, 3, 5}로 같은 집합이므로 True
print("A.equals(B) =", A.equals(B))

# C에는 5가 없기 때문에 False
print("A.equals(C) =", A.equals(C))


# ==================================================
# 도전 문제 2 : __eq__()
# ==================================================

print()
print("[문제 2 : == 연산자]")

# __eq__()를 구현했기 때문에
# A.equals(B)가 아니라 A == B 형태로 비교 가능

print("A == B :", A == B)
print("A == C :", A == C)


# ==================================================
# 도전 문제 3 : isSubsetOf()
# ==================================================

print()
print("[문제 3 : isSubsetOf()]")

# C = {1, 3}
# A = {3, 5, 1}
#
# C의 모든 원소가 A에 존재하므로
# C는 A의 부분집합
print("C.isSubsetOf(A) =", C.isSubsetOf(A))


# A에는 5가 있지만 C에는 5가 없기 때문에
# A는 C의 부분집합이 아님
print("A.isSubsetOf(C) =", A.isSubsetOf(C))


# 같은 집합 역시 자기 자신의 부분집합
print("A.isSubsetOf(B) =", A.isSubsetOf(B))