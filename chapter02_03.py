# chapter02_2
# 파이썬 완전 기초
# 파이썬 변수

# 기본 선언
n = 700

print(n * 700)

# 출력
print(n)
print(type(n)) # n의 type을 출력함

# 동시 선언
x = y  = z = 700
print(x,y,z)

# 선언
var = 75

# 재선언
var = "Change Value"

# 출력
print(var)
print(type(var)) # var 75는 바뀌고 change value 가 나오며 type은 str로 나온다.

# Object Refernces 
# 변수 값 할당 상태일때
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