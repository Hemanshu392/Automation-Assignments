#question 1

playlist = {
    "song1": {"title": "Kesariya", "artist": "Arijit Singh"},
    "song2": {"title": "Channa Mereya", "artist": "Arijit Singh"},
    "song3": {"title": "Heeriye", "artist": "Jasleen Royal"}
}

print(playlist["song2"]["artist"])

#question 2


insta_profile = {
    "username": "virat_kohli",
    "followers": 270000000,
    "posts": [
        {"caption": "Believe in yourself!", "likes": 50000},
        {"caption": "Keep working hard!", "likes": 75000},
        {"caption": "Enjoy every moment!", "likes": 60000}
    ]
}

print(insta_profile["posts"][0]["caption"])

#question 3


order = {
    'user': 'Amit',
    'items': [
        {'name': 'Pizza', 'qty': 2},
        {'name': 'Burger', 'qty': 1}
    ],
    'total': 450
}

for item in order['items']:
    print("Item:", item['name'], "Quantity:", item['qty'])

#question 4


movies = {
    "RRR": {"genre": "Action", "rating": 8.0},
    "Jawan": {"genre": "Action", "rating": 7.0},
    "3 Idiots": {"genre": "Comedy", "rating": 8.4}
}

def get_movie_rating(movies_dict, movie_name):
    return movies_dict[movie_name]["rating"]

print(get_movie_rating(movies, "RRR"))
print(get_movie_rating(movies, "Jawan"))
print(get_movie_rating(movies, "3 Idiots"))

#question 5


booking = {
    "movie": {
        "name": "Jawan",
        "showtime": "6:30 PM"
    },
    "seats": ["A1", "A2", "A3"],
    "user": {
        "name": "Amit",
        "phone": "9876543210"
    }
}

print("Seat numbers:", booking["seats"])


