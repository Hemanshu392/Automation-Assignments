#question 1


prices = [100, 200, 150, 300, 250]

gst_prices = [price + (price * 18 / 100) for price in prices]

print(gst_prices)

#question 2


usernames = ["amit123", "Virat18", "Anjali", "rahul", "Aryan", "heman"]

filtered_usernames = [name for name in usernames if name.lower().startswith("a")]

print(filtered_usernames)

#question 3


scores = [45, 67, 23, 89, 100, 50, 35]

result = ["Half-century" if score > 50 else "Below Fifty" for score in scores]

print(result)

#question 4


ratings = [
    [5, 4, 2],
    [3, 1, 4],
    [2, 5, 3]
]

filtered_ratings = [rating for sublist in ratings for rating in sublist if rating >= 3]

print(filtered_ratings)

#question 5


products = ["laptop", "Headphones", "mobile", "Keyboard", "mouse", "Monitor"]

result = [name.upper() for name in products if len(name) > 6]

print(result)
