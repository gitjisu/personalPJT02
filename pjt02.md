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

```
def recommendation(title): #이경우 입력받은 영화제목이 query의 title로 들어가야 하기때문에 함수아래에 작성
    BASE_URL = 'https://api.themoviedb.org/3'
    # https://api.themoviedb.org/3.movie/popualr?api_key=e6fcccc78c4a58a99e1758d30d821e54&language=ko&region=KR
    path = '/search/movie'
    params = {
        'api_key' : 'e6fcccc78c4a58a99e1758d30d821e54',
        'language' : 'ko',
        'ragion' : 'KR',
        'query' : title #title = 영화제목이들어감
    }

    response = requests.get(BASE_URL+path, params=params).json()



    for i in response['results']: #기생충의 title이 입력받은 타이틀과 같을경우
        if i['title'] == title:
            movie_id = i['id'] #movie_id에 기생충 id값 추가

    try:
        real_response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key=e6fcccc78c4a58a99e1758d30d821e54&language=ko') #recommendations에 기생충 요청
    
    except UnboundLocalError: #검색할수 없는 영화의 경우 UnboundLocalError발생하기 때문
        return None

    data = real_response.json()

    movie_dict = data.get('results') #추천영화목록에서 가져온 딕셔너리 저장

    recomend_movie = [] #최종값 저장 리스트 생성
    for j in movie_dict: #딕셔너리 순회 
        recomend_movie.append(j.get('title')) #추천영화 제목만 필요함
    
    return recomend_movie #리스트에 리턴

if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면
    해당 영화의 id를 기반으로 추천 영화 목록 구성.
    추천 영화가 없을 경우 [].
    영화 id검색에 실패할 경우 None.
    """
    pprint(recommendation('기생충'))
    # ['조커', '조조 래빗', '1917', ..., '토이 스토리 4', '스파이더맨: 파 프롬 홈']
    pprint(recommendation('그래비티'))
    # []  => 추천 영화 없음
    pprint(recommendation('검색할 수 없는 영화'))
    # => None

```

```
def credits(title): #입력받은 영화제목이 query의 title로 들어가야 하기때문에 함수아래로 작성
    BASE_URL = 'https://api.themoviedb.org/3'
    # https://api.themoviedb.org/3.movie/popualr?api_key=e6fcccc78c4a58a99e1758d30d821e54&language=ko&region=KR
    path = '/search/movie'
    params = {
        'api_key' : 'e6fcccc78c4a58a99e1758d30d821e54',
        'region' : 'KR',
        'language' : 'ko',
        'query' : title
    }

    response = requests.get(BASE_URL+path, params=params).json() 

    for i in response['results']: #영화검색요청정보에서 가져온 리스트중 results 순회
        if i['title'] == title: #입력받은 영화와 같을경우
            movie_id = i['id'] #movie_id에 저장

    try:
        real_response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=e6fcccc78c4a58a99e1758d30d821e54&language=ko') #크래딧정보요청
    
    except UnboundLocalError:
        return None #입력받은영화정보가 존재하지 않을경우를 제외하고
    
    
    data = real_response.json() #크래딧정보

    result = {'cast': [], 'crew': []} #결과값저장딕셔너리생성

    for i in data['cast']: #cast딕셔너리 순회
        if i['cast_id'] < 10: #캐스트 아이디값이 10보다 작을경우
            result['cast'].append(i['name']) #cast키에 name을 벨류로 추가

    for j in data['crew']: #crew딕셔너리 순회
        if j['department'] == 'Directing': #department값이 directing일경우
            result['crew'].append(j['name']) #crew키에 name을 벨류로 추가

    return result

```

