# Introduction
name = input("Hello and welcome to the interactive LED tool, please enter your name: ")

with open("brief.txt", "r") as f:
    content = f.read()
paragraphs = content.split("\n\n")

while True:
    try:
        print("To exit the menu press 0")
        print("To learn about LEDs press 1")
        print("To learn about Ohm's Law press 2")
        selection = int(input("To calculate the appropriate resistor press 3\n> "))
        if selection == 0:
            break
        else:
            print(paragraphs[(selection - 1)])
    except ValueError:
        print("You did not enter an integer. Please try again, or press 0 to exit the menu.")
    except IndexError:
        print("The number you entered was invalid. Please try again, or press 0 to exit the menu.")

