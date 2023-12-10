
# Imports

# Options
verbose    = True
test_mode  = False

# Lists


# Function for debug print
def debug_print(str):
    if verbose: print(str)



# ----- Part 1 and 2 -----
sum_p1     = 0
sum_p2     = 0
input_file = "d2p1_test.input" if test_mode else "d2.input"
with open(input_file, "r") as f:
    for line in f.readlines():
        game_num, turns = line.split(": ")
        game_num = game_num.split()[1]
        valid_game      = True
        req_red   = 0
        req_green = 0
        req_blue  = 0
        for turn in turns.split("; "):
                for balls in turn.split(", "):
                     _num, colour = balls.split()      
                     num = int(_num)

                     if colour == "red":
                        if num > 12:        valid_game = False
                        if num > req_red:   req_red    = num

                     if colour == "green":
                        if num > 13:        valid_game = False
                        if num > req_green: req_green  = num

                     if colour == "blue":
                        if num > 14:        valid_game = False
                        if num > req_blue:  req_blue   = num

        # Part 1         
        if valid_game:
             sum_p1 += int(game_num)

        # Part 2
        sum_p2 += (req_red * req_green * req_blue)

        

print("Part One = {}".format(sum_p1))
print("Part Two = {}".format(sum_p2))



