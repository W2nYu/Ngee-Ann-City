#Import needed packages
import random

#Function(s) to start game
def range_char(start, stop):
    return (chr(n) for n in range(ord(start), ord(stop) + 1))

def new_game(grid, coins):
    while coins != 0:
        #Randomly selected buildings to play game with
        choice1 = rand_pool(building_list)
        choice2 = rand_pool(building_list)

        #Print grid and new_game option
        print()
        show_grid(grid)
        print()
        print('1. Build a {}'.format(choice1))
        print('2. Build a {}'.format(choice2))
        print('3. See coins')
        print('4. See current score')
        print('5. Save current game')
        print('0. Exit to main menu')

        print()
        menu_choice = input("Enter choice: ")

        #If statement to 
        if menu_choice == "1":
            build_building(grid, choice1, turns)
        if menu_choice == "2":
            build_building(grid, choice2, turns)
        elif menu_choice == "3":
            print("Amount of coins remainding: {}".format(coins) )
        elif menu_choice == "4":
            print("See current score feature is currently not available")   
        elif menu_choice == "5":
            print("Save game feature is currently not available")   
        elif menu_choice == "0":
            break
        else:
            print('Invalid choice. Please try again.')

#Functions(s) to build a building in game
def build_building(grid, build_choice, turns):
    x_axis = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 'x', 't', ]
    y_axis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    while True:
        option = input("Choose a plot to build: ")
        option = option.lower()

        if len(option) == 2 and option[1].isnumeric():
            x = option[0]
            y = int(option[1])
            if x in x_axis and y in y_axis: #Validate if input option within the grid
                col = x_axis.index(x)
                row = y_axis.index(y)

                if turns == 0:
                    grid[row][col] = build_choice #Build choice is string value
                    break

                #Help to check if building is built
                elif turns > 0:
                    nxt_buildings = []
                    if row != 0:
                        nxt_buildings.append(grid[row-1][col])
                    if row != 19:
                        nxt_buildings.append(grid[row+1][col])
                    if col != 0:
                        nxt_buildings.append(grid[row][col-1])
                    if col != 19:
                        nxt_buildings.append(grid[row][col+1])

                    count_nxt_buildings = 0
                    for building in building_list:
                        count_nxt_buildings += nxt_buildings.count(building)
                    
                    if count_nxt_buildings != 0:
                        if grid[row][col] == '   ':
                            grid[row][col] = build_choice
                            print()
                            break
                    else:
                        print('Square is unavailable!')
                else:
                    print("You must build next to an existing building.")
            else:
                print("Input is not within grid, please re-enter valid plot!")
        else:
            print("Please re-enter a valid plot :)")

def rand_pool(pool_list):  
  while True:
    randInt = random.randint(0,4)
    return pool_list[randInt]

#Function to show grid
def show_grid(grid):
    grid_len = len(grid)  # assuming that the grid is a square

    print(' ', end='')
    for alphabet in range_char("A", "T"):
        print('     {}'.format(alphabet), end='')
    print()

    print('   ', end='')  # printing 2 space to align with row numbering
    for col in range(grid_len):
        print('+-----', end='')
    print('+')

    row_num = 1
    for row in range(grid_len):
        if row_num < 10:
            print(' ', end='')  # printing 1 space for numbers < 10
        print(' {}'.format(row_num), end='')
        row_num += 1

        # show the grid with buildings
        for col in grid[row]:
            print('| {} '.format(col), end='')
        print('|')

        print('   ', end='')  # printing 2 space to align with row numbering
        for column in range(grid_len):
            print('+-----', end='')
        print('+')
    pass


#Main code 
if __name__ == "__main__":
    while True:
        #Global variable initialisation and setting
        grid_size = 20
        grid = [["   "for col in range(grid_size)]for row in range(grid_size)]
        building_list = [' R ', ' I ', ' C ', ' O ', ' * ']
        turns = 0
        coins = 16
        
        #Print statement to display the menu and prompt user for choices
        print("""
                $$\   $$\  $$$$$$\  $$$$$$$$\ $$$$$$$$\        $$$$$$\  $$\   $$\ $$\   $$\        $$$$$$\  $$$$$$\ $$$$$$$$\ $$\     $$\ 
                $$$\  $$ |$$  __$$\ $$  _____|$$  _____|      $$  __$$\ $$$\  $$ |$$$\  $$ |      $$  __$$\ \_$$  _|\__$$  __|\$$\   $$  |
                $$$$\ $$ |$$ /  \__|$$ |      $$ |            $$ /  $$ |$$$$\ $$ |$$$$\ $$ |      $$ /  \__|  $$ |     $$ |    \$$\ $$  / 
                $$ $$\$$ |$$ |$$$$\ $$$$$\    $$$$$\          $$$$$$$$ |$$ $$\$$ |$$ $$\$$ |      $$ |        $$ |     $$ |     \$$$$  /  
                $$ \$$$$ |$$ |\_$$ |$$  __|   $$  __|         $$  __$$ |$$ \$$$$ |$$ \$$$$ |      $$ |        $$ |     $$ |      \$$  /   
                $$ |\$$$ |$$ |  $$ |$$ |      $$ |            $$ |  $$ |$$ |\$$$ |$$ |\$$$ |      $$ |  $$\   $$ |     $$ |       $$ |    
                $$ | \$$ |\$$$$$$  |$$$$$$$$\ $$$$$$$$\       $$ |  $$ |$$ | \$$ |$$ | \$$ |      \$$$$$$  |$$$$$$\    $$ |       $$ |    
                \__|  \__| \______/ \________|\________|      \__|  \__|\__|  \__|\__|  \__|       \______/ \______|   \__|       \__|    """)
        print("\n \n \n")

        print("Welcome mayor of Ngee Ann City!")
        print("---------------------------")
        print("1. Start new game")
        print("2. Load saved game")
        print("3. Show high score")
        print()
        print("0. Exit")
        option = input("Select option: ")

        #If statements to execute functions based on choice
        if option:
            option = int(option)
            if option == 1:
                new_game(grid, coins)
            elif option == 2:
                print("Load saved game feature is currently not available!")
            elif option == 3:
                print("High score feature is currently not available!")
            elif option == 0:
                print("You have exited the game :)")
                break
            else:
                print("Please enter again, entry not valid :(  \n")
        else:
            print("Please enter again, entry not valid :(  \n")
