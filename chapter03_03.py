# 파이썬 기초 자료형
# 리스트 List
# 자료구조에서 중요
# 데이터 컨테이너 
# 리스트 자료형(순서o, 중복o, 삭제o, 수정o)


# 선언
a = [] # 빈괄호는 리스트
b = list()
c = [70, 75, 80, 85] #len
d = [1000, 10000, 'Ace', 'Base', 'Captine'] # 서로 다른 자료형을 한 리스트에 담을 수 있다.
e = [1000, 10000, ['Ace', 'Base', 'Captine']]
f = [21.42, 'foobar', 3, 4, False, 3.14159]
# 인덱싱 = 내가원하는 데이터를 꺼내오는 과정
print('>>>>')
print('d -', type(d), d)
print('d -', d[1])
print('d -', d[0] + d[1] + d[1])
print('d -', d[-1])
print('e -', type(e[-1][1]))
print('e -', list(e[-1][1])) # 리스트로 형변환

# 슬라이싱
print('>>>>>')
print('d -', d[0:3])
print('d -', d[2:]) 
print('e - ', e[-1][1:3])


# 리스트 연산
print('>>>>')
print('c + d', c + d)
print('c * 3', c * 3)
print("Test + c[0]", 'Test' + str(c[0]))

# 값 비교
print(c == c[:3] + c[3:])
print(c)
print(c[:3] + c[3:])
print()


# Identity(id)
temp = c
print(temp, c)
print(id(temp))
print(id(c))

# 리스트 수정, 삭제
print('>>>>>>>')
c[0] = 4
print('c - ', c)
c[1:2] = ['a','b','c'] 
print('c - ', c)

c[1] = ['a', 'b', 'c']
print('c -', c)

c[1:3] = []
print('c - ', c)

del c[2] # 삭제 2번째를 삭제
print('c -', c)
print()

# 리스트 함수
a = [5, 2, 3, 1, 4]

print('a -', a)
a.append(10) # 끝부분에다가 데이터를 삽입할때 쓰는 함수
print('a - ', a)
a.sort() #오름차순으로 정렬함
print('a - ', a)
a.reverse() # 반대로 출력 
print('a -', a)
print('a -', a.index(3), a[3]) #index번호로 가져올수 있는 함수
a.insert(2, 7) # 2번째위치에 7이라는 값을 넣을거야
print('a - ', a)
#del a[6]
a.remove(10)
print('a - ', a)
print('a -', a.pop()) # 끝에있는요소를 가져온다
print('a - ', a)
print('a - ', a.count(4)) # 내가원하는값이 몇개가 중복되어있는지 찾을때 count

ex = [8,9]
a.extend(ex) # 뒤에 extend로 붙임
print('a - ', a)

# 삭제 :remove(내가원하는값을 바로삭제), pop(끝에있는것만삭제), del (내가원하는 인덱스번호를 알아야 삭제)
# 반복문 활용
while a:
    data = a.pop()
    print(data) # pop이기에 끝에있는것을 반복으로 삭제