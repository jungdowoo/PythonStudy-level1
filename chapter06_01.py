# 파이썬 클래스
# OOP(객체 지향 프로그래밍), self, 인스턴스 메소드, 인스턴스 변수
# 클래스 and 인스턴스 차이 이해
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 접근 가능, 공유
# 인스턴스 변수 : 객체마다 별도 존재
# 메소드란?: 객체가 가지고 있는 기능(동작)을 정의한 것 즉, 클래스 안에 정의된 함수

#객체란? Class로부터 만들어진 실제 데이터 덩어리
# 클래스 = 붕어빵 틀 , 인스턴스 = 틀을 가지고 찍어내는 객체
# 인스턴스와 객체의 차이점 = 인스턴스는 객체가 실제로 메모리에 생성된 상태


# 예제1
class Dog(object):  #object를 상속받음
    # 클래스 속성
    species = 'firstdog'

    # 초기화/인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 클래스 정보 출력
print(Dog)

# 인스턴스화
a = Dog("mikky", 2) # name과 age 
b = Dog("baby", 3)
c = Dog("baby", 3)

# 비교
# a와 c는 같아보이지만 파이썬은 전혀다른객체로 본다
print(a == b, id(a), id(b), id(c))

# 네임스페이스
print('dog1', a.__dict__)
print('dog1', b.__dict__)

# 인스턴스 속성 확인

print('{} is {} and {} is {}'.format(a.name, a.age, b.name, b.age))


if a.species == 'firstdog':
    print('{0} is a {1}'.format(a.name, a.species))

print(Dog.species)
print(a.species)


# 예제2
# self의 이해
class SelfTest():
    def func1():
        print('Func1 called')
    def func2(self):
        print(id(self))
        print('Func2 called')

f = SelfTest()

#print(dir(f))
print(id(f))
# f.func1() # 예외
f.func2() # self는 호출됨

SelfTest.func1()
SelfTest.func2(f)

print('-------------')

# 예제3
# 클래스 변수, 인스턴스 변수
class Warehouse:
    # 클래스 변수 = 0
    stock_num = 0 # 재고

    def __init__(self, name):
        # 인스턴스 변수
        self.name = name
        Warehouse.stock_num += 1

    def __del__(self):
        Warehouse.stock_num -= 1

user1 = Warehouse('Lee')
user2 = Warehouse('Cho')

print(Warehouse.stock_num)
Warehouse.stock_num = 50
print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print('before',Warehouse.__dict__)
print('>>>', user1.stock_num)


del user1
print('after',Warehouse.__dict__)

# 예제4
class Dog(object):  #object를 상속받음
    # 클래스 속성
    species = 'firstdog'

    # 초기화/인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def info(self):
        return '{} is {} years old'.format(self.name, self.age)
    
    def speak(self, sound):
        return "{} says {}!".format(self.name, sound)
    

# 인스턴스 생성

c = Dog('july', 4)
d = Dog('Merry', 10)
#메소드 호출
print(c.info())
print(d.info())
#메소드 호출
print(c.speak('Wal Wal'))
print(d.speak('Mung Mung'))