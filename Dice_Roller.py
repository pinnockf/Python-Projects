import random

def prompt():
    """" Shows prompt on screen """
    program_info = ('Dice Rolling Program\n'
                    'Author: Franklin Pinnock\n'
                    'Language: Python 3.4\n'
                    'Version: 1.0\n')
    print(program_info)

#Display program info                   
prompt()

#Prompt user to enter number of die to roll.
num_of_dice = int(input("How many dice do you want to roll? "))

#Prompt user to enter number of sides that a dice has.
num_of_sides = int(input("How many sides does each die have? "))
#Print results
print("\nRolling", num_of_dice, "die, "
      "with", num_of_sides, "sides, "
      "gives the following result:")
#Set Loop Condition
roll_again = True
while roll_again == True:
    for x in range(num_of_dice):
        #Roll the dice and display them onto the screen.
        random_number = random.randint(1,num_of_sides)
        print('\nDice',x+1,':'
              ,random_number)
       
    choice = input("\nDo you want to roll again? "
          "Enter y for yes, any other key will terminate program. ")
    #If user enters 'y', dice will roll again
    if choice != 'y':
        roll_again = False
        print("\nThank You")
 
        




