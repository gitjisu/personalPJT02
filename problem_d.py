from turtle import title
import requests
from pprint import pprint


def recommendation(title):
    BASE_URL = 'https://api.themoviedb.org/3'
    # https://api.themoviedb.org/3.movie/popualr?api_key=e6fcccc78c4a58a99e1758d30d821e54&language=ko&region=KR
    path = '/search/movie'
    params = {
        'api_key' : 'e6fcccc78c4a58a99e1758d30d821e54',
        'language' : 'ko',
        'ragion' : 'KR',
        'query' : title
    }

    response = requests.get(BASE_URL+path, params=params).json()



    for i in response['results']:
        if i['title'] == title:
            movie_id = i['id']

    try:
        real_response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key=e6fcccc78c4a58a99e1758d30d821e54&language=ko')
    
    except UnboundLocalError:
        return None

    data = real_response.json()

    movie_dict = data.get('results')

    recomend_movie = []
    for j in movie_dict:
        recomend_movie.append(j.get('title'))
    
    return recomend_movie

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
