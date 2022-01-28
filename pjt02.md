```
import requests
from pprint import pprint

BASE_URL = 'https://api.themoviedb.org/3'
api_key=e6fcccc78c4a58a99e1758d30d821e54&language=ko&region=KR
path = '/movie/popular'
params = {
    'api_key' : 'e6fcccc78c4a58a99e1758d30d821e54',
    'language' : 'ko',
    'ragion' : 'KR'
}

response = requests.get(BASE_URL+path, params=params) #사이트에 요청하기


def popular_count():
    
    data = response.json() #response한 데이터를 json으로 변환
    return len(data.get('results')) #results의 목록(영화목록)길이 len사용

    

```

```
import requests
from pprint import pprint

BASE_URL = 'https://api.themoviedb.org/3'
# https://api.themoviedb.org/3.movie/popualr?api_key=e6fcccc78c4a58a99e1758d30d821e54&language=ko&region=KR
path = '/movie/popular'
params = {
    'api_key' : 'e6fcccc78c4a58a99e1758d30d821e54',
    'language' : 'ko',
    'ragion' : 'KR'
}

response = requests.get(BASE_URL+path, params=params)


def vote_average_movies():
    total = [] #8점이상 영화목록 담을 리스트 생성
    data = response.json()
    a = data.get('results')
    for i in a: #for문을 사용하여 results 순회
        average = i.get('vote_average') #vote_average 딕셔너리 접근
        if average >= 8: #8점이상일경우
            total.append(i) #total리스트에 추가
    return total
```

```
import json
import requests
from pprint import pprint

BASE_URL = 'https://api.themoviedb.org/3'
# https://api.themoviedb.org/3.movie/popualr?api_key=e6fcccc78c4a58a99e1758d30d821e54&language=ko&region=KR
path = '/movie/popular'
params = {
    'api_key' : 'e6fcccc78c4a58a99e1758d30d821e54',
    'language' : 'ko',
    'ragion' : 'KR'
}

response = requests.get(BASE_URL+path, params=params)


def ranking():
    data = response.json()
    total = [] #ranking5 영화 담을 리스트 생성
    a = data.get('results') 
    b = sorted(a, key=lambda item:item['vote_average'], reverse= True)
    #for문으로 하려고 했으나 오류 나서 딕셔너리 키값으로 정렬하는 방법 찾아보니 람다함수있어서 사용
    #람다함수..아직 이해 못함..
    total = b[:5]
    #내림차순 정렬한거 슬라이싱
    return total
```

