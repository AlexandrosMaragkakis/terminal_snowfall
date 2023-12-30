

#TODO: explore colors
#TODO: add version that contains house
#TODO: add seasonal theming, f.e. leaves on autumn 
#TODO: figure out presets for different densities
#TODO: add wind
#TODO: add interactive controls for live parameter changes
#TODO: add person and steer them to avoid snow


import os
import random
import time

# Constants
SNOW_DENSITY = 2 # more snow
DELAY = 0.1 # faster snow
MELT_DELAY = 1 # when to melt
MELTING_FACTOR = 1000 # how much to melt
snowflakes = ['❄', '❆', '❅', '❃', '❇', '❈', '❉', '❊', '❋']

# Get terminal size
term = os.get_terminal_size()
w = term.columns
h = term.lines

# Initialize empty grid
grid = [[' '] * w for _ in range(h)]

# Fill bottom with '~'
for i in range(w):
    grid[h-1][i] = '¯'

ascii_house = """
  []___
 /    /\\
/____/__\\
|[][]||||
"""

ascii_rows = ascii_house.split('\n')

house_height = len(ascii_rows)
house_width = len(ascii_rows[-1])

# Calculate the starting position to embed the ASCII art in the grid
ascii_start_row = h - house_height 
ascii_start_col = 10 + house_width // 2  # Adjusted to be to the right of the center


# Embed the ASCII art into the grid
for i, row in enumerate(ascii_rows):
    # Find the first non-space character in the row
    start_index = 0#row.find(row.lstrip())
    for j, char in enumerate(row):
        # Skip leading spaces and update the grid
        if char != ' ':
            grid[ascii_start_row + i][ascii_start_col + start_index + j] = char







def melt_snowflakes():
    """
    Melt snowflakes in the grid.

    This function iterates over the grid and melts snowflakes based on a random chance.
    Each snowflake has a chance of melting based on the SNOW_DENSITY and MELTING_FACTOR.
    """
    for j in range(w):
        for i in range(h - 1, 0, -1):
            if grid[i][j] in snowflakes and random.random() < SNOW_DENSITY / MELTING_FACTOR:
                grid[i][j] = ' '

def generate_new_row():
    """
    Generate a new row of snowflakes at the top of the grid.
    """
    new_row = []
    for j in range(w):
        if random.random() < SNOW_DENSITY / 1000:
            new_row.append(random.choice(snowflakes))
        else:
            new_row.append(' ')
    grid[0] = new_row

def update_grid():
    """
    Update the grid by moving snowflakes down one row.
    """
    for i in range(h - 1, 0, -1):
        for j in range(w):
            if grid[i][j] == ' ' and grid[i-1][j] in snowflakes:
                grid[i][j] = grid[i-1][j]
                grid[i-1][j] = ' '

def clear_screen():
    """
    Clear the terminal screen.
    """
    os.system('clear')

def hide_cursor():
    """
    Hide the cursor in the terminal.
    """
    print('\033[?25l')

def show_grid():
    """
    Print the grid on the screen.
    """
    output = ''
    for row in grid:
        output += ''.join(row) + '\n'
    output = output.strip('\n')
    print(output, end='')

def snowfall():
    """
    Run the snowfall animation.
    """
    global DELAY
    while True:
        clear_screen()
        hide_cursor()

        generate_new_row()
        melt_snowflakes()
        update_grid()
        show_grid()

        time.sleep(DELAY)
        if DELAY > MELT_DELAY:
            DELAY -= 0.01

def main():
    """
    Main entry point of the program.
    """
    snowfall()

main()