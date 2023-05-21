class Operation:
    # Addition
    def Addition(self, num_1, num_2):
        answer = num_1 + num_2
        print("The sum of the two numbers:", answer)
    
    # Subtraction
    def Subtraction(self, num_1, num_2):
        answer = num_1 - num_2
        print("The difference of the two numbers:", answer)
    
    # Multiplication
    def Multiplication(self, num_1, num_2):
        answer = num_1 * num_2
        print("The product of the two numbers:", answer)

    # Division
    def Division(self, num_1, num_2):
        try:
            answer = num_1 / num_2
            print("The quotient of the two numbers:", answer)
        except ZeroDivisionError:
            print("⚠️ Error, the number is divided by 0.")
        


   