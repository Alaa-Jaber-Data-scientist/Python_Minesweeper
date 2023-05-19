"""
This code generates a Minesweeper grid based on user input.
The user specifies the number of rows and columns and then enters
the contents of the grid row by row. The script then calculates the
number of adjacent cells that contain mines ('#') and displays the
result.
"""


# Define a function to validate user input.
def validate_input(prompt):
    """ This function prompts the user to enter a positive integer and validates the input.
    If the input is not a positive integer, the function raises a ValueError and prompts the user to enter a valid number.
    Once a valid number is entered, the function returns the value.
    """
    while True:
        try:
            value = int(input(prompt))
            if value <= 0 :
                raise ValueError
            return value
            
        except ValueError:
            print("Please enter a valid number. Only positive digital input is valid.")


# Prompt the user to input the grid contents row by row and validate the input.
def get_grid():
    """
    This function loops through each row of the grid.
    prompts the user to enter the contents of each row, and validates the input.
    If the input contains characters other than '-' and '#', the function prompts the user to enter a valid row.
    Once a valid row is entered, it is added to the grid.
    After all rows are entered and validated, the function prints the user-entered grid and returns it.
    """
    allowed_characters = ["-", "#"]
    grid = []
    for i in range (rows_number):
        row_list = []
        while True:
            try: 
                # Prompt the user to enter the row, and validate the input.           
                row = input(f"\tEnter row {i+1} (use '-' for empty cells and '#' for mines): ")
               
                if len(row) == columns_number:
                    valid_row = True
                    
                    for char in row:
                        if char not in allowed_characters:
                            print("Invalid input. Please use only '-' and '#' in your grid.")
                            valid_row = False
                            row_list = []
                            break
                        else:
                            row_list.append(char)
                    
                    if valid_row:
                        # Add the row to the grid if it is valid.
                        grid.append(row_list)
                        break

                else:
                    raise ValueError
            except:
                # If the user enters an invalid number of characters, prompt them to enter again.
                print(f"You have entered {len(row)} elements. Please enter only {columns_number} elements in a row.")
    
    # Print the user-entered grid.
    print("\nYou have entered the following grid:") 
   
    # Iterate through each row of the grid and print it.    
    for row in (grid):
        # Join the elements of the row into a string separated by spaces.
        print (" ".join(row))
    print ()
    return grid


# Define a function to check adjacent cells for mines.            
def adjacent_grid():
    """ This function: Count the number of adjacent cells that contain mines"#".
     For each empty cell, check the eight surrounding cells for mines.
     Update the cell with the count of adjacent mines."""

    for index, row in enumerate (grid):
        for col, value in enumerate (row):
            if value == "-":
                count = 0      
                for i in range(index-1, index+2):
                    for c in range(col-1, col+2):            
                        if (i != index or c != col) and (0 <= i < rows_number) and (0 <= c < columns_number):
                            if grid[i][c] == "#":
                                count += 1
                
                row[col] = str(count)
            else:
                row[col] = "#"
    
    # Print Minesweeper grid.    
    print ("Here is your Minesweeper game grid: ")   
    # Iterate through each row of the grid and print it.   
    for row in (grid):
        # Join the elements of the row into a string separated by spaces.
        print (" ".join(row))



# Print a welcome message.
print("Welcome to Minesweeper!")
print("*" * 70)
# Provide instructions for the user to follow when using the program.
print("Please enter the number of rows and columns for your game grid.")


# Loop until the user enter 'N' to exit.
while True:
    
    # prompt the user to input rows and columns number. 
    rows_number = validate_input ("Enter the number of rows: ")
    columns_number = validate_input ("Enter the number of columns: ")     
    print("*" * 70)
    print("\nPlease enter the contents of your game grid, one row at a time.")   
    
    grid = get_grid() 
    adjacent_grid() 
    
    # Ask the user if they want to continue or exit the program.
    repeat = True  
    while repeat:
        exit = input("\nDo you want to continue? (Y,N): ").lower()
        
        if exit == "y":
            break
        elif exit == "n":
            print("Thank you for using Minesweeper!")
            repeat = False          
            break
        else:
            print(f"You have entered '{exit}'. Please enter either 'Y' to continue or 'N' to exit. ")
            continue
           
    # Exit the loop if the user wants to exit the program.
    if repeat == False :
        break