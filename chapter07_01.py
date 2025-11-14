# 파이썬 예외처리의 이해
# 예외 종류
# SyntaxError(문법 에러), TypeError(서로 더할수 없는자료형을 더했을때), NameError, IndexError, ValueError, KeyError...
# 문법적으로는 예외가 없지만, 코드 실행 프로세스(단계)발생하는 예외도 중요
# 1. 예외는 반드시 처리
# 2. 로그는 반드시 남긴다.
# 3. 예외는 던져진다.
# 4. 예외 무시


# 1. SyntaxError : 문법 오류

#print('error)
# print('error))
# if True
#   pass


# 2. NameError : 참조 없음 (선언되지 않은걸 사용할 떄)

# a = 10
# b = 15
# print(c)

# 3. ZeroDivisionError
#print(100 / 0) # 0으로는 나눌수 없음

# 4. IndexError
# x = [50, 70, 90]
# print(x[1])
# print(x[4])
# print(x.pop())
# print(x.pop())
# print(x.pop())
# print(x.pop())

# 5. KeyError
# dic = {'name': 'Lee', 'Age':'41', 'City':'Busan'}
# print(dic['hobby'])
# print(dic.get('hobby'))

# 6. AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용 예외
# import time
# print(time.time2())

# 7. ValueError

# x = [10, 50, 90]
# x.remove(50)
# print(x)
# x.remove(200)


# 8. FileNotFoundError

# f = open('test.txt')

# 9. TypeError : 자료형에 맞지 않는 연산을 수행 할 경우
# x = [1, 2]
# y = (1, 2)
# z = 'test'

# print(x + y)
# print(x + z)
# print(y + z)

# 올바른 코드 print(x + list(y)) 형변환해주기
# print(x + list(z))


# 예외 처리 기본
# try : 에러가 발생 할 가능성이 있는 코드 실행
# except 에러명1 : 여러개 가능
# except 에러명2 :
# else : try 블록의 에러가 없을 경우 실행
# finally : 항상 마지막에 실행




name = ['Kim', 'Lee', 'Park']
# 예제1
# try:
#     z = 'Kim' # Cho같은걸로 바꾸면 예외처리에러발생
#     x = name.index(z)
#     print('Found it! {} in name'.format(z, x + 1))
# except ValueError:
#     print('Not found it! - Occurred ValueError!')
# else:
#     print('Ok! else.')

# print()


# 예제2
# try:
#     z = 'Kim' 
#     x = name.index(z)
#     print('Found it! {} in name'.format(z, x + 1))
# except Exception: # 모든에러를 다잡지만 무슨 에러인지 알수가없음
#     print('Not found it! - Occurred ValueError!')
# else:
#     print('Ok! else.')

# print()


# 예제3
# try:
#     z = 'Cho' 
#     x = name.index(z)
#     print('Found it! {} in name'.format(z, x + 1))
# except Exception as e: # 에러의 내용을 출력
#     print(e)
#     print('Not found it! - Occurred ValueError!')
# else:
#     print('Ok! else.')
# finally:
#     print('Ok! finally!')

# print()


# 예제4
# 예외 발생 : raise
# raise 키워드로 예외 직접 발생

# try:
#     a = 'Park'
#     if a == 'Kim':
#         print('Ok! Pass!')
#     else:
#         raise ValueError
# except ValueError:
#     print('Occurred! Exception!')
# else:
#     print('Ok! else!')