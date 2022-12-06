def new_game(coins):
    while coins != 0:
        show_grid()
        print('1. Build building')
        print('2. See current score')
        print('3. Exit')

        menu_choice = input("Choice: ")

        if menu_choice == "1":
            build_building()
        elif menu_choice == "2":




def build_building():
    pass

def show_grid():
    pass

if __name__ == "__main__":
    while True:
        # Global variable initialisation and setting
        grid_size = 20
        grid = [["   " for col in range(grid_size)] for row in range(grid_size)]
        coins = 16

        print()
        # Print statement to display the menu and prompt user for choice
        new_game()
        break

        # If statements to execute functions based on choice