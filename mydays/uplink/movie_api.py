from uplink import Consumer, get, Path, Query


class MovieSearch(Consumer):
    """A Python client for the TalkPython.fm movie search API"""
    def __init__(self, base_url, **kwargs):
        self.base_url = base_url
        super().__init__(base_url, **kwargs)

    @get("/api/search/{keyword}")
    def search_movies(self, keyword):
        """Search movies by keyword."""

    @get("/api/director/{director_name}")
    def by_director(self, director_name):
        """Search movies by director."""

    @get("/api/movie/{imdb_code}")
    def by_imdb(self, imdb_code):
        """Search movies by """
