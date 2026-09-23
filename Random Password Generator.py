import random

# Random Password Generator
# by [ATHARV GIRISH]

def make_password(length):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%^&*"

    all_chars = letters + numbers + symbols

    password = ""
    for i in range(length):
        random_char = random.choice(all_chars)
        password = password + random_char

    return password


def check_password(password):
    # just a simple check to see if it has at least one number and one symbol
    has_number = False
    has_symbol = False

    for ch in password:
        if ch in "0123456789":
            has_number = True
        if ch in "!@#$%^&*":
            has_symbol = True

    if has_number and has_symbol:
        return True
    else:
        return False


print("=== Random Password Generator ===")
length = int(input("How long do you want your password to be? "))

if length < 4:
    print("That's too short, try at least 4 characters.")
else:
    my_password = make_password(length)

    # keep generating until it has both a number and symbol
    while check_password(my_password) == False:
        my_password = make_password(length)

    print("Here is your password:", my_password)
    print("Password length:", len(my_password))