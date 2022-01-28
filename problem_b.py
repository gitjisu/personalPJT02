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
    total = []
    data = response.json()
    a = data.get('results')
    for i in a:
        average = i.get('vote_average')
        if average >= 8:
            total.append(i)
    return total


if __name__ == '__main__':
    """
    popular 영화목록중 vote_average가 8 이상인 영화목록 출력.
    """
    pprint(vote_average_movies())
    # => 영화정보 순서대로 출력
