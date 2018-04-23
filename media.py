import webbrowser # we are importing this module to use the web-based documents

class Movie():
    # this class or object stores the database.
    # we know that each movie is going to have the same attributes (title, storyline, image, trailer)
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
        
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
    # init (constructor) passes parameters to the class when instantiating it 
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
    # represent the instance calling the method with the parameter via 'self'
        webbrowser.open(self.trailer)

