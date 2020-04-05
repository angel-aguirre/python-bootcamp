import random
import os

def number_shape(num=0):
    """
    Function that returns the dice shape according to the given number.
    """
    if num == 1:
        print( 
        """
        ___________
        |         |
        |         |
        |    o    |
        |         |
        |         |
        ▔▔▔▔▔▔▔▔▔▔▔
        """
        )
    if num == 2:
        print( 
        """
        ___________
        |         |
        |  o      |
        |         |
        |      o  |
        |         |
        ▔▔▔▔▔▔▔▔▔▔▔
        """
        )
    if num == 3:
        print( 
        """
        ___________
        |         |
        |  o      |
        |    o    |
        |      o  |
        |         |
        ▔▔▔▔▔▔▔▔▔▔▔
        """
        )
    if num == 4:
        print( 
        """
        ___________
        |         |
        |  o   o  |
        |         |
        |  o   o  |
        |         |
        ▔▔▔▔▔▔▔▔▔▔▔
        """
        )
    if num == 5:
        print( 
        """
        ___________
        |         |
        |  o   o  |
        |    o    |
        |  o   o  |
        |         |
        ▔▔▔▔▔▔▔▔▔▔▔
        """
        )
    if num == 6:
        print( 
        """
        ___________
        |         |
        |  o   o  |
        |  o   o  |
        |  o   o  |
        |         |
        ▔▔▔▔▔▔▔▔▔▔▔
        """
        )

# We define a variable for the user choice
choice = 'Y'

while choice.lower() == 'y':
    # Generating a random number between 1 and 6
    num = random.randint(1, 6)

    # We clear the console
    os.system("clear")
    print("Let's roll it!")
    number_shape(num)
    choice = input("Roll it again? Y/N: ")

