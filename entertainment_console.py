import media
import fresh_tomatoe


monsters_inc = media.Movie("Monsters Inc",
                           "Monsters scare kids ,and use"
                           "their screams as energy.",
                           "https://www.movieposter.com/posters"
                           "/archive/main/115/MPW-57986",
                           "https://www.youtube.com/watch?v=cvOQeozL4S0")

beautiful_mind = media.Movie("A Beautiful Mind", "Mathematician works a"
                             "secret job,creating a nightmare.",
                             "http://static.rogerebert.com/uploads/movie/"
                             "movie_poster/a-beautifmind-2001/large_v1WdK"
                             "m9qQPBfhoHanBP5XxzIBDU.jpg",
                             "https://www.youtube.com/watch?v=aS_d0Ayjw4o")

schindlers_list = media.Movie("Schindler's List", "Schindler saves people"
                              "during WWII",
                              "http://www.bradleyfarless.com/wp-content/"
                              "uploads/2013/06/1du18TPUDqO3NNxeDY"
                              "x3sJGWPs4.jpg",
                              "https://www.youtube.com/watch?v=M5FpB6qDGAE")

bridge_terabithia = media.Movie("Bridge to Terabithia",
                                "Boy befriends girl.",
                                "http://img.moviepostershop.com/bridge-to"
                                "-terabithiamovie"
                                "-poster-2007-1020399124.jpg",
                                "https://www.youtube.com/watch?v=3SvqEIKP4t8")

les_miserables = media.Movie("Les Miserables", "Jean Valjean breaks parole",
                             "http://www.impawards.com/2012/posters/"
                             "les_miserables_ver3.jpg",
                             "https://www.youtube.com/watch?v=IuEFm84s4oI")

harry_potter = media.Movie("Harry Potter", "Boy finds out he is a wizard",
                           "https://www.harrypottermovieposters.com/wp-"
                           "content/uploads/2013/08/harry-potter-"
                           "and-the-order-of-the-phoenix-movie"
                           "-poster-style-d.jpg",
                           "https://www.youtube.com/watch?v=K1KPcXRMMo4")


movies = [monsters_inc, beautiful_mind, schindlers_list, bridge_terabithia,
          les_miserables, harry_potter] fresh_tomatoe.open_movies_page(movies)
