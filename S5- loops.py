# question 1

apps = ['Zomato', 'Swiggy', 'Flipkart', 'Myntra']

for app in apps:
    print(app)

# question 2

for i in range(2, 21, 2):
    print(i)

# question 3

scores = [45, 67, 23, 89, 100]

total = 0

for score in scores:
    total += score

print("Total score:", total)

# question 4

name = input("Enter your name: ")

for i in range(5):
    print("Welcome", name)

# question 5

for i in range(1, 5):
    for j in range(i):
        print("*", end=" ")
    print()