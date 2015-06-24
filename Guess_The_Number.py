import random
import sys

def prompt_header():
    """" Shows prompt header when program starts """
    program_info = ('Guess The Number'
                    '\nAuthor: Franklin Pinnock'
                    '\nLanguage: Python 3.4'
                    '\nVersion: 1.0')
    return program_info

def prompt_start():
    """Shows the beginning prompt"""
    prompt_string = ("\nI am thinking of a number from 1-10." 
                     "\nLet's see if you can guess what it is!")
    return prompt_string

def is_number(val):
    """Checks to see if val is a valid integer"""
    try:
       val = int(userInput)
    except ValueError:
       print("That's not an int!") 
       
===================================   
Code Segment
===================================  
     
#Display program info                   
print(prompt_header())

#Display opening prompt
print(prompt_start())

#Take input and check if its a number
number = int(input("Please enter a number from 1-10"))

guess_number = 


sys.exit()



