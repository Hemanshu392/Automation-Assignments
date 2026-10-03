# Question 1

name = input("Enter your name: ")
favorite_team = input("Enter your favorite IPL team: ")

print(f"Welcome, {name}! Your favorite team is {favorite_team}.")

# Question 2

order_price = input("Enter the Zomato order price: ")

# Convert string to float
order_price = float(order_price)

# Add 10% delivery fee
delivery_fee = order_price * 0.10
final_bill = order_price + delivery_fee

# Print final bill with two decimal places
print(f"Final bill amount: Rs. {final_bill:.2f}")

# Question 3

wishlist_count = input("Enter your Flipkart wishlist count: ")

# Convert string to integer
wishlist_count = int(wishlist_count)

# Format the count
if wishlist_count > 1000:
    formatted_count = f"{wishlist_count / 1000:.1f}K"
else:
    formatted_count = f"{wishlist_count}"

print(f"Wishlist count: {formatted_count}")

# Question 4 - WhatsApp-style message

print("Hemanshu:\tHi! How are you?\nFriend:\t\tI'm good! What about you?\nHemanshu:\tI'm doing great!\nFriend:\t\tThat's nice to hear! 😊")

# Question 5

name = "Aryan"
score = 97

print(f"Congrats {name}, your score is {score}!")