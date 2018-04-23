import fresh_tomatoes # linking with fresh_tomatoes.py
import media # linking with media.py 

# we are creating instances of the class Movie as per media.py
# attributes of Movie class as listed: title, storyline, image, trailer 
dunkirk = media.Movie("Dunkirk (2017)",
                     "Allied soldiers from Belgium, the British Empire and France are surrounded by the German Army, and evacuated during WWII. 8/10 Source: IMDb",
                     "https://upload.wikimedia.org/wikipedia/en/1/15/Dunkirk_Film_poster.jpg",
                     "https://www.youtube.com/watch?v=F-eMt3SrfFU")

budapest_hotel = media.Movie("The Grand Budapest Hotel (2014)",
                     "The adventures of Gustave H, a legendary concierge at a famous hotel, and Zero Moustafa, the lobby boy who becomes his most trusted friend. 8.1/10 Source: IMDb",
                     "https://upload.wikimedia.org/wikipedia/en/1/1c/The_Grand_Budapest_Hotel.png",
                     "https://www.youtube.com/watch?v=1Fg5iWmQjwk")

interstellar = media.Movie("Interstellar (2014)",
                     "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival. 8.6/10 Source: IMDb",
                     "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                     "https://www.youtube.com/watch?v=0vxOhd4qlnA")

pianist = media.Movie("The Pianist (2002)",
                     "A Polish Jewish musician struggles to survive the destruction of the Warsaw ghetto of World War II. 8.5/10 Source: IMDb",
                     "https://upload.wikimedia.org/wikipedia/en/a/a6/The_Pianist_movie.jpg",
                     "https://www.youtube.com/watch?v=u_jE7-6Uv7E")

godfather = media.Movie("The Godfather (1972)",
                     "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son. 9.2/10 Source: IMDb",
                     "https://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg",
                     "https://www.youtube.com/watch?v=sY1S34973zA")

hobbit = media.Movie("The Hobbit: An Unexpected Journey (2012)",
                    "A reluctant Hobbit, Bilbo Baggins, sets out to the Lonely Mountain with a spirited group of dwarves to reclaim their mountain home. 7.9/10 Source: IMDb",
                    "https://upload.wikimedia.org/wikipedia/en/a/a9/The_Hobbit_trilogy_dvd_cover.jpg",
                    "https://www.youtube.com/watch?v=SDnYMbYB-nU")

lord_of_the_rings_1 = media.Movie("The Lord of the Rings - The Fellowship of the Ring (2001)",
                                "A meek Hobbit from the Shire and eight companions set out on a journey to destroy the powerful One Ring and save Middle-earth from the Dark Lord Sauron. 8.8/10 Source: IMDb",
                                "https://upload.wikimedia.org/wikipedia/en/9/9d/The_Lord_of_the_Rings_The_Fellowship_of_the_Ring_%282001%29_theatrical_poster.jpg",
                                "https://www.youtube.com/watch?v=V75dMMIW2B4")

lord_of_the_rings_2 = media.Movie("The Lord of the Rings - The Two Towers (2002)",
                                "While Frodo and Sam edge closer to Mordor with the help of the shifty Gollum, the divided fellowship makes a stand against Sauron's new ally, Saruman. 8.7/10 Source: IMDb",
                                "https://upload.wikimedia.org/wikipedia/en/a/ad/Lord_of_the_Rings_-_The_Two_Towers.jpg",
                                "https://www.youtube.com/watch?v=LbfMDwc4azU")

lord_of_the_rings_3 = media.Movie("The Lord of the Rings - The Return of the King (2003)",
                                "Gandalf and Aragorn lead the World of Men against Sauron's army to draw his gaze from Frodo and Sam as they approach Mount Doom with the One Ring. 8.9/10 Source: IMDb",
                                "https://upload.wikimedia.org/wikipedia/en/9/9d/Lord_of_the_Rings_-_The_Return_of_the_King.jpg",
                                "https://www.youtube.com/watch?v=r5X-hFf6Bwo")

# lists movies to pass to open_movies_page function from fresh_tomatoes.py
movies = [dunkirk, budapest_hotel, interstellar, pianist, godfather, hobbit, lord_of_the_rings_1, lord_of_the_rings_2, lord_of_the_rings_3]
fresh_tomatoes.open_movies_page(movies)

# prints list of ratings from media.py
#print(media.Movie.VALID_RATINGS) 
