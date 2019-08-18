from movie_api import MovieSearch

search = MovieSearch(base_url="http://movie_service.talkpython.fm/")

keyword = input("Enter a keyword to search:")
resp = search.search_movies(keyword)
print(resp.json())
