# Question 1

# Declare variables
name = "Hemanshu"
age = 22
city = "Ahmedabad"
favorite_food = "Pizza"
spotify_subscription = True

# Print values and data types
print("Name:", name, "| Data type:", type(name))
print("Age:", age, "| Data type:", type(age))
print("City:", city, "| Data type:", type(city))
print("Favorite Food:", favorite_food, "| Data type:", type(favorite_food))
print("Spotify Subscription:", spotify_subscription, "| Data type:", type(spotify_subscription))

# Question 2

# Zomato Order Summary

restaurant_name = "Pizza Palace"
item_count = 3
total_price = 450.5
is_veg = True
delivery_time_minutes = 30

# Print order summary
print(
    f"Ordered {item_count} items from {restaurant_name}. "
    f"Total: ₹{total_price}. Veg: {is_veg}. "
    f"Delivery in {delivery_time_minutes} min."
)

# Question 3

# Get YouTube channel details from the user

followers = int(input("Enter the number of followers: "))
posts = int(input("Enter the number of posts: "))

# Print the result
print(f"You have {followers} followers and {posts} posts.")

# Question 4

product_price = '499'
discount = 50
is_flash_sale = 'True'

# Convert to correct data types
product_price = int(product_price)
is_flash_sale = bool(is_flash_sale)

# Calculate final price
final_price = product_price - discount

# Print the result
print("Product price:", product_price)
print("Discount:", discount)
print("Flash sale:", is_flash_sale)
print("Final price:", final_price)