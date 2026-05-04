import supporting_module

# Introduction
name = input("Hello and welcome to the interactive LED tool, please enter your name: ")

# Opening brief.txt and parsing its paragraphs into a list
with open("brief.txt", "r") as f:
    content = f.read()
paragraphs = content.split("\n\n")

print("To exit the menu press 0")
print("To learn about LEDs press 1")
print("To learn about Ohm's Law press 2")
print("To calculate the appropriate resistor press 3")
# Looping the menu until users are satisfied and press 0 to exit the menu
while True:
    try:
        selection = int(input("> "))
        if selection == 0:
            break
        else:
            print(paragraphs[(selection - 1)])
    except ValueError:
        print("You did not enter an integer. Please try again, or press 0 to exit the menu.")
    except IndexError:
        print("The number you entered was invalid. Please try again, or press 0 to exit the menu.")

circuits = supporting_module.load_circuits("datavalues.json")
score, hints_used = supporting_module.run_quiz(circuits)
print(score)
print(hints_used)
