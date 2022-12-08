def range_char(start, stop):
    return (chr(n) for n in range(ord(start), ord(stop) + 1))

def new_game(grid, coins):
    while coins != 0:
        print()
        show_grid(grid)
        print()
        print('1. Build building')
        print('2. See coins')
        print('0. Exit to main menu')

        print()
        menu_choice = input("Enter choice: ")

        if menu_choice == "1":
            build_building()
        elif menu_choice == "2":
            pass
        elif menu_choice == "3":
            break
        elif menu_choice == "0":
            break
        else:
            print('Invalid choice. Please try again.')

def build_building():
    pass

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


if __name__ == "__main__":
    while True:
        # Global variable initialisation and setting
        grid_size = 20
        grid = [["   " for col in range(grid_size)] for row in range(grid_size)]
        coins = 16

        # Print statement to display the menu and prompt user for choice
        print("""
$$\   $$\  $$$$$$\  $$$$$$$$\ $$$$$$$$\        $$$$$$\  $$\   $$\ $$\   $$\        $$$$$$\  $$$$$$\ $$$$$$$$\ $$\     $$\ 
$$$\  $$ |$$  __$$\ $$  _____|$$  _____|      $$  __$$\ $$$\  $$ |$$$\  $$ |      $$  __$$\ \_$$  _|\__$$  __|\$$\   $$  |
$$$$\ $$ |$$ /  \__|$$ |      $$ |            $$ /  $$ |$$$$\ $$ |$$$$\ $$ |      $$ /  \__|  $$ |     $$ |    \$$\ $$  / 
$$ $$\$$ |$$ |$$$$\ $$$$$\    $$$$$\          $$$$$$$$ |$$ $$\$$ |$$ $$\$$ |      $$ |        $$ |     $$ |     \$$$$  /  
$$ \$$$$ |$$ |\_$$ |$$  __|   $$  __|         $$  __$$ |$$ \$$$$ |$$ \$$$$ |      $$ |        $$ |     $$ |      \$$  /   
$$ |\$$$ |$$ |  $$ |$$ |      $$ |            $$ |  $$ |$$ |\$$$ |$$ |\$$$ |      $$ |  $$\   $$ |     $$ |       $$ |    
$$ | \$$ |\$$$$$$  |$$$$$$$$\ $$$$$$$$\       $$ |  $$ |$$ | \$$ |$$ | \$$ |      \$$$$$$  |$$$$$$\    $$ |       $$ |    
\__|  \__| \______/ \________|\________|      \__|  \__|\__|  \__|\__|  \__|       \______/ \______|   \__|       \__|    """)
        print()
        print("Welcome to Ngee Ann City!")
        print("1. Start game")
        print("2. <something>")
        print("3. <something>")
        print()
        print("0. Exit")

        menu_input = input("Choice: ")

        if menu_input == "1":
            new_game(grid, coins)
        elif menu_input == "0":
            print()
            break
        else:
            print("wrong input")
