#quesion 1


def calculate_discounted_price(price, discount_percent):
    discount_amount = price * discount_percent / 100
    final_price = price - discount_amount
    return final_price

result = calculate_discounted_price(999, 20)
print("Final price =", result)

#question 2


def format_follower_count(count):
    if count >= 1000000:
        return str(round(count / 1000000, 1)) + "M"
    elif count >= 1000:
        return str(round(count / 1000, 1)) + "K"
    else:
        return str(count)

print(format_follower_count(950))
print(format_follower_count(1500))
print(format_follower_count(1200000))

#question 3


songs = [
    ("Kesariya", 3.5),
    ("Tum Hi Ho", 4.5),
    ("Heeriye", 3.8),
    ("Channa Mereya", 4.2),
    ("Apna Bana Le", 3.9)
]

filtered_songs = list(filter(lambda song: song[1] <= 4, songs))

print(filtered_songs)

#question 4


def apply_coupon(order_total, coupon_code=None):
    if coupon_code == "SAVE10":
        return order_total - (order_total * 10 / 100)
    else:
        return order_total

print(apply_coupon(1000, "SAVE10"))
print(apply_coupon(1000))
print(apply_coupon(1000, "INVALID"))

#question 5


users = [120, 340, 560, 80]

new_points = list(map(lambda points: points + 100, users))

print(new_points)

