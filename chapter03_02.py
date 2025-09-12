# Chapter3-2
# 파이썬 문자형
# 문자형 중요


# 문자열 생성
str1 = "I am Python"
str2 = 'Python'
str3 = """How are You?"""
str4 = '''Thank you!'''


print(type(str1), type(str2), type(str3), type(str4))
print(len(str1),len(str2), len(str3), len(str4)) # 문자의 길이 출력


# 빈 문자열
str1_t1 = ""
str2_t2 = str()

print(type(str1_t1), len(str1_t1))
print(type(str2_t2), len(str2_t2))


# 이스케이프 문자 사용
# I'm Boy \

print("I'M Boy")
print('I\'mBoy')

print('a \t b')
print('a \"\ b')

escape_str1 = "Do you have a \"retro games\"?"
print(escape_str1)
escape_str2 = 'What\'s on TV?'
print(escape_str2)

# 탭, 줄 바꿈
t_s1 = "Click \t Start!" # 탭
t_s2 = "New Line \n Check!" # 줄바꿈 \n

print(t_s1)
print(t_s2)
print()

# Row String 출력
raw_s1 = r'D:\tpython\test'
print(raw_s1)

# 멀티라인 입력
multi_Str =\
'''
String
Multi line
Test
'''

print(multi_Str)


# 문자열 연산
str_o1 = "python"
str_o2 = "Apple"
str_o3 = "How are you doing"
str_o4 = "Seoul Deajeon Busan !Jinju"

print(str_o1 * 3) # str1이 세번 반복됌
print(str_o1 + str_o2)# str1 + str2 더해서알려줌
print('y' in str_o1) # str_o1에 y 라는게있어? 있으면 True라고답
print('x' in str_o1) # str_o1에는 x 가없어서 False반환
print('p' in str_o1) # 대소문자를 구별하기에 소문자p는 없다고 반환

# 문자열 형 변환
print(str(66), type(str(66))) # 문자열의 문자66을 의미
print(str(10.1), type(str(10.1)))
print(str(True), type(str(True)))

# 문자열 함수(upper, isalnum, startswith, count, endswith, isal)

print("Capitlize:", str_o1.capitalize()) # 이 함수는 첫번째 글자를 대문자로바꿔준다.
print("endswith?:", str_o2.endswith("e")) # 마지막에 e로끝나는지 묻는것 참과거짓으로나옴
print("replace", str_o1.replace("thon",' Good')) # thon이라는것을 찾아서 Good으로 바꿔줘라는말
print("sorted", sorted(str_o1))
print("split:", str_o4.split('!')) # ! 가있는곳을 기준으로 나눔

# 반복(시퀀스)
im_str = "Good Boy!" 
print(dir(im_str)) # __iter___

# 출력
for i in im_str:
    print(i)

# 슬라이싱 
str_sl = "Nice Python"


# 슬라이싱 연습
print(str_sl[0:3]) # 3-1 까지 나옴 0,1,2가 나옴 
print(str_sl[5:11]) # 띄어쓰기도 포함이니 5~11로해야 Python 출력
print(str_sl[:len(str_sl)]) # str_sl[:11]
print(str_sl[:len(str_sl)-1]) # str_sl[:10]
print(str_sl[1:4:2]) # 1~4 까지 두칸씩 건너띄;어서 가져와라 세번째 인수는 단위(몇 개 단위로 스킵하면서 가져올지)
print(str_sl[-5:])
print(str_sl[1:-2])
print(str_sl[::2])


# 아스키 코드(또는 유니코드)
a = 'z'

print(ord(a))
print(chr(122))

