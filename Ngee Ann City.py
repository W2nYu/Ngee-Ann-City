#Import needed packages
import random

#Function(s) to start game
def start_game():
    pass

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



if __name__ == "__main__":
    while True:
        #Global variable initialisation and setting
        grid_size = 20
        grid = [["   "for col in range(grid_size)]for row in range(grid_size)]
        building_list = ['R', 'I', 'C', 'O', '*']
        turns = 0
        coins = 16
        
        #Print statement to display the menu and prompt user for choices
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
                print(grid)
            elif option == 2:
                pass
            elif option == 3:
                print("Suck my nuts")
            elif option == 0:
                print("You have exited the game :)")
                break
            else:
                print("Please enter again, entry not valid :(  \n")
        else:
            print("Please enter again, entry not valid :(  \n")
