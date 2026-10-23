#question 1


def add_numbers(a, b):
    return a + b


def multiply_numbers(a, b):
    return a * b

#from math_helpers import add_numbers, multiply_numbers


# Duration of two songs in minutes
song1_duration = 4
song2_duration = 3

# Play counts of two songs
song1_plays = 100
song2_plays = 200

# Calculate total duration
total_duration = add_numbers(song1_duration, song2_duration)

# Calculate product of play counts
total_plays_product = multiply_numbers(song1_plays, song2_plays)

print("Total duration of two songs:", total_duration, "minutes")
print("Product of play counts:", total_plays_product)

#question 2


def apply_bw_filter(image_name):
    print("Black and white filter applied to:", image_name)


def add_story(username, image_name):
    print(username, "added a story with image:", image_name)


#from insta_utils.filters import apply_bw_filter
#from insta_utils.stories import add_story

# Apply black and white filter
apply_bw_filter("vacation.jpg")

# Add an Instagram story
add_story("hemanshu", "vacation.jpg")

#question 3


import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

if response.status_code == 200:
    posts = response.json()

    for post in posts[:3]:
        print(post["title"])
else:
    print("Failed to fetch data:", response.status_code)


#question 5


import qrcode

upi_link = "upi://pay?pa=demo@upi&pn=TestUser&am=100&cu=INR"

qr_image = qrcode.make(upi_link)

qr_image.save("payment_qr.png")

print("QR code generated successfully!")
print("Saved as payment_qr.png")


