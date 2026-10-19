#question 1

def is_valid_email(email):
    if email.count("@") != 1:
        return False

    if "." not in email:
        return False

    if email.startswith("@") or email.endswith("@"):
        return False

    return True


email = input("Enter your email: ")
print(is_valid_email(email))

#question 2

def validate_username(username):
    if len(username) < 6:
        return False

    if not username.isalnum():
        return False

    if username[0].isdigit():
        return False

    return True


username = input("Enter username: ")
print(validate_username(username))

#question 3

def check_password_strength(password):
    if len(password) < 6:
        return "Weak"

    has_letter = any(char.isalpha() for char in password)
    has_number = any(char.isdigit() for char in password)
    special_chars = "!@#$%^&*"
    has_special = any(char in special_chars for char in password)

    if has_letter and has_number and has_special:
        return "Strong"
    elif has_letter and has_number:
        return "Medium"
    else:
        return "Weak"


password = input("Enter your password: ")
print(check_password_strength(password))

#question 4

def validate_username(username):
    if len(username) < 6:
        return False

    if not username.isalnum():
        return False

    if username[0].isdigit():
        return False

    return True


def filter_invalid_usernames(usernames):
    valid_usernames = []

    for username in usernames:
        if validate_username(username):
            valid_usernames.append(username)

    return valid_usernames


usernames = ["Hemanshu123", "123abc", "cool_user", "Priya99", "abc"]

print(filter_invalid_usernames(usernames))

#question 5

def is_valid_indian_phone(number):
    return len(number) == 10 and number.isdigit() and number[0] in "6789"


# Test cases
print(is_valid_indian_phone("9876543210"))
print(is_valid_indian_phone("5123456789"))
print(is_valid_indian_phone("98765abc10"))
