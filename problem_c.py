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
    total = []
    a = data.get('results')
    # b = sorted(a, key=lambda item:item['vote_average'], reverse= True)
    # total = b[:5]
    # return total
    rank = sorted(a['vote_average'], reverse=True)
    return rank

    
    

        
        
   
if __name__ == '__main__':
    """
    popular 영화목록을 정렬하여 평점순으로 5개 영화.
    """
    pprint(ranking())
    # => 영화정보 순서대로 출력

