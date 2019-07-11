import api
import requests.exceptions
from logbook import RotatingFileHandler, debug, info, warn, exception


def main():
    handler = RotatingFileHandler("MovieSearch")
    handler.push_application()

    keyword = input('Keyword of title search: ')
    try:
        results = api.find_movie_by_title(keyword)
        debug(f"Gut results: {results} for search of keyword: {keyword}")

        print(f'There are {len(results)} movies found.')
        for r in results:
            print(f"{r.title} with code {r.imdb_code} has score {r.imdb_score}")
    except requests.exceptions.ConnectionError:
        exception("Could not find server.")
        print("ERROR: Could not find server. Check your network connection.")

    except ValueError:
        print("ERROR: You must specify a search term.")
    except Exception as x:
        exception(x)


if __name__ == '__main__':
    main()
