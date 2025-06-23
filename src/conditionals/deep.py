number = str(input())


def deep():
    if number == "42":
        print("Yes")
    elif number == "Forty Two":
        print("Yes")
    elif number == "forty-two":
        print("Yes")
    else:
        print("No")


deep()
