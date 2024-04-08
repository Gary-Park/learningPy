"""
    파이썬 공식문서
        https://docs.python.org/ko/3/
        
    외부모듈
    표준모듈
        https://docs.python.org/3/library/index.html

    math, random, sys, os, datetime, time, urllib

    from 구문
        from 모듈 이름 import 가져오고 싶은 변수 또는 함수
    as 구문
        import 모듈 as 사용하고 싶은 식별자
"""
# import random

# print (" # random 모듈 ")
# print (" - random(): ", random.random())

# import sys

# print ( sys.argv )
# print ( "---" )
# print ( "getWindowsVersion:()", sys.getwindowsversion())

import time as tm
print ( tm.ctime())

from urllib import request


target = request.urlopen("https://google.com")
output = target.read()

print (output)
