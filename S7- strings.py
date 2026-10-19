# questions 1

message = "Your Zomato order ID is: ZMT12345. Enjoy your meal!"

order_id = message[25:33]

print(order_id)

# question 2

handle = input("Enter your Instagram handle: ")

username = handle[1:]

print("Username:", username)

# question 3

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

display_name = first_name + " " + last_name

print("Display Name:", display_name)

# question 4

def shorten_title(title):
    if len(title) > 10:
        return title[:10] + "..."
    else:
        return title


product = input("Enter Flipkart product title: ")
print(shorten_title(product))

# question 5

message = "Paytm-Transaction: Rs.500 credited on 2024-06-18"

# Extract transaction amount
amount = message[19:25]

# Extract date
date = message[42:52]

print("Transaction Amount:", amount)
print("Date:", date)