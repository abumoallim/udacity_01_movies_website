import media
import fresh_tomatoes


def main():
    """Initializing object with particular data"""
    """At particular instance __init__ method is invoked"""
    martian = media.Movie(
        "The Martian",
        "A man is stuck on Mars",
        "http://t2.gstatic.com/images?q=tbn:ANd9GcTkKPZ7EIOafEsemyn6zTIDeGYthKC_Okgxi1eX6diuOT3xKWXQ",
        "https://www.youtube.com/watch?v=lQqhfq87FgY",
        "September 24, 2015"
    )

    matrix = media.Movie(
        "The Matrix",
        "The world is a simulation",
        "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
        "https://www.youtube.com/watch?v=vKQi3bBA1y8",
        "March 31, 1999"
    )

    harry_potter = media.Movie(
        'Harry Potter and the Chamber of Secrets',
        "Harry ignores warnings not to return to Hogwarts, only to find "
        "the school plagued by a series of mysterious attacks and a "
        "strange voice haunting him.",
        'http://t0.gstatic.com/images?q=tbn:ANd9GcTltzcooPkGcy1fKKqzSuO8U6S9XBpNDR9MuYc9SS_L5AbAn66O',
        'https://www.youtube.com/watch?v=dmPrfYkpwTY',
        "July 11, 1997"
    )

    spectre = media.Movie(
        "Spectre",
        "The latest James Bond movie",
        "http://t3.gstatic.com/images?q=tbn:ANd9GcQcjheOnBb_WFU5yuYLnUYWjfr33KzdFx1PCNGVhgM4-89otmi9",
        "https://www.youtube.com/watch?v=vBnGxAkdh_k",
        "October 26, 2015"
    )

    harry_potter_2 = media.Movie(
        'Harry Potter and the Prisoner of Azkaban',
        "It's Harry's third year at Hogwarts; not only does he have"
        "a new \"Defense Against the Dark Arts\" teacher, but there"
        "is also trouble brewing. Convicted murderer Sirius Black"
        "has escaped the Wizards' Prison and is coming after Harry.",
        'http://t3.gstatic.com/images?q=tbn:ANd9GcSkFf3MN_oao6q3gysHpVfJA2lICz2ckgXE2VoKRWEGk0huoKnQ',
        'https://www.youtube.com/watch?v=lAxgztbYDbs',
        "June 9, 2004"
    )

    midnight_in_paris = media.Movie(
        "Midnight in Paris",
        "This Movie is About Time Travel",
        "http://t3.gstatic.com/images?q=tbn:ANd9GcTk3ssys2bKM5-U6XMgvoD8yVoS5Io2YKg_1xA6x6GA8mKuuqID",
        "https://www.youtube.com/watch?v=BYRWfS2s2v4",
        "May 13, 2011"
    )

    """Storing all the objects in the list"""
    movies = [martian, matrix, harry_potter, spectre, harry_potter_2, midnight_in_paris]
    """Passing this list to fresh_tomatoes class for rendering it to html"""
    fresh_tomatoes.open_movies_page(movies)

"""Will called only when executed not when imported"""
if __name__ == '__main__':
    main()

