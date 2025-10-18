# 예외처리
# Input 사용자 입력



# 예제1 -> 예외처리 
# 숫자를 입력하면 Ok.문구출력 만약 숫자가 아닌 문자입력이라면 This is not a number 출력
# Java에서는 try catch지만 파이썬에서는 try except 사용

try:
    n = int(input('Enter a number : '))
    print('Ok. Your number is :', n)
except ValueError:
    print('This is not a number.')


# 예제2 -> 올바른 값 입력 완료까지 지속
while True:
    try:
        n = int(input('Enter a number :'))
        break
    except ValueError:
        print('This is not a number.')
print('OK. Your number is:', n)