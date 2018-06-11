

```python
# 1
girlsday_members = ['민아', '혜리', '유라', '소진']
```


```python
def girlsday():
    for m in girlsday_members:
        print('-',m)

girlsday_info = girlsday()
girlsday_info
```

    - 민아
    - 혜리
    - 유라
    - 소진



```python
# 2
fruit_dict = {
    'red': 'apple',
    'yellow': 'banana',
    'green': 'melon',
}
def fruit():
    n = -1
    for color, item in fruit_dict.items():
        
        n +=1
        print(f'[{n}]', color.upper(),':', item)
fruit_info = fruit()
fruit_info
```

    [0] RED : apple
    [1] YELLOW : banana
    [2] GREEN : melon



```python
# 3
# list 에서 copy() 가 하는 일,
# a 리스트가 있을 때 a의 리스트를 b라는 새로운 리스트에 복사할때
a = ['do', 'is', 'not', 'for', 'hell']
b = a
```


```python
a
```




    ['do', 'is', 'not', 'for', 'hell']




```python
b
```




    ['do', 'is', 'not', 'for', 'hell']




```python
a is b
```




    True




```python
# 출력했을때 두 리스트가 가리키는 매모리 주소가 같다. 이때 a의 list에서
# 하나를 지우면 b의 리스트에서 무슨일이 일어날까?
print(id(a))
print(id(b))
```

    4473670920
    4473670920



```python
a.remove('do')
```


```python
a
```




    ['is', 'not', 'for', 'hell']




```python
# b의 리스트에 있는 내용도 지워진다.
# 이를 Shallow Copy(얕은 복사) 라고 하는데
# 이러한 현상을 피하기위해 copy() 함수를 사용한다.
b
```




    ['is', 'not', 'for', 'hell']




```python
c = a.copy()
```


```python
c
```




    ['is', 'not', 'for', 'hell']




```python
c is a
```




    False




```python
# 내용은 같아도 둘이 가르키는 메모리 주소가 다르다.
# 이렇게 사용할때 a의 값이 수정되도 c의 값이 영향을 미치는 일은 없다.
```


```python
# 4
num = [i for i in range(3,31,4)]
print(num)
```

    [3, 7, 11, 15, 19, 23, 27]



```python
# 5
# dict형 객체인 `obj`가 있다고 할 때, `obj['key']`와 `obj.get('key')`의 차이를 서술하시오.
# `obj['key']` 를 사용하여 호출했을때 해당하는 키가 없을 경우에 키 에러가 난다.
# `obj.get('key')` 를 사용하여 호출했을때 해당하는 키가 없을 경우 에러를 호출하지 않는다.
```


```python
# 6
pokemon_info = [
    ('피카츄', '전기 타입'),
    ('파이리', '불 타입'),
    ('꼬부기', '물 타입'),
    ('이상해씨', '풀 타입'),
]

for i in pokemon_info:
    print(i[0], i[1])
# 튜플 언패킹은 하나의 리스트 또는 튜플에 여러게의 리스트나 튜플이 들어가 있을 때 그것을 풀어주는 것


```

    피카츄 전기 타입
    파이리 불 타입
    꼬부기 물 타입
    이상해씨 풀 타입



```python
# 7
# 위치인자는 들어오는 순서대로 미리 정의한 인자에 할당된다. *args 로 사용하며 *만 앞에 붙으면 뒤의 args는 다른걸로 대체해도 상관없다. 관용적으로 사용된다.
# 키워드 인자는 정해놓은 키워드에 알아서 들어간다. **kwargs 로 사용된다.
# 키워드 인자는 키워드로 미리 정해놓은 인자이며 해당 키워드만 앞서 선언해주면 순서는 상관 없다.
# 키워드 인자
def sells(a=0,b=0,c=0):
   return a + b + c
sells(a=1, b=2, c=3)
```




    6




```python
# 8
# - 클래스와 인스턴스의 차이점 [2점]
# 클래스는 함수를 묶어놓은 가방, 인스턴스는 가방의 내용물, 내가집어놓은 서류 등
# - 클래스의 생성자 함수 이름 [1점]
# method
# - 클래스의 생성자 함수가 호출되는 시점은? [2점]
# 인스턴스를 클래스에 정의할때, 클래스에 있는 method 를 사용할때
# - 인스턴스 메서드의 `self`매개변수의 의미 [4점]
# 자기자신, 즉 인스턴스가 post_list 라면 self 는 post_list
```


```python
# 9
# `property`를 정의하는 방법에 대해 서술하시오. [5점]
# property는 클래스 내부에 사용되며 @property로 선언한다.
# 사용법은
class Post:
    def __init__(self):
        pass
    
    @property
    def info(self):
        return '이렇게'
# property는 읽기전용
```


```python
# 10
# 아래와 같은 `User`클래스가 있다. 이 클래스를 상속받은 `Student`클래스를 정의하고, 초기화 메서드에서 `name`과 함께`age`라는 매개변수를 추가로 사용해 인스턴스의 `age`속성을 추가로 정의하도록 한다. [10점]

# - (기본구현) User클래스를 상속: 1
# - 초기화 메서드 재정의: +3
# - 초기화 메서드에서 `super`사용: +6

class User:
    def __init__(self, name):
        self.name = name

class Student(User):
    def __init__(self, age):
        super(). __init__(name)
        self.age = age

```


```python
# 11 `url`주소로부터 아래 결과를 출력한다. [10점]
# url = 'http://www.leagueoflegends.co.kr/?m=news&cate=notice'
import requests
import os
from bs4 import BeautifulSoup
from urllib import parse

def html():
    url = 'http://www.leagueoflegends.co.kr/?m=news&cate=notice'
    file_path = 'data/notics.html'
    if os.path.exists(file_path):
        html = open(file_path, 'rt').read()
    else:
        response = requests.get(url)
        html = response.text
        open(file_path, 'wt').write(html)
    soup = BeautifulSoup(html, 'lxml')
    title_wrap = soup.select('td.tleft > a')
    for i in title_wrap:
        print(i.get_text())
html()
```

    top[#2] 격전을 준비하세요! (수정)
    top격전 참여시 불건전 행위에 대한 주의사항 안내(수정)
    대리 게임 등 적발 현황 263차 안내
    부정행위 프로그램 제재 현황 안내
    6월 2차 소환사 문화재지킴이 모집 안내
    일부 클라이언트 오류 현상에 대한 안내 (정상화)
    6월 6일(수) 서버 점검 안내 (완료)
    PBE 인사이드 20화(8.12 패치 편) 방송 안내
    다시 돌아온 격전! 얼불져스 6/5(화) 방송 일정 안내
    1일 격전 테스트에 참여해 주세요
    대리 게임 등 적발 현황 262차 안내
    부정행위 프로그램 제재 현황 안내



```python
# 12 `url`주소에 있는 공지사항에 해당하는 `Notice`클래스를 만들고,
# 크롤링시 공지사항 하나마다 `Notice`클래스 인스턴스를 만들어 `notice_list`리스트에 추가한다. [10점]

# class 

```


```python
# 13 runserver가 localhost:8000에서 입력을 받는 상태로 동작 중일 때, 브라우저에서 `http://localhost:8000/abc/`URL을 입력하면
# 어떤 절차를 거쳐 사용자에게 다시 화면을 보여주는지 서술하시오. [10점]
# 브라우져 -> 리퀘스트 -> 서버 -> 리스폰스 -> 서버 -> 브라우져
```
