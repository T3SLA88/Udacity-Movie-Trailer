import media
import fresh_tomatoes

# create instances of your favourite movies
the_avengers = media.Movie('The Avengers',
                           'Earths mightiest heroes must come\
                           together and learn to fight',
                           'https://bit.ly/2ukVQb6',
                           'https://www.youtube.com/watch?v=eOrNdBpGMv8')

baby_driver = media.Movie('Baby Driver',
                          'A deaf boy driver and his girl story',
                          'https://bit.ly/2KX4nv9',
                          'https://www.youtube.com/watch?v=6XMuUVw7TOM')

logan = media.Movie('Logan (2017)',
                    'Logans legacy, are upended when a young mutant\
                    arrives, pursued by dark forces.',
                    'https://bit.ly/2L2Twge',
                    'https://www.youtube.com/watch?v=gbug3zTm3Ws')

rush = media.Movie('Rush (2013)',
                   'The merciless 1970s rivalry between Formula\
                   One rivals James Hunt and Niki Lauda.',
                   'https://bit.ly/2N2BQSi',
                   'https://www.youtube.com/watch?v=lzNbGH1oZJc')

incredibles_2 = media.Movie('Incredibles 2 (2018)',
                            'Bob Parr (Mr. Incredible) is left to care for\
                            the kids while Helen (Elastigirl) is out\
                            saving the world.',
                            'https://bit.ly/2KHCjwB',
                            'https://www.youtube.com/watch?v=i5qOzqD9Rms')

wall_e = media.Movie('WALL - E (2008)',
                     'In the distant future, a small waste-collecting robot',
                     'https://bit.ly/2NEC0AL',
                     'https://www.youtube.com/watch?v=alIq_wG9FNk')

# create a list of the movies instances
movies = [the_avengers, baby_driver, logan, rush, incredibles_2, wall_e]

''' call the fresh tomatoes class and
pass in the list of movies to display on the page'''
fresh_tomatoes.open_movies_page(movies)
