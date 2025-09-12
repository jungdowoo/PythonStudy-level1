# 튜플
# 파이썬 튜플
# 리스트와 비교 중요
# 튜플 자료형(순서0, 중복0, 수정x, 삭제x) # 수정, 삭제는 불변 (한번 선언해서 끝까지 사용)
# 리스트 자료형(순서o, 중복o, 삭제o, 수정o) 

# 선언

a = ()
b = (1,) # ,가 붙어야 int가아닌튜플
c = (11, 12, 13, 14)
d = (100, 1000, 'Ace', 'Base', 'Captine')
e = (100, 1000, ('Ace', 'Base', 'Captine'))

# 인덱싱
print('>>>>>>>')
print('d -', d[1])
print('d -', d[0] + d[1] + d[1]) # 튜플도 연산가능
print('d -', d[-1]) # -1인덱스는 맨 마지막 원소를 의미
print('d -', e[-1])

print('d - ', list(e[-1][1])) # 튜플을 리스트로 형변환시 불변이라는 특징이 없어지고 가변이됌


# 수정x테스트
#d[0] = 1500


# 슬라이싱
print('>>>>>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('d - ', e[2][1:3]) # e[2]는 다른튜플('Ace,base,captine을뜻함) 거기서 인덱스 1부터 2까지의요소 (3은제외)


# 튜플 연산
print('>>>>>>>>>>>>>')
print('c + d', c + d)
print('c * 3', c * 3)

# 튜플 함수
a = (5, 2, 3, 1, 4, 2)
print('a - ', a)
print('a - ', a.index(3)) # 값이 3인 원소의 인덱스 번호를 찾는것 즉 3은 0,1,2 2번의 인덱스에있기에 2출력
print('a - ', a.count(2)) # 값이 2인 원소가 몇개있냐

# 팩킹 & 언팩킹(Packing, and Unpacking)

# 팩킹
t = ('foo', 'bar', 'baz', 'qux') # 이 원소 4개를 패키지로묶은것 이게 팩킹

print(t)
print(t[0])
print(t[-1])

# 언팩킹1
(x1, x2, x3, x4) = t

print(type(x1), type(x2), type(x3), type(x4))
print(x1, x2, x3, x4)

# 팩킹 & 언팩킹
t2 = 1, 2, 3 # 괄호가 없어도 튜플
t3 = 4,
x1, x2, x3 = t2 # 언팩킹
x4, x5, x6 = 4, 5, 6

print(t2)
print(t3)
print(x1, x2, x3)
print(x4, x5, x6)