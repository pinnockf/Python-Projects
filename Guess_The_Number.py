import random
import sys

# ===================================   
# Functions
# =================================== 

def prompt_header():
    """" Returns a string containing the program info """
    program_info = ('Guess The Number'
                    '\nAuthor: Franklin Pinnock'
                    '\nLanguage: Python 3.4'
                    '\nVersion: 1.0')
    return program_info

def prompt_start():
    """returns a string containing the start prompt"""
    start_string = ("\nI am thinking of a number." 
                     "\nLet's see if you can guess what it is!")
    return start_string

def is_number(input_string):
    """Checks to see if input is a valid integer
       Returns integer converted from input"""
    try:
       val = int(input_string)
       return val
    except ValueError:
       return False   

def in_range(n,start,end):
    if n < start or n > end:
        return False
    else:
        return True   
    
def prompt_menu():
    """Return an integer indicating the level of difficulty"""
    while True:
        menu_string = ("\nPlease enter the number associated "
                            "with that level of difficulty."
                            "\n1) Range 1-10"
                            "\n2) Range 1-100"
                            "\n3) Range 1-1000")
        print(menu_string)
        user_choice = is_number(input("\nYour choice: "))
        if user_choice == False:
            print("That was not an integer. Try again.") 
            continue
        user_range = in_range(user_choice,1,3)
        if user_range == False:
            print("That is not a choice. Try again")
            continue

        if user_choice == 1:
            max_endpoint = 10
        elif user_choice == 2:
            max_endpoint = 100
        elif user_choice == 3:
            max_endpoint = 1000
            
        return max_endpoint
 
# ===================================   
# Code Segment
# ===================================  
#Display program info                   
print(prompt_header())

#Display opening prompt
print(prompt_start())

#Display menu prompt
max_endpoint = prompt_menu()

#Generate random number
random_number = random.randint(1,max_endpoint)

#Enable Hints?
hints_msg = ("\nPress the 'y' key at this point to enable hints, "
              "any other key will proceed as normal")
print(hints_msg)
hints_enabled = input("\nEnable Hints?: ")
if hints_enabled == 'y':
    hints_enabled = True

#Take input and check if its a number
while True:
    print("\nPlease enter a number from 1-" + str(max_endpoint) + ".")
    user_guess = input("You chose: ")
    if is_number(user_guess) == False:
        print("Please enter a valid integer. Try again.")
        continue
    user_guess = int(user_guess)
    if user_guess < 1 or user_guess > max_endpoint:
        print("That number is not within the given range. Try again ")
        continue
    if user_guess != random_number:
        if hints_enabled == True and user_guess < random_number:
            print("Your guess was too low. Try again. XD")
        elif hints_enabled == True and user_guess > random_number:
            print("Your guess was too high. Try again. XD")
        else:
            print("Sorry, you guessed the wrong number. Try again.")  
        continue
    print("\nCongratulations! You guessed the right number."
          "\nThanks for playing. :D")
    break

sys.exit()