# question 1

number = 1

while number <= 10:
    print(number)
    number += 1

# question 2

confirmation = ""

while confirmation != "yes":
    confirmation = input("Please enter 'yes' to confirm your food order: ")

print("Order confirmed!")

# question 3

prices = [250, 300, 200, 400, 150]

subtotal = 0
i = 0

while i < len(prices):
    subtotal += prices[i]

    if subtotal > 1000:
        break

    i += 1

print("Subtotal:", subtotal)

# question 4

correct_password = "paytm123"

attempts = 0

while attempts < 3:
    password = input("Enter your password: ")

    if password == correct_password:
        print("Welcome")
        break

    attempts += 1

else:
    print("Access Denied")