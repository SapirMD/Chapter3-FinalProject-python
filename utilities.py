import os

# "error_to_print" is a string - letting the user know which input was incorrect
def isNumber(variable, error_to_print: str) -> bool: 
    if not variable.isdigit():
        print("Error: " + error_to_print + " must be a number. " + variable + " is not a number" + os.linesep)
        return False
    return True


def errorMessage(user_choice: int) -> None:
    print("Error: Option [" + str(user_choice) + "] does not exist. Please try again." + os.linesep)


def handleUserChoice(error_to_print: str, list_len: int = None) -> int:
    user_choice = input("Please enter your choice: ")
    while not isNumber(user_choice, error_to_print):
        user_choice = input("Please enter your choice: ")
    user_choice = int(user_choice)
    if list_len:
        if user_choice > list_len:
            errorMessage(user_choice)
            raise ValueError
    return user_choice
        
