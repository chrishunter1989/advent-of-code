
# Imports
import re

# Options
verbose    = False
test_mode  = False

# Lists
num_strs = [('one',        1),
            ('two',        2),
            ('three',      3),
            ('four',       4),
            ('five',       5),
            ('six',        6),
            ('seven',      7),
            ('eight',      8),
            ('nine',       9)]

# Function for debug print
def debug_print(str):
    if verbose: print(str)

# Function to convert number string to number
def get_number(number):
    for str,val in num_strs:
        if number == str:
            return val        
    return number

# ----- Part 1 -----
sum = 0
input_file = "d1p1_test.input" if test_mode else "d1.input"
with open(input_file, "r") as f:
    for line in f.readlines():
        line_numbers = re.findall(r'\d', line)
        
        if len(line_numbers) > 0:
            num = '{}{}'.format(line_numbers[0], line_numbers[-1])
            debug_print(num)
            sum += int(num)
print("Part One = {}".format(sum))


# ----- Part2 -----
sum = 0
input_file = "d1p2_test.input" if test_mode else "d1.input"
with open(input_file, "r") as f:
    for line in f.readlines():
        line_numbers = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)
        debug_print(line_numbers)

        if len(line_numbers) > 0:
            num = '{}{}'.format(get_number(line_numbers[0]), get_number(line_numbers[-1]))
            debug_print(num)
            sum += int(num)

print("Part Two = {}".format(sum))
