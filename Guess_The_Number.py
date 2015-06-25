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
    start_string = ("\nI am thinking of a number from 1-10." 
                     "\nLet's see if you can guess what it is!")
    return start_string

def is_number(input_string):
    """Checks to see if argument is a valid integer"""
    try:
       val = int(input_string)
       return True
    except ValueError:
       print("That was not an integer. Try again.") 
       return []   
    
    
def prompt_menu():
    """Return an integer indicating the level of difficulty"""
    menu_string = ("\nPlease enter the number associated"
                   "with the level of difficulty you wish to use."
                   "\n1) Range 1-10"
                   "\n2) Range 1-100"
                   "\n3) Range 1-1000")
    max_endpoint = input(menu_string)
  
    return max_endpoint
 

       
# ===================================   
# Code Segment
# ===================================  
     
#Display program info                   
print(prompt_header())

#Display opening prompt
print(prompt_start())

#Generate random number
n = 10
random_number = random.randint(1,n)

#Take input and check if its a number
while True:
    user_guess = input("\nPlease enter a number from 1-10: ")
    if is_number(user_guess) == True:
        user_guess = int(user_guess)
        if user_guess >= 1 and user_guess <= n:
            if user_guess == random_number:
                print("Congratulations! You guessed the right number.")
                break
            else:
                print("Sorry. Guess again.")
        else:
            print("That number is not within the given range. Try again ")
    
        




sys.exit()



