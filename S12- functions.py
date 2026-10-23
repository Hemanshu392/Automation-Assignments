#question 1


def get_total_price(price, quantity):
    return price * quantity

result = get_total_price(299, 3)
print("Total amount =", result)

#question 2


def format_follower_count(number):
    if number >= 1000000:
        return str(round(number / 1000000, 1)) + "M"
    elif number >= 1000:
        return str(round(number / 1000, 1)) + "K"
    else:
        return str(number)

print(format_follower_count(950))
print(format_follower_count(1500))
print(format_follower_count(1200000))


#question 3


def get_discounted_price(price, discount):
    discount_amount = price * discount / 100
    final_price = price - discount_amount
    return final_price

result = get_discounted_price(999, 20)
print("Final price =", result)

#question 4


ratings = [4.5, 3.8, 5.0, 4.2]

def average_rating(ratings):
    average = sum(ratings) / len(ratings)
    return round(average, 1)

result = average_rating(ratings)
print("Average rating =", result)

#question 5


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

for i in range(1, 21):
    if is_even(i):
        print(i)

