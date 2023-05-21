#import the two classes.
from USERINTERFACE import UserInterface
from OPERATIONS import Operation

ui = UserInterface()
operation = Operation()

ui.Introduction()
while True:
    # Ask the user for 2 innput numbers.
    num_1 = ui.UserInput()
    num_2 = ui.UserInput()

    # Ask the user for operation to perform.
    operation_choice = ui.OperationChoice()

    # Loading
    ui.Loading()
    # Prints result.
    ui.Result(num_1, num_2, operation_choice, operation)

    # Ask the user if they want to use calculator again.
    if not ui.Repeat():
        break
