# 집합(Set) 특징
# 집합(Set)  자료형(순서x, 중복X)

# 선언
a = set() # 빈집합
b = set([1, 2, 3, 4]) # 리스트
c = set([1, 4, 5, 6])
d = set([1, 2, 'Pen', 'Cap', 'Plate'])
e = {'foo', 'bar', 'baz', 'foo', 'qux'} # 키가 없이 원소만 나열한다면 이것도 집합(set)임. 딕셔너리가아님
f = {42, 'foo', (1, 2, 3), 3.1411579}

print('a - ', type(a), a, 2 in b)
print('a - ', type(b), b)
print('a - ', type(c), c)
print('a - ', type(d), d)
print('a - ', type(e), e)
print('a - ', type(f), f)

# 튜플 변환 (set -> tuple)
t = tuple(b)
print('t - ', type(t), t)
print('t - ', t[0], t[1:3])


# 리스트 변환(set -> list)
l = list(c)
l2 = list(e)

print('l -', l)
print('l2 -', l2)

# 길이(len)
print(len(a))
print(len(b))
print(len(c))
print(len(d))
print(len(e))
print(len(f))

# 집합 자료형 활용
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

#교집합
print('s1 & s2 :', s1 & s2) # s1 과 s2 의 교집합만 보여줌
print('s1 & s2 :', s1.intersection(s2)) #intersection 함수로도 가능

#합집합
print('s1 | s2 :', s1 | s2)
print('s1 | s2 :', s1.union(s2))

#차집합 
print('s1 - s2:', s1 - s2)
print('s1 - s2 :', s1.difference(s2))

# 중복 원소 확인 True,False 로
print('s1 & s2 : ', s1.isdisjoint(s2)) # False가 나와야 있다는것. 헷갈리지 말것

# 부분 집합 확인
print('subset : ', s1.issubset(s2))
print('superset :', s1.issuperset(s2))  

# 추가 & 제거
s1 = set([1, 2, 3, 4])
s1.add(5)
print('s1 - ', s1)

# 제거
s1.remove(2)
print('s1 - ', s1)

# discard는 예외를 발생시키지않는다. 
s1.discard(3)
print('s1 - ', s1) 

# 모두삭제
s1.clear()




