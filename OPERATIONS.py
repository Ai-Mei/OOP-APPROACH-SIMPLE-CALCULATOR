class Operation:
    # Addition
    def Addition(self, num_1, num_2):
        answer = num_1 + num_2
        print("\n\033[0;32mThe \033[1;92msum\033[0;32m of the 2 numbers: " , "\033[47m\033[1;30m\033[1;32m", answer , "\033[0m\n")
    
    # Subtraction
    def Subtraction(self, num_1, num_2):
        answer = num_1 - num_2
        print("\033[0;33mThe \033[1;93mdifference\033[0;33m of the 2 numbers: " , "\033[47m\033[1;30m", answer, "\033[0m\n")
    
    # Multiplication
    def Multiplication(self, num_1, num_2):
        answer = num_1 * num_2
        print("\n\033[0;31mThe \033[1;91mproduct\033[0;31m of the 2 numbers: " , "\033[47m\033[1;30m", answer, "\033[0m\n")

    # Division
    def Division(self, num_1, num_2):
        try:
            answer = num_1 / num_2
            print("\n\033[0;35mThe \033[1;95mquotient \033[0;35mof the 2 numbers: " , "\033[47m\033[1;30m", answer,"\033[0m\n")
        except ZeroDivisionError:
            print("\033[0m\033[0;101m\033[1;90m⚠️   Error, the number is divided by 0.\033[0m")
        


   