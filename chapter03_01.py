# 파이썬 기초 자료형
# 숫자형

# 파이썬 지원 모든 자료형
"""
int : 정수
float : 실수
complex : 복소수
bool : 불린 True or False
str : 문자열(시퀀스)
list : 리스트(시퀀스)
tuple : 튜플(시퀀스)
set : 집합
dict : 사전타입
"""

# 데이터 타입
str1 = "Python" 
bool = True
str2 = 'Anaconda'
float_v = 10.0 # 10 == 10.0 은 컴퓨터에서는 다르다. 10.0은 엄연히 실수
int_v = 7
list = [str1, str2]
dict = {
    "name": "Machine Learning", #name은 키 Machine Learning은 키 값
    "version": 2.0
}
tuple = (7, 8, 9)
set = {3, 5, 7}


# 데이터 타입 출력
print(type(str1))
print(type(bool))
print(type(str2))
print(type(float_v))
print(type(int_v))
print(type(dict))
print(type(tuple))
print(type(set))

# 숫자형 연산자
"""
+
-
*
/
// : 나눈 다음의 몫
% : 나머지
abs(x) : 절대값
pow(x, y) x ** y -> 2 ** 3  제곱값
"""

# 정수 선언
i = 77
i2 = -14
big_int = 7777777777777777777777777777777

# 정수 출력
print(i)
print(i2)
print(big_int)

# 실수 출력
f = 0.9999
f2 = 3.141592
f3 = -3.9
f4 = 3 / 9

print(f)
print(f2)
print(f3)
print(f4)
print()

# 연산 실습
i1 = 39
i2 = 939
big_int1 = 77777777777777777777777791923912939
big_int2 = 34343424124123123123123123123123123
f1 = 1.234
f2 = 3.939


# +
print(" >>>>>> +")
print("i1 + i2 : ", i1 + i2)
print("f1 + f2:", f1 + f2)
print("big_int1 + big_int2 :", big_int1 + big_int2)

# *

print(" >>>>>> * ")
print("i1 * i2 : ", i1 * i2)
print("f1 * f2:", f1 * f2)
print("big_int1 + big_int2 :", big_int1 * big_int2)


# 형 변환 실습 (0은 생략가능)
a = 3.
b = 6
c = .7
d = 12.7

# 타입 출력
print(type(a), type(b), type(c), type(d))

# 형 변환
print(float(b))
print(int(c))
print(int(d))
print(int(True)) # True:1 , False: 0을 의미 즉 참은 1 거짓은 0
print(float(False)) # 0.0
print(complex(3))
print(complex('3')) # 문자형 -> 숫자형
print(complex(False))
print()

# 수치 연산 함수
print(abs(-7))  #abs는 절대값 출력
x,y = divmod(100,8) # x는 몫 y는 나머지
print(x,y)
print(pow(5,3), 5 ** 3)

# 외부 모듈
import math


print(math.ceil(5.1)) # x 이상의 수 중에서 가장 작은 정수를 찾아줌
print(math.pi)




