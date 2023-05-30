Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> avengers = [ "아이언맨", "토르", "헐크", "스칼렛 위치"]
>>> avengers[1] = "스파이더맨"
>>> print(avengers)
['아이언맨', '스파이더맨', '헐크', '스칼렛 위치']
>>> avengers.append("비전")
>>> print(avengers)
['아이언맨', '스파이더맨', '헐크', '스칼렛 위치', '비전']
>>> avengers.insert(3,"캡틴 아메리카")
>>> print(avengers)
['아이언맨', '스파이더맨', '헐크', '캡틴 아메리카', '스칼렛 위치', '비전']
>>> avengers.remove("비전")
>>> print(avengers)
['아이언맨', '스파이더맨', '헐크', '캡틴 아메리카', '스칼렛 위치']
