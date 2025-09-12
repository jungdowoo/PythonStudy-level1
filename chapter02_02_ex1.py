# Chapter02-1-ex1
# Print 사용법
# 파이썬 3가지 Print Formatting
# 자주 나오는 질문 참고

### 3가지 Format Practices

x = 50
y = 100
text = 308276567
n = 'Lee'

# 출력1
ex1 = 'n = %s, s = %s, sum=%d' %  (n, text, (x + y))
print(ex1)

# 출력2
ex2 = 'n = {n}, s = {s}, sum={sum}'.format(n=n, s=text, sum=x+y)
print(ex2)

# 출력3
ex3 = f'n = {n}, s = {text}, sum={x + y}'
print(ex3)

# 구분기호
m = 10000000

print(f'm : {m:,}') # 1000단위별로,찍어줌

print()
print()

# 정렬
# ^ : 가운데 정렬 , <: 왼쪽정렬, >: 오른쪽 정렬

t = 20

print(f"t : {t:10}")
print(f"t center :  {t:^10}")
print(f"t center :  {t:<10}")
print(f"t center :  {t:>10}")

print()
print()

print(f"t center :  {t:-^10}") # -를 써주면 빈칸을 - 로됌 @도되고 상관없음


