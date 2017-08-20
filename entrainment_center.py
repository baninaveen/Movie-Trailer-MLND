import fresh_tomatoes
import media

toystory = media.Movie("Toy Story",
                       "A story of a boy and his toys",
                       "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",   	# NOQA
                       "https://www.youtube.com/watch?v=vwyZH85NQC4")

jab_harry_met = media.Movie("Jab Harry Mete",
                            "What you seek is seeking you!",
                            "http://static.koimoi.com/wp-content/new-galleries/2017/06/jab-harry-met-sejal-poster-2.jpg",   	# NOQA
                            "https://www.youtube.com/watch?v=W5MZevEH5Ns")

munna_michael = media.Movie("Munna Michael",
                            "Let's Dance with Munna",
                            "http://t3.gstatic.com/images?q=tbn:ANd9GcRqmVIRCHKPUwMYgjpErn5FJkR0SCC8LwYfR6lNvDzZ9SpagAT6",   	# NOQA
                            "https://www.youtube.com/watch?v=1YOfv5tIGwU")

jagga_jasoos = media.Movie("Jagga Jasoos",
                           "Jasoos is Jaggu",
                           "http://t1.gstatic.com/images?q=tbn:ANd9GcSOAtClswC3b6BsEw_SkKME4ZVjj26h4AAzyYqnbujkFUrixNly",   	# NOQA
                           "https://www.youtube.com/watch?v=YheC-4Qgoro")

half_girlfriend = media.Movie("Half Girlfriend",
                              "Dost se zyada GF se Kaam",
                              "http://t3.gstatic.com/images?q=tbn:ANd9GcQZLHjT1iKZgZ9CPajMAjQA-ihHA8KMenmox_3KIXsNK-9Tu97V",   	# NOQA
                              "https://www.youtube.com/watch?v=KmlBnmyelHI")

maa = media.Movie("Maa",
                  "In House God",
                  "http://t1.gstatic.com/images?q=tbn:ANd9GcSeWYr2LRdlBqbDbB3STdbwHunbi9TyHIQiWm_puXorzMaVs5lv",   	# NOQA
                  "https://www.youtube.com/watch?v=je_4hpfAd1g")

raabta = media.Movie("Raabta",
                     "Everything is connected",
                     "http://t2.gstatic.com/images?q=tbn:ANd9GcRwchuikezYdG9hqmBbwmmr9tdIfH__1xP1huKeeRLmFkQm7cWA",   	# NOQA
                     "https://www.youtube.com/watch?v=YXjYfpqg8Z0")

mubarakan = media.Movie("Mubarakan",
                        "family Movies",
                        "http://t1.gstatic.com/images?q=tbn:ANd9GcT6SDaxZJEgyBhxkA3Py12CAVQBhABucp4aFYv-tjfjv3OU3_7U",   	# NOQA
                        "https://www.youtube.com/watch?v=aYXNMaBQrwU")

transformers = media.Movie("Transformers",
                           "The Last knight",
                           "http://t1.gstatic.com/images?q=tbn:ANd9GcQfKnoR3RsDT6gq3eEHzvH4XCt0Fal6sHiMZ7M98eyTF3ahSAPJ",   	# NOQA
                           "https://www.youtube.com/watch?v=Ua-uPOn5Jj8")

spider_man = media.Movie("Spider Man - Home Coming",
                         "Home Coming",
                         "http://t0.gstatic.com/images?q=tbn:ANd9GcT8W3Fe7DD101g0M7OCalJN9u675sQAJFslGCjvs74PTOfEKt_t",  	 # NOQA
                         "https://www.youtube.com/watch?v=DiTECkLZ8HM")

emoji_movies = media.Movie("Emoji Movies",
                           "An Advanture beyond World",
                           "http://t0.gstatic.com/images?q=tbn:ANd9GcRQc0pj8eAuiJa5K_DX1MeTSWwQCX5mDaBWz8auP38FeUX7NX5V",  	 # NOQA
                           "https://www.youtube.com/watch?v=1SdBMSnWPo8")

fate_furious = media.Movie("The fate of the Furious 2017",
                           "Racing never ends",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BMjMxODI2NDM5Nl5BMl5BanBnXkFtZTgwNjgzOTk1MTI@._V1_SY1000_CR0,0,631,1000_AL_.jpg",  	 # NOQA
                           "https://www.youtube.com/watch?v=J_k1yGJtHgw")
# Initialze Movie Class from Media.py
movies = [toystory, jab_harry_met, jagga_jasoos, munna_michael, half_girlfriend, 	# NOQA
            maa, mubarakan, raabta, transformers, spider_man, emoji_movies, fate_furious] 	# NOQA
fresh_tomatoes.open_movies_page(movies)
