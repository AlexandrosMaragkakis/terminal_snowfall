import os
import random
import time

SNOW_DENSITY = 20
DELAY = 0.2

snowflakes = ['❄', '❅', '❆', '❃', '❇', '❈', '❉', '❊', '❋']
term = os.get_terminal_size()

w = term.columns
h = term.lines

grid = []

for _ in range(h):
    grid.append([' '] * w)

def is_row_full(row):
    for i in range(w):
        if row[i] == ' ':
            return False
    return True

def draw_grid():
    os.system('clear')

    # hide the cursor
    print('\033[?25l')

    output = ''

    for row in grid:
        output += ''.join(row) + '\n'

    output = output.strip('\n')

    print(output, end='')

while True:
     # Generate new row of snowflakes at the top
    row = []
    for j in range(w):
        if random.random() < SNOW_DENSITY / 100:
            row.append(random.choice(snowflakes))
        else:
            row.append(' ')
    grid[0] = row

    for i in range(h - 1, 0, -1):
        for j in range(w):
            if grid[i][j] == ' ':
                grid[i][j] = grid[i-1][j]
                grid[i-1][j] = ' '

   # if is_row_full(grid[h//2]):
   #     # shift the middle row one at a time till it reaches the bottom
   #     for i in range(h//2, h):
   #         for j in range(w):
   #             grid[i][j] = grid[i-1][j]
   #             grid[i-1][j] = ' '
    


    draw_grid()

    time.sleep(DELAY)
