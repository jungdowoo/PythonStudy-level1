# 파이썬 딕셔너리(사전)
# 범용적으로 가장 많이 사용 
# 딕셔너리 자료형(순서O, 키 중복X, 수정o, 삭제o)

# 선언 방법 {}
a = {'name': 'Kim', 'phone': '0101010101010', 'birth':'970812'} # 키 : 값(밸류) 키 중복이 X 라 name이라는 키에 두개가있으면 중복허용 x
b = {0: 'Hello Python'}
c = {'arr': [1, 2, 3, 4]} # 값에 리스트가들어와도 OK
d = {
    'Name': 'NiceMan',
    'City': 'Seoul',
    'Age' : 33,
    'Grade': 'A',
    'Status': True
}
# dict안에 리스트로 선언하는 방법
e = dict([
    ('Name', 'Niceman'),
    ('City', 'Seoul'),
    ('Age',33),
])

# f방식으로 선언
f = dict(
    Name = 'Niceman',
    City = 'Seoul',
    Age = 33,
    Grade = 'A',
    Status = True
)


print('a - ', type(a), a)
print('a - ', type(b), b)
print('a - ', type(c), c)
print('a - ', type(d), d)
print('a - ', type(e), e)
print('a - ', type(f), f)
print()
# 원하는 키로 출력

print('a - ', a['name']) # a의Name이라는 키에담긴 값을 출력() 이 방식은 키가 존재하지않을시 -> 에러발생
print('a -', a.get('name1')) # get으로 접근했을때 키가없을땐 None이라고 출력이 됨 그래서 get이 안전해서 자주사용 
print('b -', b[0])
print('b -', b.get(0))


# 딕셔너리 추가
a['address'] = 'seoul'
print('a -', a)
a['rank'] = [1,2,3]
print('a -', a)

# 딕셔너리 길이
print('a - ', len(a)) # len은 키의길이 확인하는 함수

# dict_keys, dict_values, dict_items : 반복문에서 사용 가능

print('a -', a.keys())  # 밸류값은 신경쓰지않고 키값들만 출력함
print('b -', b.keys())
print('c -', c.keys())
print('d -', d.keys())
print('e -', e.keys())

print('a -', list(a.keys())) # keys 함수를 불러오고 list형변환으로 하면 키 값들을 리스트로 가져옴
print('b -', list(b.keys())) 

print()

print('a -', a.values()) # 밸류(값)만 가져옴
print('b -', b.values())
print('c -', c.values())

print()

#키와 밸류를 동시에 가져오는 메소드 items
print('a -', a.items())
print('b -', b.items())
print('c -', c.items())

print('a -', list(a.items()))
print('b -', list(b.items()))

print()

print('a -', a.pop('name'))
print('a - ', a)

print('c -', c.pop('arr'))
print('c - ', c)

print()

print('f -', f.popitem()) #아무거나 임의로 하나 꺼내옴 # pop이 들어가면 무조건 원본데이터는 삭제
print('f -', f) # 출력해보면 가져온값은 출력되지않음

print()

# in메소드

print('a -', 'birth' in a) # birth라는 키가 a에 있어? 있으면 True반환 없으면 False반환
print('a -', 'birth2' in a) # birth2라는 키는 없기에 False반환
print('a -', 'City' in d) # 대소문자를 가리기에  city는 False반환 City는 True반환


# 수정 & 추가
a['test'] = 'test_dict'
print('a-', a)

a['address'] = 'dj'
print('a -', a)

a.update(birth='910904')
print('a -', a)
temp = {'address': 'Busan'}

# 수정
a.update(temp)
print('a -', a) 
