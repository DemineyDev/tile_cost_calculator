# Program calculates the cost of tile for a room of which the user provides the width, length and height and cost of the tiles.
from os import system, name

def clear():                    # Function to clear the screen
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def start_program():               # Function as starting point for the program
    clear()
    print('*********************************************')
    print('*      Welcome to Tile Cost Calculator      *')
    print('*        Please make your selection         *')
    print('*    Press \'1\' to calculate floor tiles     *')
    print('*    Press \'2\' to calculate floor tiles     *')
    print('*        Press any other key to quit        *')
    print('*                                           *')
    print('*********************************************')
    user_choice = input('Please make your choice: ')            # User makes a selection
    if user_choice == '1':
        calculate_floor() 
    elif user_choice == '2':
        calculate_walls()
    else: 
        quit()

def calculate_floor():              # Function to calculate floor cost
    clear()
    floor_length = float(input('Please enter the length of the floor: '))
    floor_width = float(input('Please enter the width of the floor: '))
    floor_price = float(input('Please enter the tile cost per square meter: '))
    floor_cost = (floor_length * floor_width) * floor_price
    print('The cost of tiling the floor will be {}'.format(str(floor_cost)))
    menu_option = input('Please press \'M\' to return to the main menu or \'Q\' to quit: ')
    if menu_option == 'm':
        start_program()
    else:
        quit()

def calculate_walls():          # Function to calculate wall cost
    clear()
    walls_length = float(input('Please enter the total length of the walls: '))
    walls_height = float(input('Please enter the total height of the walls: '))
    walls_price = float(input('Please enter the tile cost per square meter: '))
    floor_cost = (walls_length * walls_height) * walls_price
    print('The cost of tiling the walls will be {}'.format(str(floor_cost)))
    menu_option = input('Please press \'M\' to return to the main menu or \'Q\' to quit: ')
    if menu_option == 'm':
        start_program()
    else:
        quit()



start_program()