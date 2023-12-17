
# Imports
import re

# Options
verbose    = False
test_mode  = False

# Function for debug print
def debug_print(str):
    if verbose: print(str)

# Function to find adjacent symbol
def find_adjacent_sym(number, x_start, x_end, y):

    # Determine which rows to check for symbols (Y-1/Y/Y+1)
    num_per_row = schematic[-1][2]
    num_rows    = schematic[-1][3]
    rows_to_check = []
    if y > 0: 
        rows_to_check.append(y-1)
    rows_to_check.append(y)
    if y < num_rows:
        rows_to_check.append(y+1)

    debug_print("   Rows Info: {}".format(rows_to_check))

    # Find symbols on the required rows and check
    # whether they're adjacent
    for entry in schematic:
        # If this row (y) is in range, and isn't a period, then check it
        if entry[3] in rows_to_check and entry[0] != '.':

            # If it's a number, then ignore and move on
            try:
                val = int(entry[0])
                continue

            # Else, it's a symbol, so let's check it...
            except:
                # Set symbol search range. We allow +1 for diagonal, but limit
                # this if the number is at the start/end of the line (as don't want to check
                # out of bounds)
                min_x = x_start-1 if x_start >          0  else x_start
                max_x = x_end+1   if x_end   < num_per_row else x_end
                debug_print("   Symbol Info: {}, pos={}, range_min={}, range_max={}".format(entry[0], entry[1], min_x, max_x))

                # Note: Symbols start/end is the same, as only one character
                if entry[1] in range(min_x, max_x+1):
                    debug_print("      adjacent!")

                    # Check whether it's a gear, and store the info for Part 2
                    if entry[0] == "*":
                        debug_print("      it's a gear!")
                        # Index 0 = gear X coordinate (row position)
                        # Index 1 = gear Y coordinate (row)
                        # Index 2 = adjacent number
                        gears.append((entry[1], entry[3],number))

                    return True
                else:
                    debug_print("      not adjacent!")

    return False


# ----- Read in -----
schematic  = [] 
gears      = []
input_file = "d3p1_test.input" if test_mode else "d3.input"
with open(input_file, "r") as f:
    # Find all numbers, symbols and periods and store in an array (schematic)
    for y, read_line in enumerate(f.readlines()):
        entries = re.finditer(r'(\d+|.|[^\n| ])', read_line)
        for entry in entries:
            # Index 0 = value (number/symbol/period)
            # Index 1 = Start position of the value on the row (x_start)
            # Index 2 = End position of the value  on the row  (x_end)
            # Index 3 = Row number (y)
            schematic.append((entry.group(), int(entry.start()), int(entry.end()-1), y))

# ----- Part 1 -----
sum        = 0
for entry in schematic:
    try:
        val = int(entry[0])
        debug_print("\nChecking {}".format(val))
        if find_adjacent_sym(val, entry[1], entry[2], entry[3]):
            sum = sum + val
            
    except:
        continue  
print("Part One = {}".format(sum))

# ----- Part 2 -----
sum        = 0
for i in range(0, len(gears)-1):
    two_gears  = []
    two_gears.append(gears[i])
    for y in range(i+1, len(gears)):
        if (gears[i][0] == gears[y][0]) and (gears[i][1] == gears[y][1]):
            two_gears.append(gears[y])

    # Says it must match exactly two (i.e. not 1 or 3 or more)
    if len(two_gears) == 2:
        debug_print(two_gears)
        sum = sum + (two_gears[0][2] * two_gears[1][2])

print("Part Two = {}".format(sum))

