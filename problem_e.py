from unittest import result
import requests
from pprint import pprint


def credits(title):
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

    for i in response['results']:
        if i['title'] == title:
            movie_id = i['id']

    try:
        real_response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=e6fcccc78c4a58a99e1758d30d821e54&language=ko')
    
    except UnboundLocalError:
        return None
    
    print(real_response.url)

    data = real_response.json()

    result = {'cast': [], 'crew': []}

    for i in data['cast']:
        if i['cast_id'] < 10:
            result['cast'].append(i['name'])

    for j in data['crew']:
        if j['department'] == 'Directing':
            result['crew'].append(j['name'])

    return result



if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면
    해당 영화 id를 통해 영화 상세정보를 검색하여
    주연배우 목록(cast)과 제작진(crew).
    영화 id검색에 실패할 경우 None.
    """
    pprint(credits('기생충'))
    # => {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # => None
