#question 1

playlist = [
    "Tum Hi Ho",
    "Kesariya",
    "Apna Bana Le",
    "Chaleya",
    "Heeriye"
]

print(playlist)

#question 2

def add_to_cart(cart, item):
    cart.append(item)
    return cart


cart = []

cart = add_to_cart(cart, "T-shirt")
cart = add_to_cart(cart, "Shoes")
cart = add_to_cart(cart, "Watch")

print(cart)

#question 3

order_prices = [199, 349, 120, 499, 220]

total_bill = sum(order_prices)

print("Total bill amount:", total_bill)

#question 4

def remove_duplicates(usernames):
    seen = []
    
    for username in usernames:
        if username not in seen:
            seen.append(username)
    
    return seen


usernames = ["virat", "rohit", "virat", "dhoni", "rohit", "hardik"]

result = remove_duplicates(usernames)

print(result)

#question 5

def second_highest(scores):
    unique_scores = list(set(scores))
    unique_scores.sort(reverse=True)
    return unique_scores[1]


scores = [45, 120, 67, 120, 88, 67]

result = second_highest(scores)

print("Second highest score:", result)