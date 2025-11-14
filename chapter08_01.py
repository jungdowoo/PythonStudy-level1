# 파이썬 내장(Built-in) 함수
# 자주 사용하는 함수 위주로 실습
# str(), int(), tuple() 형변환은 이미 학습



# 절대값 구하는 함수
# abs()

print(abs(-3)) # 절대값인 3 출력


# all, any :iterable 요소 검사(참, 거짓)
print(all([1, 2, ''])) # all이라는건 요소가 전부 True인지 판별 하나라도 False면 false반환 # and
print(any([1, 2, 0]))  #any는 요소중에 하나라도 True가 있으면 True반환 # or

# chr : 아스키 ->문자, ord : 문자 -> 아스키코드로 돌려주는 함수

print(chr(44))
print(ord('C'))

# enumerate : 인덱스 + Iterable 객체 생성
for i, name in enumerate(['abc', 'bcd', 'efg']):
    print(i+1, name)

# filter : 반복가능한 객체 요소를 지정한 함수 조건에 맞는 값 추출

def conv_pos(x):
    return abs(x) > 2

print(list(filter(conv_pos, [1, -3, 2, 0, -5, 6])))
print(list(filter(lambda x: abs(x) > 2, [1, -3, 2, 0, -5, 6]))) #람다식으로하면 함수를 선언하지않아도됌

# id : 객체의 주소값(레퍼런스) 반환

print(id(int(5)))
print(id(4))

# Len : 요소의 길이 반환
print(len('abcdefg') -1) # 길이에서 1빼줌
print(len([1,2,3,4,5,6,7]))

# max, min : 최대값, 최소값

print(max([1,2,3]))
print(max('python study'))
print(min([1,2,3]))
print(min('python study'))

# map : 반복가능한 객체 요소를 지정한 함수 실행 후 추출
def conv_abs(x):
    return abs(x)

print(list(map(conv_abs,[1,-3,2,0,-5,6])))
print(list(map(lambda x:abs(x), [1,-3,2,0,-5,6]))) # 람다식



# pow : 제곱값 반환
print(pow(2,10)) # 2의 10승 = 1024

# range : 반복가능한 객체(Iterable) 반환
print(range(1,10,2))
print(list(range(1,10,2)))
print(list(range(0,-15,-1)))

# round : 반올림
print(round(6.5781, 2)) # 2번째 인자를 넣지않으면 그냥둘째자리에서 반올림을 해버림
print(round(5.6))


# sorted : 반복가능한 객체(Iterable) 정렬 후 반환

print(sorted([6,7,4,3,1,2]))
a = sorted([6,7,4,3,1,2])
print(a)
print(sorted(['p','y','t','h','o','n']))

# sum : 반복가능한 객체(Iterable) 합 반환
print(sum([6,7,8,9,10])) # 다 더함
print(sum(range(1,101))) # 1부터 100까지의 합을 구해줌


# type : 자료형 확인
print(type(3)) # int
print(type({3,4})) #set
print(type(())) #tuple
print(type([])) #list

# zip : 반복가능한 객체(Iterable)의 요소를 묶어서 반환

print(list(zip([10, 20, 30], [40, 50, 60])))
print(type(list(zip([10, 20, 30], [40, 50, 777]))) [0])

