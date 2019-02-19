# 5-2 Q1

1. sys.path.append 이용하기
import sys
sys.path.append("C:/doit/mymod")
import mymod

2. PYTHONPATH 환경 변수 사용하기
C:\Users>set PYTHONPATH =C:\doit\mymod
C:\Users>python
-----python shell-----
import mymod
