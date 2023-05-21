class UserInterface:
    def UserInput(self):
        while True:
            number = input("Enter a number: ")
            try:
                number = float(number)
                if number.is_integer():
                    number = int(number)
                break
            except ValueError:
                print("⚠️ Invalid input. Please enter a valid number.")
                continue
        return number

# Asks input from user.

# Converts the input to float.
# Ask for operation.
# Prints results.
# Asks the user to either repeat the program.