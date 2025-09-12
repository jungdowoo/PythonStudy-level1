#파이썬 완전 기초
# Print 사용법

print('Python Start!')
print("Python Start!")
print('''Python Start!''') 


# separator 옵션
print('P','Y','T','H','O','N', sep='')
print('010','7777','3333',sep='-')

print('python','google.com', sep='@')






# end 옵션

print('Welcome to', end='       ')
print('IT News', end='   ')
print('Web Site')
print()
# 파일옵션
import sys


print('Learn Python', file=sys.stdout)
print()

#format 사용(d:3, s:'python', f: 3.14444)

print('%s %s' % ('one','two')) # 첫번째 %s에는 one이 두번째에는 two가 들어감
print('{} {}'.format('one','two')) # 같은 결과값이지만 가독성이 좀 더좋음
print('{1} {0}'.format('one','two')) # 인덱스는 무조건0부터인데 {1} {0}이라 two,one으로 결과값이나옴

# %s
print('%10s' % ('nice')) # 10개의자릿수 공백포함 nice가 10자리수가됌 양수일경우 왼쪽에 공백
print('{:>10}'.format('nice')) #왼쪽에 지정후10자리공백


print('%-10s' % ('nice')) #음수-가오면 오른쪽부터 공백을채움
print('{:10}'.format('nice'))#>< 를 생략하면 오른쪽에 공백을 채움


print('{:_>10}'.format('nice')) #공백을 밑줄로채워줌
print('{:^10}'.format('nice')) #중앙정렬 ^

print('%.5s' % ('nice'))
print('%.5s' % ('pythonstrrr'))   # 5글자 절삭 .을붙여야 절삭
print('{:10.5}'.format('pythonstudy'))  # 총 10개의자리를차지하지만 5개만보여줘라 (공간은10개이지만 다섯글자만보여라)

# %d (정수출력)
print('%d %d' % (1,2))
print('{} {}'.format(1,2))


print('%4d' % (42))
print('{:4d}'.format(42)) # 정수일때는 d붙여줘야함


# %f 실수형

print('%1.18f' % (3.14444444111111)) # 정수부.소수부 1.18
print('{:f}'.format(3.14141414123123))

print('%06.2f' % (3.1415926531231231))
print('{:06.2f}'.format(3.141414141414))

#문자열은 생략가능하지만 정수형 실수형에는 d,f를 꼭써줘야함