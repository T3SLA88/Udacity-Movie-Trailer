import webbrowser


class Movie():
    '''
    This class is used to create instances of movies
    using the instance variable below

    __init__ initialises a movie instance

    Arguments that are passed to the __init__

    m_title = pass in a string caontaining the movie title
    m_storyline = pass in a string describing the movie
    poster_image = a link to the movie poster
    trailer_youtube = a link to the movie trailer on youtube
    '''

    def __init__(self, m_title, m_storyline, poster_image, trailer_youtube):
        self.title = m_title
        self.storyline = m_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):  # function to play the trailer in a web browser
        webbrowser.open(self.trailer_youtube_url)
