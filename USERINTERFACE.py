from OPERATIONS import Operation
operation = Operation
import pyfiglet

class UserInterface:
    def Introduction(self):
        banner = pyfiglet.figlet_format("    My Calculator", font="serifcap", justify="center")
        print("\033[0;32m+ \033[0;33m- \033[0;31mx \033[0;35m÷ " * 12)
        print(banner)
        print("\033[0;32m+ \033[0;33m- \033[0;31mx \033[0;35m÷ " * 12)
        print()
        print("\033[0;31m       ∧,,,∧   ~       ┏━━━━━━━━┓".center(90))
        print("    (  ̳• · • ̳)   ~ ♡  My Calculator  ♡".center(90))
        print("/       づ  ~      ┗━━━━━━━━┛\033[0m".center(90))
        

        print("\033[0;33mWelcome to \033[1;34mMy Calculator\033[0;33m.This is a simple calculator.".center(120))
        print("                    This calculator can perform 4 operations (\033[1;32m+\033[0;33m, \033[1;33m-\033[0;33m, \033[1;31mx\033[0;33m, and \033[1;35m/\033[0m).".center(90))
        print()
        print("\033[0;32m+ \033[0;33m- \033[0;31mx \033[0;35m÷ " * 12)
        print()
    # Asks input from user.
    def UserInput(self):
        while True:
            number = input("\033[0m\033[1;33mEnter a number: \033[4;37m")
            # Converts the input to float.
            try:
                number = float(number)
                if number.is_integer():
                    number = int(number)
                break
            except ValueError:
                print("\033[0m\033[0;101m\033[1;90m⚠️   Invalid input. Please enter a valid number.\033[0m")
                continue
        return number

    # Ask for operation.
    def OperationChoice(self):
        operation = input("\033[0m\033[1;34mPlease select an operation to perform: \033[0;32m+\033[1;34m for \033[4;32maddition \033[0m\033[1;34m, \033[0;33m-\033[1;34m for \033[4;33msubtraction\033[0m\033[1;34m, \033[0;31m*\033[1;34m for \033[4;31mmultiplication\033[0m\033[1;34m, \033[0;35m/\033[1;34m for \033[4;35mdivision\033[0m\033[1;34m: \033[4;37m")
        return operation
    
    # Prints results.
    def Result(self, num_1, num_2, operation_choice, operation):
        while True:
            if operation_choice == "+":
                result = operation.Addition(num_1, num_2)
                break
            elif operation_choice == "-":
                result = operation.Subtraction(num_1, num_2)
                break
            elif operation_choice == "*":
                result = operation.Multiplication(num_1, num_2)
                break
            elif operation_choice == "/":
                result = operation.Division(num_1, num_2)
                break
            else:
                print("\033[0m\033[0;101m\033[1;90m⚠️   Invalid operation selected.\033[0m")
                operation_choice = self.OperationChoice()

    # Asks the user to either repeat the program.
    def Repeat(self):
        while True:
            decision = input("Do you want to do more calculations? Type Yes or No: ")
            if decision.lower() == "yes":
                return True
                break
            if decision.lower() == "no":
                print("Process done, thank you for using My Calculator.")
                return False
                break
            else:
                print("⚠️ Please type in only Yes or No.")
                continue
