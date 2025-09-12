# 파이썬 딕셔너리(사전)
# 범용적으로 가장 많이 사용 
# 딕셔너리 자료형(순서X, 키 중복X, 수정o, 삭제o)

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


