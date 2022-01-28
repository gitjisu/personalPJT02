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
# # print(response.status_code, response.url)
# data = response.json()
# print(type(data)) #dict
# print(data.keys()) #dict_keys(['page', 'results', 'total_pages', 'total_results'])
# print(type(data.get('results'))) #list
# print(data.get('results')[0]) #list의 첫번째 구조
# print(len(data.get('results')))


def popular_count():
    
    data = response.json()
    return len(data.get('results'))

    



if __name__ == '__main__':
    """
    popular 영화목록의 개수 출력.
    """
    print(popular_count())
    # => 20
