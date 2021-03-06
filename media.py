"""This is class for Movie objects which contains details of movie"""


class Movie():
    """This class provides a way to store movie related information.

    Attributes:
        title: A string to store the title of the movie.
        storyline: A string to store the basic plot of the movie.
        poster_image_url: A string to store the URL of the movie poster.
        trailer_youtube_url: A string to store the URL of the movie trailer.
        release_date: A string to store the release date of the movie."""

    """init method is called when object is initialzed"""
    """self refers to current instance of class"""
    def __init__(self, name, storyline, poster, youtube_url, release_date):
        """Initialises Movie class instance variables."""
        self.title = name
        self.storyline = storyline
        self.poster_image_url = poster
        self.trailer_youtube_url = youtube_url
        self.release_date = release_date

