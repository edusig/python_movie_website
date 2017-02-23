"""
Defines a list of movies to generate a web page showing them
"""

import media
import freash_tomatoes

def get_favorite_movies():
    """
    Returns a list of instances of favorite movies
    Most storylines were taken from http://imdb.com
    """
    toy_story = media.Movie('Toy Story',
                            'A story of a boy and his toys that come to life',
                            'http://upload.wikimedia.org/wikipedia/en/1/13/To'
                            'y_Story.jpg',
                            'https://www.youtube.com/watch?v=vwyZH8NQC4')

    avatar = media.Movie('Avatar',
                         'A marine on an alian planet',
                         'http://upload.wikimedia.org/wikipedia/id/b/b0/Avata'
                         'r-Teaser-Poster.jpg',
                         'https://www.youtube.com/watch?v=-9ceBgWV8io')

    ratatouille = media.Movie('Ratatouille',
                              'A rat who can cook makes an unusual alliance '
                              'with a young kitchen worker at a famous '
                              'restaurant.',
                              'http://upload.wikimedia.org/wikipedia/en/5/50/'
                              'RatatouillePoster.jpg',
                              'https://www.youtube.com/watch?v=c3sBBRxDAqk')

    back_to_the_future = media.Movie('Back to the Future',
                                     'Marty McFly, a 17-year-old high school '
                                     'student, is accidentally sent 30 years '
                                     'into the past in a time-traveling '
                                     'DeLorean invented by his close friend, '
                                     'the maverick scientist Doc Brown',
                                     'https://meansheets.files.wordpress.com/'
                                     '2009/12/back-to-the-future.jpg',
                                     'https://www.youtube.com/watch?v=qvsgGti'
                                     'vCgs')

    school_of_rock = media.Movie('School of Rock',
                                 'After being kicked out of a rock band, Dewey'
                                 ' Finn becomes a substitute teacher of a '
                                 'strict elementary private school, only to '
                                 'try and turn it into a rock band.',
                                 'http://upload.wikimedia.org/wikipedia/en/1/'
                                 '11/School_of_Rock_Poster.jpg',
                                 'https://www.youtube.com/watch?v=3PsUJFEBC74')

    the_matrix = media.Movie('The Matrix',
                             'A computer hacker learns from mysterious rebels'
                             ' about the true nature of his reality and his '
                             'role in the war against its controllers',
                             'http://www.impawards.com/1999/posters/matrix_ve'
                             'r1.jpg',
                             'https://www.youtube.com/watch?v=m8e-FF8MsqU')

    jump_street = media.Movie('21 Jump Street',
                              'A pair of underachieving cops are sent back to'
                              ' a local high school to blend in and bring '
                              'down a synthetic drug ring.',
                              'http://www.impawards.com/2012/posters/twenty_o'
                              'ne_jump_street.jpg',
                              'https://www.youtube.com/watch?v=nfkiFVhiIYw')

    fight_club = media.Movie('Fight Club',
                             'An insomniac office worker, looking for a way '
                             'to change his life, crosses paths with a '
                             'devil-may-care soap maker, forming an '
                             'underground fight club that evolves into '
                             'something much, much more',
                             'https://9to5toys.files.wordpress.com/2015/06/fi'
                             'ght-club-poster.jpg?quality=82&strip=all',
                             'https://www.youtube.com/watch?v=SUXWAEX2jlg')

    star_wars = media.Movie('Star Wars: The Force Awakens',
                            'Three decades after the defeat of the Galactic '
                            'Empire, a new threat arises. The First Order '
                            'attempts to rule the galaxy and only a ragtag '
                            'group of heroes can stop them, along with the '
                            'help of the Resistance',
                            'http://a.dilcdn.com/bl/wp-content/uploads/sites/'
                            '6/2015/10/star-wars-force-awakens-official-poste'
                            'r.jpg',
                            'https://www.youtube.com/watch?v=sGbxmsDFVnE')

    return [
        back_to_the_future,
        the_matrix,
        jump_street,
        fight_club,
        school_of_rock,
        toy_story,
        avatar,
        star_wars,
        ratatouille,
    ]

freash_tomatoes.open_movies_page(get_favorite_movies())
