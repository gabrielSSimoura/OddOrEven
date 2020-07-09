# Ask the user for a number.
# Depending on whether the number is even or odd, print out an appropriate message to the user.

def isEven(number):
    if (number % 2 == 0):
        return 1
    else:
        return 0


def main():
    userNumber = int(input("Type a number: "))
    userNumber = isEven(userNumber)

    if(userNumber):
        print("Your number is Even")

    else:
        print("Your number is Odd")

    return 0


main()
