# 파일 읽기 및 쓰기
# 읽기 모드 : r(read), 쓰기모드 w(write), 추가모드 a(append), 텍스트 모드 t, 바이너리 모드 b
# 상대 경로('../, ./'), 절대 경로('C:\Django\example..')

# 파일 읽기(Read)
# 예제1

f = open('절대경로넣기', 'r', encoding='UTF-8')
# 속성확인
print(dir(f))
# 인코딩 확인
print(f.encoding)
# 파일 이름
print(f.name)
# 모드 확인
print(f.mode)
cts = f.read()
print(cts)
# 반드시 close
f.close()

