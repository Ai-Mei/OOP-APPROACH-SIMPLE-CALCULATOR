from OPERATIONS import Operation
operation = Operation

class UserInterface:
    # Asks input from user.
    def UserInput(self):
        while True:
            number = input("Enter a number: ")
            # Converts the input to float.
            try:
                number = float(number)
                if number.is_integer():
                    number = int(number)
                break
            except ValueError:
                print("⚠️ Invalid input. Please enter a valid number.")
                continue
        return number

    # Ask for operation.
    def OperationChoice(self):
        operation = input("Please select an operation to perform + for addition, - for subtraction, * for multiplication, / for division: ")
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
                print("⚠️ Invalid operation selected.")
                operation_choice = self.OperationChoice()

    # Asks the user to either repeat the program.