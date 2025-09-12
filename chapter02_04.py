# 파이썬 변수


# 기본선언

n = 700 

print(n * 700)

# 출력
print(n)
print(type(n)) # n이라는 변수에 자료형을 출력해준다 type

# 동시 선언
x = y = z = 700 # xyz에 다 700
print(x,y,z)
print()

# 선언
var = 75
# 재선언
var = "Change Value"

# 출력
print(var)
print(type(var))

# Object References
# 변수 값 할당 상태
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔 출력

# 예1)
print(300)
print(int(300))

# 예2)
# n -> 777
n = 777

print(n, type(n))
print()

m = n
# m -> 777 <- n

print(m, n)
print(type(m), type(n))
print()

m = 400
print(m, n)
print(type(m), type(n))
print()

# id(idenfity)확인:  객체의 고유값 확인

m = 800
n = 655
# 800,655가 아닌 객체의 고유값이 출력됌
print(id(m))
print(id(n))
print(id(m) == id(n)) # false가 나옴 고유값이 다르기에
print()

# 이건 True가 나옴 파이썬 입장에서는 보기에는 우리가 변수 4개를 선언했지만 효율성을 내부적으로 인터프리터가 굳이 이렇게 변수를 복사해서 선언할 필요는없잖아라고 판단
# 하나의 오브젝트로 생성해버림.
# 같은 오브젝트 참조
m = 800
n = 800
z = 800
i = 800
print(id(m))
print(id(n))
print(id(m) == id(n)) 
print()

# 다양한 변수 선언 
# Camel Case : numberOfCollegeGraduates (첫글자 소문자 -> 보통 Method를 선언할때)
# Pascal Case : NumberOfColleageGraduates (첫글자 대문자 -> 보통 Class 생성할때)
# Snake Case : number_of_colleage_graduates (파이썬에서 변수를 선언할때 보통 자주 사용)

# 허용하는 변수 선언 법 (_은 허용)
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 8
# 특수문자나 숫자로 시작하는 변수는 X


# 예약어는 변수명으로 불가능 예)for = 3 , as = 3, class = 3 

