# Chapter04-2
# 파이썬 반복문
# For 실습
# 코딩의 핵심
# for in <collection>
# <Loop body>

for v1 in range(10): # 0~9 까지 반복 
    print('v1 is :', v1)

for v2 in range(1, 11): # 1~10까지
    print('v2 is :', v2)

for v3 in range(1, 11, 2): # 1~10까지 2개씩 건너뛰어서 출력
    print('v3 is :', v3)


# 1~ 1000 까지의 합
sum1 = 0

for v in range(1, 1001):
    sum1 += v
print('1~1000 Sum:', sum1)

print()
# Iterables 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전(딕셔너리) 전부 for문 사용가능
# iterable 리턴 함수: range, reversed, enumerate, filter, map, zip

# 예제1
names = ['Kim', 'Park', 'Cho', 'Lee', 'Choi', 'Yoo']

for name in names:
    print('You are :', name)

# 예제2
lotto_numbers = [11, 19, 21, 28, 36, 37]

for n in lotto_numbers:
    print("Current number:", n)

# 예제3
word = "Beautiful"

for s in word:
    print('word :', s)

# 예제4
my_info ={
    "name":'Lee',
    "Age":33,
    "City":"Seoul"
}

# key가져오기
for key in my_info:
    print('key:', key)

# value가져오기
for v in  my_info.values():
    print('value :', v)


#예제5
# 만약 n이 대문자라면 그대로 출력하고 아니라면 대문자로 바꿔서 출력해줘
name = 'FineAppLE'


for n in name:
    if n.isupper():
        print(n)
    else:
        print(n.upper())

# break문(for문 탈출)

numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

# 34를 찾으면 그 뒤에 것이 실행되지않음
for num in numbers:
    if num == 34:
        print('Found:34!')
        break
    else:
        print('Not found :', num)

print()

# countinue문
# 어떠한 조건안에서 countinue문을 만나면 다시 조건을 검색한다.
# 여기서 boolean형은 출력하고 싶지않아 라면
lt =["1", 2, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is bool:
        continue
    print("current type: ", type(v))
    print("multiply by 2", v * 3)
    print(True * 3) # True는 1이기에 곱해도 3이 나옴


# for - else

numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]
for num in numbers:
    if num == 24:
        print("Found: 24")
        break
else:
    print('Not Found : 49')


# 구구단 출력

for i in range(1, 10):
    for j in range(1, 10):
        print('{:4d}'.format(i*j), end='')
        print()

# 변환 예제
name2 = 'Aceman'

print('Reversed', reversed(name2))
print('List', list(reversed(name2)))
print('Tuple', tuple(reversed(name2)))
print('Set', set(reversed(name2))) # 집합은 순서가X 실행할때마다 위치가 랜덤