
import webbrowser
import fresh_tomatoes

class Movie ():
    """
        'Movie' maintains the meta data for a single movie.
    """

    def __init__(self, title, storyline, poster_url, trailer_url):
        """
            - title: the movie title
            - storyline: the short description about a movie
            - poster_url: URL for a movie poster image
            - trailer_url: URL for a movie trailer
        """
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_url
        self.trailer_youtube_url = trailer_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

# This is the metadata of my three favorite movies

die_hard = Movie(
    "Die Hard",
    "John McClane, officer of the NYPD, tries to ....",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTA4MjcyOTUxOTleQTJ"
    "eQWpwZ15BbWU2MDIxNjExOQ@@._V1_.jpg",
    "https://youtu.be/-qxBXm7ZUTM")

redemption = Movie(
    "The ShawShank Redemption",
    "Two imprisoned men bond over a number of years, finding solace and ...",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BODU4MjU4NjIwNl5BMl5B"
    "anBnXkFtZTgwMDU2MjEyMDE@._V1_SY1000_CR0,0,672,1000_AL_.jpg",
    "https://youtu.be/6hB3S9bIaco")

field_of_dreams = Movie(
    "Field of Dream",
    "An Iowa corn farmer, hearing voices, interprets them as a command to ...",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BNzk5OWY0YjAtYWU3ZS"
    "00Y2Q4LWFlNjItMzgwMTQ2MjIyMDFmL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQx"
    "NzMzNDI@._V1_SY1000_CR0,0,665,1000_AL_.jpg",
    "https://youtu.be/sHTsQ9qePrQ")

list_movies = [ die_hard, redemption, field_of_dreams ]

def generate_movies_page(movies):
    """
         This function generates the movie page dynamically
    """
    fresh_tomatoes.open_movies_page(movies)

# This is the code to produce the web page.
generate_movies_page(list_movies)
