# import from files
from typing import Union
from constant import END, END_X, END_Y
from constant import MAZE, HIGHT, WIEDTH, OUTFILE_PATH, START_X, START_Y, MOVE


def index_of_col_row(col:int, row:int) -> Union[int, None]:
    """ get the index of sample by its coloumn and row """
    with open(OUTFILE_PATH, 'r+') as file:
        indx = 0
        for coloumn, line in enumerate(file.readlines()):
            for row_, _ in enumerate(line):
                indx += 1
                if coloumn == col and row_ == row:
                    return indx - 1


def write_move(index:int, move:str) -> None:
    """ write the move to board """
    global solution
    solution = solution[:index] + move + solution[index + 1:]
    with open(OUTFILE_PATH,'r+') as file:
        file.seek(0)
        file.write(solution)


def check(col:int, row:int, check_for=END) -> Union[list, None]:
    """ check if the there is sample arround the given column and row 
        and return a list of coordinates if so """
    if col <= 0 and row <= 0 :
        return

    global solution
    check_sample_dict = \
    {
        "up"    : (col - 1, row),
        "down"  : (col + 1, row),
        "right" : (col,     row + 1),
        "left"  : (col,     row - 1)
    }
    samples_found = []

    for sample in check_sample_dict:
        # ignore the boundried of the maze
        if sample == "down" and col == HIGHT:
            continue
        if sample == "right" and row == WIEDTH:
            continue
        x, y = check_sample_dict[sample]
        sample_index = index_of_col_row(x, y)
        if check_for == solution[sample_index]:
            samples_found.append((check_sample_dict[sample], sample))

    return samples_found


def move(col:int, row:int, sample:str) -> None:
    """ make move from column and row and diraction (up, down, left, right) """
    move_sample = {
        "up"    : "|",
        "down"  : "|",
        "right" : "-",
        "left"  : "-"
    }
    write_move(index_of_col_row(col,row), move_sample[sample])


def get_min_distance_value(moves:list) -> Union[int, None]:
    """ return None if in the edge 
        otherwise return index of the closest move to the end target """
    if len(moves) < 0:
        return

    distance_values_list = [
        # distance value between move and the target end
        abs( (move[0] [0] - END_X) + 
                (move[0] [1] - END_Y) )
        for move in moves ]

    minimum_value = min(distance_values_list)
    return distance_values_list.index(minimum_value)


def main():
    global solution
    solution = MAZE

    position_x, position_y = START_X, START_Y

    while not check(position_x, position_y, END):
        # get list of all posible moves in with its direction
        move_list = check(position_x,position_y, MOVE)
        # check dead end
        if not move_list: return
        # get the index of the closest move to the target end
        minimum_value_index = get_min_distance_value(move_list)
        # get the coordinates (x, y) and the direction of minimum value from the move availabe
        (best_move_x, best_move_y), best_move = move_list[minimum_value_index]
        # make the move
        move(best_move_x, best_move_y, best_move)
        # change the current coordinates position
        position_x, position_y = best_move_x, best_move_y
        # check if we found a solotion
        sol_status = [check(position_x,position_y, END) == 'up',
                    check(position_x,position_y, END) == 'down',
                    check(position_x,position_y, END) == 'right',
                    check(position_x,position_y, END) == 'left']
        if any(sol_status):
            return solution
        # remove the previous move from the move availabe
        move_list.pop(minimum_value_index)

    return solution

if __name__ == "__main__":
    # write the maze into the output file to solve
    with open(OUTFILE_PATH, "w+") as file: file.write(MAZE)

    print(f"your maze: \n{MAZE}")

    final_solution = main()

    print("Done")

    if not final_solution:
        print("No Solution Found")
        print(final_solution)
    else:
        print("Solution Found: ")
    print(solution)


