# question 1

likes = int(input("Enter the number of likes: "))
comments = int(input("Enter the number of comments: "))

if likes > 1000 and comments > 100:
    print("Trending")
else:
    print("Not Trending")

# question 2

price = float(input("Enter the original price: "))
discount = float(input("Enter the discount percentage: "))

discount_amount = price * discount / 100
final_price = price - discount_amount

print("Final price after discount:", final_price)

# question 3

total_amount = float(input("Enter the order total: "))

if total_amount >= 299:
    print("Free Delivery")
else:
    print("Delivery Charges Apply")

# question 4

balance = float(input("Enter your Paytm wallet balance: "))
amount = float(input("Enter the payment amount: "))

if balance >= amount:
    print("Payment Successful")
else:
    print("Insufficient Balance")

# question 5

runs = int(input("Enter the player's runs: "))
strike_rate = float(input("Enter the strike rate: "))

if runs > 50 and strike_rate > 120:
    print("Excellent")
elif runs > 30 and strike_rate > 100:
    print("Good")
else:
    print("Needs Improvement")
