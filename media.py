import webbrowser


class Movie():
	"""The BluePrint of Movie Information"""
    def __init__(bani, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
    """Initialize Movie Title, Movie Storyline, Poster Images of Movies and Youtube Trailer"""
        bani.title = movie_title
        bani.storyline = movie_storyline
        bani.poster_image_url = poster_image
        bani.trailer_youtube_url = trailer_youtube

"""This Initialize Youtube trailer Object"""
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
