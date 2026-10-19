#question 1

fav_brands = ("Spykar", "Adidas", "Rare Rabbit", "Levi's", "H&M")

print("Second brand:", fav_brands[1])
print("Last brand:", fav_brands[-1])

#question 2

def get_unique_cuisines(restaurants):
    return set(restaurants)


restaurants = ['Italian', 'Chinese', 'Italian', 'Mexican', 'Chinese']

unique_cuisines = get_unique_cuisines(restaurants)

print(unique_cuisines)

#question 3

scores = (120, 85, 150, 200, 85, 120)

count_120 = scores.count(120)

print("Score 120 appears:", count_120, "times")

#question 4

watched_movies = {'RRR', 'Jawan', 'KGF', 'Pathaan'}
trending_movies = {'Jawan', 'Pathaan', 'Animal', 'Salaar'}

trending_watched = watched_movies.intersection(trending_movies)

print("Movies watched that are also trending:", trending_watched)

#question 5

captions = [
    "Loving this day! #happy #instagood #travel",
    "Great trip with friends! #travel #friends #happy",
    "Best memories! #instagood #friends #fun"
]

hashtags = set()

for caption in captions:
    words = caption.split()
    for word in words:
        if word.startswith("#"):
            hashtags.add(word)

print("Unique hashtags:", hashtags)