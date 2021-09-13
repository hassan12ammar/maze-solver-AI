def start_values():
    FILE_PATH = input("maze path: ").strip('"\'') #"/home/hassan/Documents/testing/maze3.txt"             #"maze1.txt"
    OUTFILE_PATH = input("output path: ").strip('"\'') #"/home/hassan/Documents/testing/maze solve3.txt"    #"maze solve1.txt"
    HIGHT = len(open(FILE_PATH,'r').readlines())
    WIEDTH = len(open(FILE_PATH,'r').readline())-1
    file = open(FILE_PATH,'r')
    MAZE = file.read()
    file.close()
    file = open(OUTFILE_PATH,"w+")
    file.write(MAZE)
    file.close()
    return FILE_PATH,OUTFILE_PATH,HIGHT,WIEDTH

FILE_PATH, OUTFILE_PATH, HIGHT, WIEDTH = start_values()

def reload_maze():
    file = open(OUTFILE_PATH,'r')
    maze = file.read()
    file.close()
    return maze

maze = reload_maze()

def latter_indexing(l):
    with open(FILE_PATH,'r+') as file:
        column = 0
        for line in file.readlines():
            column+= 1
            row = 0
            for latter in line:
                row+= 1
                if latter == l:
                    return column,row

def column_row_indexing(col,row_):
    with open(OUTFILE_PATH,'r+') as file:
        indx = 0
        coloumn = 0
        for line in file.readlines():
            coloumn += 1
            row = 0
            for latter in line:
                indx += 1
                row += 1
                if coloumn == col and row == row_:
                    return indx-1

def write_move(index,move):
    maze_ = maze[:index] + move + maze[index + 1:]
    with open(OUTFILE_PATH,'r+') as file:
        file.seek(0)
        file.write(maze_)

def check(col,row,check_sample):
    check_sample_dict = \
    {
        "up":(col-1,row),
        "down":(col+1,row),
        "right":(col,row+1),
        "left":((col,row-1))
    }
    return_values = []
    if col >= 0 and row >= 0 :
        for sample in check_sample_dict:
            if sample == "down" and col == HIGHT :
                continue
            if sample == "right" and row == WIEDTH :
                continue
            current_check_x,current_check_y = check_sample_dict[sample]
            current_check_index = column_row_indexing(current_check_x,current_check_y)
            if check_sample == maze[current_check_index]:
                return_values.append((check_sample_dict[sample],sample))
        return return_values
    else:
        return False

def move(col,row,sample):
    global maze
    sample_dict = {
        "up":"|",
        "down":"|",
        "right":"-",
        "left":"-"}
    for sample_check in sample_dict:
        if sample == sample_check:
            write_move(column_row_indexing(col,row),sample_dict[sample_check]) #move_down(col,row)
            maze = reload_maze()

def get_min_distance_value(move_list,END_X,END_Y):
    distance_values_list = []
    if len(move_list)>0:
        for move in range(len(move_list)):
            move_value = move_list[move][0]
            distance_value = abs((move_value[0]-END_X)+(move_value[1]-END_Y))
            distance_values_list.append(distance_value)
    minimum_value = min(distance_values_list)
    return distance_values_list.index(minimum_value)

def main():
    #setting up the constant
    global maze
    print("maze solver by Hassan Ammar")
    print(maze)
    END = input("end sample: ") #'+'
    START = input("start sample: ") #'.'
    MOVE = input("move sample: ") #' '
    END_X,END_Y = latter_indexing(END)
    START_X,START_Y = latter_indexing(START)
    position_x,position_y = START_X,START_Y
    move_list = []
    #began the main loop by checking the end
    while not check(position_x,position_y,END):
        #check() return list of all posible moves in tuple with direction
        move_list = check(position_x,position_y,MOVE)
        #calculate the distance of moves and return the index of minimum value
        minimum_value_index = get_min_distance_value(move_list,END_X,END_Y)
        #get the coordinates as tuple and direction of minimum value from the move list
        best_move_index,best_move = move_list[minimum_value_index]
        #split the coordinates to x and y of the value
        best_move_index_x,best_move_index_y = best_move_index
        print(best_move)
        #make the move
        move(best_move_index_x,best_move_index_y,best_move)
        #change the current coordinates position
        position_x,position_y = best_move_index_x,best_move_index_y
        #check the odds of winning
        win_status = [check(position_x,position_y,END) == 'up',
                    check(position_x,position_y,END) == 'down',
                    check(position_x,position_y,END) == 'right',
                    check(position_x,position_y,END) == 'left']
        #check if any of it if True 
        if any(win_status):
            print("Solustion Found")
            break
        #check dead end
        if not move_list :
            print("No Solutio Found")
            break
        #remove the previous move from the move list
        move_list.pop(minimum_value_index)
    #tell the user that we done and display the answer
    print("Done.")
    print(maze)

if __name__ == "__main__":
    main()
