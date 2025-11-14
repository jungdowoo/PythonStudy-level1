# 파이썬 외장(External)함수
# 실제 프로그램 개발 중 자주 사용
# 종류 : sys, pickle, shutill, temfile, time, random 등

# 예제1
import sys

print(sys.argv) # 파이썬 파일을 외부에서 실행할때


# 예제2(강제종료)
# sys.exit() #정말 위험한 함수 강제종료하는 함수


# 예제3(파이썬 패키지 위치)
print(sys.path)

# pickle : 객체 파일 쓰기
import pickle


# 예제4(쓰기)
f = open("test.obj", 'wb')
obj = {1:'python', 2:'study', 3:'basic'}
pickle.dump(obj, f)
f.close # open으로 열었으면 close로 닫아주기

# 예제5(읽기)
f = open('test.obj')


# os : 환경 변수, 디렉토리(파일) 처리 관련, 운영체제 작업 관련
# mkdir(폴더생성), rmdir(폴더삭제 단, 비어있어야함), rename


# 예제6
import os
print(os.environ)
print(os.environ["USERNAME"])

# 예제7(현재 경로)
print(os.getcwd())


# time : 시간 관련 처리
import time

# 예제 8
print(time.time())

# 예제 9 (형태 변환)
print(time.localtime(time.time()))

# 예제 10 (간단 표현)
print(time.ctime())

# 예제 11 (형식 표현)
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))) # 대문자 M은 분


# 예제12 (시간 간격 발생)
for i in range(5):
    print(i)
    time.sleep(1)

# random : 난수 리턴
import random

# 예제13
print(random.random()) # 0 ~ 1 실수

# 예제14
print(random.randint(1,45))
print(random.randrange(1,45))

# 예제15(섞기)
d = [1, 2, 3, 4, 5]
random.shuffle(d)
print(d)


# 예제16(무작위 선택)
c = random.choice(d)
print(c)


# webbrowser : 본인 os의 웹 브라우저 실행

import webbrowser
webbrowser.open("http://google.com")
webbrowser.open_new("http://google.com") # 새탭으로 열기