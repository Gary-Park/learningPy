print("학습사이트 100% 활용하기")
print("hongong.hanbit.co.kr << 예제 파일 다운로드, 동영상 강의 보기, 저자에게 질문하기")
print("VS CODE 단축키 모음")
print("한줄 복사 : S + A + 위아래")
print("한줄 삭제 : C + X")
print("파이썬은 다른 프로그래밍 언어와는 다르게 변수에 자료형을 지정하지 않습니다.")
print()
print()
print("https://pythontutor.com/")
print()
print()
print("SyntaxError")
print("TypeError")
print("IndexError")
print("ValueError : 자료형을 변환할때 '변환할 수 없는 것'을 변환하려고 할때 발생")
print("IndentationError : 조건문에 반드시 필요함 : pass 로 스킵할수 있슴")
print("raise NotImplementedError")
print()
print()
print("Beautiful Soup 모듈")
print("https://www.crummy.com/software/BeautifulSoup/bs4/doc")
"""
#구의 부피와 겉넓이
question = input("구의 반지름을 입력해주세요 : ")
int_question = int(question)
pi = 3.141592

bupi = ( 4 * pi * (int_question**3) ) / 3
nulb = 4 * pi * (int_question**2)

print(" = 구의 부피는 ", bupi, "입니다" )
print(" = 구의 겉넓이는  ", nulb, "입니다" )

#피타고라스의 정리
garo = input("밑변의 길이를 입력해주세요 : ")
float_garo = float(garo)
sero = input("높이의 길이를 입력해주세요 : ")
float_sero = float(sero)

bitbyun = (( float_garo **2) + ( float_sero**2))**(1/2)
print(" = 빗변의 길이는 ",bitbyun, " 입니다.")

import datetime ##모듈

now = datetime.datetime.now()
print(now)
"""
"""
a = int(input("> 1번째 숫자 : "))
b = int(input("> 2번째 숫자 : "))
print()

if a > b :
    print("처음 입력했던 {}가 {}보다 더 큽니다".format(float(a),float(b)))
elif a == b :
    print("{}와 {}는 모두 같습니다.".format(float(a),float(b)))
else :
    print("두번째로 입력했던 {}가 {}보다 더 큽니다".format(float(b),float(a)))

import datetime ##모듈
hour = datetime.datetime.now().hour

inp = str(input("입력 :"))

if inp in ("안녕") :
    print(" > 안녕하세요.")
elif inp in ("몇 시") :
    print("> 지금은 {}시 입니다.".format(hour))
else :
    print("> ",inp)
"""

a = input (" 문자열 입력 > ")
b = input (" 문자열 입력 > ")

print ( a, b )

c = str(a)
a = str(b)
b = c

print ( a, b )

