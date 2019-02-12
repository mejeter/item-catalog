from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Genre, Movie

engine = create_engine('sqlite:///movies.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()


user1 = User(id=1000,
             username="jetemeg123",
             email="jetemeg123@gmail.com")
session.add(user1)
session.commit()


genre1 = Genre(id=1, user_id=1000, name="Drama")
session.add(genre1)
session.commit()

movie1 = Movie(id=1,
                user_id=1000,
                genre_id=1,
                title="Forrest Gump",
                year="1994",
                rating="PG-13",
                plot_summary="Several historical events are retold and"
                " reimagined through the life of one man.",
                poster_image="https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg")  # NOQA
session.add(movie1)
session.commit()

movie2 = Movie(id=2,
                user_id=1000,
                genre_id=1,
                title="Moonlight",
                year="2016",
                rating="R",
                plot_summary="The coming-of-age story of a black, gay man"
                " growing up in Miami, told in three chapters.",
                poster_image="https://upload.wikimedia.org/wikipedia/en/8/84/Moonlight_%282016_film%29.png")  # NOQA
session.add(movie2)
session.commit()

movie3 = Movie(id=3,
                user_id=1000,
                genre_id=1,
                title="Spotlight",
                year="2015",
                rating="R",
                plot_summary="The true story of The Boston Globe's discovery"
                " of the child molestation cover-up by the Catholic Church.",
                poster_image="https://upload.wikimedia.org/wikipedia/en/f/f3/Spotlight_%28film%29_poster.jpg")  # NOQA
session.add(movie3)
session.commit()

movie4 = Movie(id=4,
                user_id=1000,
                genre_id=1,
                title="Creed",
                year="2015",
                rating="PG-13",
                plot_summary="The son of Apollo Creed has a lot to prove"
                " when he wants to be a professional boxer.",
                poster_image="https://upload.wikimedia.org/wikipedia/en/2/24/Creed_poster.jpg")  # NOQA
session.add(movie4)
session.commit()

movie5 = Movie(id=5,
                user_id=1000,
                genre_id=1,
                title="Arrival",
                year="2016",
                rating="PG-13",
                plot_summary="A linguist must figure out how to communicate"
                " with the aliens that have just arrived on Earth.",
                poster_image="https://upload.wikimedia.org/wikipedia/en/d/df/Arrival%2C_Movie_Poster.jpg")  # NOQA
session.add(movie5)
session.commit()

movie6 = Movie(id=6,
                user_id=1000,
                genre_id=1,
                title="Selma",
                year="2014",
                rating="PG-13",
                plot_summary="A chronicle of the march for voting rights"
                " in 1965 led by Martin Luther King, Jr. from Selma to"
                "Montgomery, Alabama.",
                poster_image="https://upload.wikimedia.org/wikipedia/en/8/8f/Selma_poster.jpg")  # NOQA
session.add(movie6)
session.commit()

movie7 = Movie(id=7,
                user_id=1000,
                genre_id=1,
                title="The Truman Show",
                year="1998",
                rating="PG",
                plot_summary="A man's seemingly boring life is actually a"
                " reality TV show watched by millions of people.",
                poster_image="https://upload.wikimedia.org/wikipedia/en/c/cd/Trumanshow.jpg")  # NOQA
session.add(movie7)
session.commit()


genre2 = Genre(id=2, user_id=1000, name="Comedy")
session.add(genre2)
session.commit()

movie8 = Movie(id=8,
                user_id=1000,
                genre_id=2,
                title="Girls Trip",
                year="2017",
                rating="R",
                plot_summary="Four friends reconnect for a wild trip to the"
                " Essence Festival in New Orleans.",
                poster_image="https://upload.wikimedia.org/wikipedia/en/f/f4/Girls_Trip_film_poster.png")  # NOQA
session.add(movie8)
session.commit()

movie9 = Movie(id=9,
                user_id=1000,
                genre_id=2,
                title="Bridesmaids",
                year="2011",
                rating="R",
                plot_summary="The maid of honor is a mess, but is still"
                " determined to get through her duties until her best friend's"
                " wedding day.",
                poster_image="https://upload.wikimedia.org/wikipedia/en/d/df/BridesmaidsPoster.jpg")  # NOQA
session.add(movie9)
session.commit()

movie10 = Movie(id=10,
                user_id=1000,
                genre_id=2,
                title="Hitch",
                rating="PG-13",
                plot_summary="A date doctor meets his match when he pursues"
                " a cynical gossip columnist.",
                poster_image="https://upload.wikimedia.org/wikipedia/en/d/d4/Hitch_poster.JPG")  # NOQA
session.add(movie10)
session.commit()

movie11 = Movie(id=11,
                user_id=1000,
                genre_id=2,
                title="Game Night",
                year="2018",
                rating="R",
                plot_summary="Game night takes a turn for a group of friends"
                " when one of them is kidnapped.",
                poster_image="https://upload.wikimedia.org/wikipedia/en/a/a4/Game_Night_%28film%29.png")  # NOQA
session.add(movie11)
session.commit()

movie12 = Movie(id=12,
                user_id=1000,
                genre_id=2,
                title="Mean Girls",
                year="2004",
                rating="PG-13",
                plot_summary="A home-schooled teen must navigate the social"
                " atmosphere of a suburban high school in America.",
                poster_image="https://upload.wikimedia.org/wikipedia/en/a/ac/Mean_Girls_film_poster.png")  # NOQA
session.add(movie12)
session.commit()

movie13 = Movie(id=13,
                user_id=1000,
                genre_id=2,
                title="The Proposal",
                year="2009",
                rating="PG-13",
                plot_summary="Faced with deportation, an editor-in-chief"
                " coerces her assistant into faking an engagement.",
                poster_image="https://upload.wikimedia.org/wikipedia/en/0/02/The_Proposal.jpg")  # NOQA
session.add(movie13)
session.commit()

movie14 = Movie(id=14,
                user_id=1000,
                genre_id=2,
                title="Friday",
                year="1995",
                rating="R",
                plot_summary="Craig and his friend Smokey must repay a drug"
                " dealer the $200 they owe by the end of the day.",
                poster_image="https://upload.wikimedia.org/wikipedia/en/2/27/Fridayposter1995.jpg")  # NOQA
session.add(movie14)
session.commit()


genre3 = Genre(id=3, user_id=1000, name="Action")
session.add(genre3)
session.commit()

movie15 = Movie(id=15,
                user_id=1000,
                genre_id=3,
                title="Black Panther",
                year="2018",
                rating="PG-13",
                plot_summary="A new king must defend his technologically"
                " advanced nation from outside threats.",
                poster_image="https://upload.wikimedia.org/wikipedia/en/0/0c/Black_Panther_film_poster.jpg")  # NOQA
session.add(movie15)
session.commit()

movie16 = Movie(id=16,
                user_id=1000,
                genre_id=3,
                title="The Dark Knight",
                year="2008",
                rating="PG-13",
                plot_summary="When the Joker incites chaos in Gotham, Batman"
                " must stop him at any cost.",
                poster_image="https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg")  # NOQA
session.add(movie16)
session.commit()

movie17 = Movie(id=17,
                user_id=1000,
                genre_id=3,
                title="Thor: Ragnarok",
                year="2017",
                rating="PG-13",
                plot_summary="Thor must escape from prison on another planet"
                " in order to save Asgard from his long-lost sister.",
                poster_image="https://upload.wikimedia.org/wikipedia/en/7/7d/Thor_Ragnarok_poster.jpg")  # NOQA
session.add(movie17)
session.commit()

movie18 = Movie(id=18,
                user_id=1000,
                genre_id=3,
                title="Guardians of the Galaxy",
                year="2014",
                rating="PG-13",
                plot_summary="A ragtag group must join forces to save the"
                " galaxy from a manical villian.",
                poster_image="https://upload.wikimedia.org/wikipedia/en/b/b5/Guardians_of_the_Galaxy_poster.jpg")  # NOQA
session.add(movie18)
session.commit()

movie19 = Movie(id=19,
                user_id=1000,
                genre_id=3,
                title="Avengers",
                year="2012",
                rating="PG-13",
                plot_summary="Iron Man, Captain America, Thor, Hulk, Black"
                " Widow, and Hawkeye team up in order to stop Loki from"
                " controlling humanity.",
                poster_image="https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg")  # NOQA
session.add(movie19)
session.commit()

movie20 = Movie(id=20,
                user_id=1000,
                genre_id=3,
                title="Wonder Woman",
                year="2017",
                rating="PG-13",
                plot_summary="The Amazonian princess leaves her home to"
                " fight during World War I and stop her nemesis, Ares.",
                poster_image="https://upload.wikimedia.org/wikipedia/en/e/ed/Wonder_Woman_%282017_film%29.jpg")  # NOQA
session.add(movie20)
session.commit()


genre4 = Genre(id=4, user_id=1000, name="Animation")
session.add(genre4)
session.commit()

movie21 = Movie(id=21,
                user_id=1000,
                genre_id=4,
                title="The Lion King",
                year="1994",
                rating="G",
                plot_summary="A lion returns from self-exile to take back"
                " his late father's throne from his father's killer.",
                poster_image="https://upload.wikimedia.org/wikipedia/en/3/3d/The_Lion_King_poster.jpg")  # NOQA
session.add(movie21)
session.commit()

movie22 = Movie(id=22,
                user_id=1000,
                genre_id=4,
                title="Mulan",
                year="1998",
                rating="G",
                plot_summary="A woman disguises herself as a male warrior to"
                " fill in for her ailing father and saves China.",
                poster_image="https://upload.wikimedia.org/wikipedia/en/a/a3/Movie_poster_mulan.JPG")  # NOQA
session.add(movie22)
session.commit()

movie23 = Movie(id=23,
                user_id=1000,
                genre_id=4,
                title="Shrek",
                year="2001",
                rating="PG",
                plot_summary="An ogre agrees to save a princess as payment"
                " for getting his land back from an evil ruler.",
                poster_image="https://upload.wikimedia.org/wikipedia/en/3/39/Shrek.jpg")  # NOQA
session.add(movie23)
session.commit()

movie24 = Movie(id=24,
                user_id=1000,
                genre_id=4,
                title="Up",
                year="2009",
                rating="PG",
                plot_summary="An old widower goes on the adventure to South"
                " America that he and his late wife had always planned.",
                poster_image="https://upload.wikimedia.org/wikipedia/en/0/05/Up_%282009_film%29.jpg")  # NOQA
session.add(movie24)
session.commit()

movie25 = Movie(id=25,
                user_id=1000,
                genre_id=4,
                title="Toy Story",
                year="1995",
                rating="G",
                plot_summary="An old cowboy toy and a new astronaut toy are"
                " rivals that work together to be reunited with their owner.",
                poster_image="https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg")  # NOQA
session.add(movie25)
session.commit()

movie26 = Movie(id=26,
                user_id=1000,
                genre_id=4,
                title="Zootopia",
                year="2016",
                rating="PG",
                plot_summary="A rabbit cop and a clever fox stumble upon a"
                " conspiracy while looking for a missing animal.",
                poster_image="https://upload.wikimedia.org/wikipedia/en/9/96/Zootopia_%28movie_poster%29.jpg")  # NOQA
session.add(movie26)
session.commit()

movie27 = Movie(id=27,
                user_id=1000,
                genre_id=4,
                title="Coco",
                year="2017",
                rating="PG",
                plot_summary="After aspiring musician Miguel accidentally"
                " enters the Land of the Dead, he decides to search for his"
                " famous ancestor.",
                poster_image="https://upload.wikimedia.org/wikipedia/en/9/98/Coco_%282017_film%29_poster.jpg")  # NOQA
session.add(movie27)
session.commit()


genre5 = Genre(id=5, user_id=1000, name="Thriller")
session.add(genre5)
session.commit()

movie28 = Movie(id=28,
                user_id=1000,
                genre_id=5,
                title="Get Out",
                year="2017",
                rating="R",
                plot_summary="A black man meets his white girlfriend's"
                " family and encounters strange behavior.",
                poster_image="https://upload.wikimedia.org/wikipedia/en/a/a3/Get_Out_poster.png")  # NOQA
session.add(movie28)
session.commit()

movie29 = Movie(id=29,
                user_id=1000,
                genre_id=5,
                title="Silence of the Lambs",
                year="1991",
                rating="R",
                plot_summary="An FBI trainee interviews an imprisoned"
                " cannibalistic serial killer to catch a serial killer that"
                " skins his victims.",
                poster_image="https://upload.wikimedia.org/wikipedia/en/8/86/The_Silence_of_the_Lambs_poster.jpg")  # NOQA
session.add(movie29)
session.commit()

movie30 = Movie(id=30,
                user_id=1000,
                genre_id=5,
                title="The Sixth Sense",
                year="1999",
                rating="PG-13",
                plot_summary="A child psychologist attempts to help a boy"
                " who can communicate with ghosts.",
                poster_image="https://upload.wikimedia.org/wikipedia/en/a/a4/The_Sixth_Sense_poster.png")  # NOQA
session.add(movie30)
session.commit()

movie31 = Movie(id=31,
                user_id=1000,
                genre_id=5,
                title="The Quiet Place",
                year="2018",
                rating="PG-13",
                plot_summary="A family must live in silence to avoid being"
                " killed by creatures that hunt by sound.",
                poster_image="https://upload.wikimedia.org/wikipedia/en/a/a0/A_Quiet_Place_film_poster.png")  # NOQA
session.add(movie31)
session.commit()

movie32 = Movie(id=32,
                user_id=1000,
                genre_id=5,
                title="Misery",
                year="1990",
                rating="R",
                plot_summary="A crazed fan holds her favorite author hostage"
                " after a car accident and forces him to write a new novel.",
                poster_image="https://upload.wikimedia.org/wikipedia/en/5/52/Misery_%281990_film_poster%29.png")  # NOQA
session.add(movie32)
session.commit()


print "added movie titles!"
