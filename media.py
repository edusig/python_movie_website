"""
media module provides classes to store media related information
"""

class Movie():
    """
    This class provides a way to store movie related information
    """

    def __init__(self, movie_title, storyline, poster_image, yotube_trailer_url):
        self.title = movie_title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = yotube_trailer_url
