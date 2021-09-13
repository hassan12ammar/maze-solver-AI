def start_values():
    FILE_PATH = "/home/hassan/Documents/testing/maze3.txt"             #"maze1.txt"
    OUTFILE_PATH = "/home/hassan/Documents/testing/maze solve3.txt"    #"maze solve1.txt"
    HIGHT=len(open(FILE_PATH,'r').readlines())
    WIEDTH=len(open(FILE_PATH,'r').readline())-1
    file =open(FILE_PATH,'r')
    MAZE =file.read()
    file.close()
    file =open(OUTFILE_PATH,"w+")
    file.write(MAZE)
    file.close()
    return FILE_PATH,OUTFILE_PATH,HIGHT,WIEDTH

FILE_PATH, OUTFILE_PATH, HIGHT, WIEDTH = start_values()
# print("start values: ",start_values())

def reload_maze():
    file =open(OUTFILE_PATH,'r')
    maze =file.read()
    file.close()
    return maze

maze=reload_maze()
# print(maze)

def latter_indexing(l):
    with open(FILE_PATH,'r+') as file:
        column=0
        for line in file.readlines():
            column+=1
            row=0
            for latter in line:
                row+=1
                if latter ==l:
                    return column,row
START_INDEX_X,START_INDEX_Y=latter_indexing(".")
# print("START_INDEX_X,START_INDEX_Y: ",START_INDEX_X,START_INDEX_Y)
# print("latter_indexing("+"): ",latter_indexing("+"))

def column_row_indexing(col,row_):
    with open(OUTFILE_PATH,'r+') as file:
        indx=0
        coloumn=0
        for line in file.readlines():
            coloumn+=1
            row=0
            for latter in line:
                indx+=1
                row+=1
                if coloumn == col and row == row_:
                    return indx-1
START_INDEX=column_row_indexing(START_INDEX_X,START_INDEX_Y)
# print("START_INDEX: ",START_INDEX)
# print("maze[START_INDEX]: ",maze[START_INDEX])

def write_move(index,move):
    maze_ = maze[:index] + move + maze[index + 1:]
    with open(OUTFILE_PATH,'r+') as file:
        file.seek(0)
        file.write(maze_)
# UP_START=column_row_indexing(START_INDEX_X-1,START_INDEX_Y)
# write_move(UP_START,"|")
# maze=reload_maze()
# print(maze)

def move_up(col,row):
    write_move(column_row_indexing(col-1,row),'|')
    global maze
    maze=reload_maze()
    return col-1,row
def move_down(col,row):
    write_move(column_row_indexing(col+1,row),'|')
    global maze
    maze=reload_maze()
    return col+1,row
def move_right(col,row):
    write_move(column_row_indexing(col,row-1),'-')
    global maze
    maze=reload_maze()
    return col,row+1
def move_left(col,row):
    write_move(column_row_indexing(col,row+1),'-')
    global maze
    maze=reload_maze()
    return col,row-1
# UP_START_X,UP_START_Y=move_up(START_INDEX_X,START_INDEX_Y)
# LEFT_UP_START_X,LEFT_UP_START_Y=move_left(UP_START_X,UP_START_Y)
# RIGHT_UP_START_X,RIGHT_UP_START_Y=move_right(UP_START_X,UP_START_Y)
# DOWN_START_X,DOWN_START_Y=move_down(UP_START_X,UP_START_Y)
# print(maze)


def check(col,row,check_sample):
    check_sample_dict=\
    {
        "up":(col-1,row),
        "down":(col+1,row),
        "right":(col,row+1),
        "left":((col,row-1))
    }
    return_values=[]
    if col >=0 and row >=0 :
        for sample in check_sample_dict:
            if sample =="down" and col == HIGHT :
                continue
            if sample == "right" and row == WIEDTH :
                continue
            # print("sample,check_sample_dict[sample]: ",sample,check_sample_dict[sample])
            current_check_x,current_check_y=check_sample_dict[sample]
            # print("current_check_x,current_check_y: ",current_check_x,current_check_y)
            current_check_index=column_row_indexing(current_check_x,current_check_y)
            # print("current_check_index: ",current_check_index)
            if check_sample==maze[current_check_index]:
                return_values.append((check_sample_dict[sample],sample))
        return return_values
    else:
        return False
# print(maze)
# print("check(START_INDEX_X,START_INDEX_Y," "): ",check(START_INDEX_X,START_INDEX_Y," "))
# print("check(11,27," "): ",check(11,27," "))

def move(col,row,sample):
    global maze
    # print("col,row: ",col,row)
    # print("check_sample: ",sample)
    sample_dict={
        "up":"|",
        "down":"|",
        "right":"-",
        "left":"-"}
    for sample_check in sample_dict:
        # print("sample, sample_check: ",sample, sample_check)
        # print("sample ==sample_check: ",sample ==sample_check)
        if sample == sample_check:
            write_move(column_row_indexing(col,row),sample_dict[sample_check]) #move_down(col,row)
            maze=reload_maze()

    # elif check_sample == 'down':
    #     write_move(column_row_indexing(col,row),"|") #move_up(col,row)
    #     maze=reload_maze()
    # elif check_sample == 'right':
    #     write_move(column_row_indexing(col,row),"-") #move_left(col,row)
    #     maze=reload_maze()
    # elif check_sample == 'left':
    #     write_move(column_row_indexing(col,row),"-") #move_right(col,row)
    #     maze=reload_maze()
    # else:
    #     return False

# (start_move_x,start_move_y),start_sample=check(START_INDEX_X,START_INDEX_Y," ")[0]
# print("start_move_x,start_move_y,start_sample: ",start_move_x,start_move_y,start_sample)
# print("move(start_move_x,start_move_y,start_sample): ",move(start_move_x,start_move_y,start_sample))
# print(maze)

def get_min_distance_value(move_list,END_X,END_Y):
    # print("-------in get_min_distance_value-------")
    # print("move_list: ",move_list)
    distance_values_list=[]
    # print("len of move_list: ",len(move_list))
    if len(move_list)>0:
        for move in range(len(move_list)):
            move_value=move_list[move][0]
            # print("move_value: ",move_value)
            # print("first move value: ",move_value[0])
            # print("second move value: ",move_value[1])
            distance_value=abs((move_value[0]-END_X)+(move_value[1]-END_Y))
            # print("distance_value: ",distance_value)
            distance_values_list.append(distance_value)
    # print("distance_values_list: ",distance_values_list)
    minimum_value=min(distance_values_list)
    # print("minimum_values: ",minimum_value)
    # print("-------out of get_min_distance_value-------")
    return distance_values_list.index(minimum_value)
# END="+"
# END_X,END_Y=latter_indexing(END)
# move_list=check(11,27," ")
# minimum_value_index=get_min_distance_value(move_list,END_X,END_Y)
# # print("minimum_value_index: ",minimum_value_index)
# # print("move_list[minimum_value_index]: ",move_list[minimum_value_index])
# (best_move_index_x,best_move_index_y),best_move=move_list[minimum_value_index]
# # print("best_move_index_x,best_move_index_y,best_move: ",best_move_index_x,best_move_index_y,best_move)
# move(best_move_index_x,best_move_index_y,best_move)
# # print(maze)

# def check_sampleall(check_samplevalue_,position_x_,position_y_,MOVE,move_list_,move_played_):
#     if check_samplevalue_ == 'up':
#         print("up",position_x_,position_y_)  # print(maze)
#         new_position_x,new_position_y = position_x_-1,position_y_ #move_up(position_x,position_y)
#         move_list_.append((new_position_x,new_position_y))
#         move_played_=True
#     if check_samplevalue_ == 'down':
#         print("down",position_x_,position_y_)  # print(maze)
#         new_position_x_,new_position_y_ = position_x_+1,position_y_ #move_down(position_x,position_y)
#         move_list_.append((new_position_x,new_position_y))
#         move_played_=True
#     if check_samplevalue_ == 'right':
#         print("right",position_x_,position_y_)  # print(maze)
#         new_position_x_,new_position_y_ = position_x_,position_y_+1 #move_right(position_x,position_y)
#         move_list_.append((new_position_x_,new_position_y_))
#         move_played_=True
#     if check_samplevalue_ == 'left':
#         print("left",position_x_,position_y_)  # print(maze)
#         new_position_x_,new_position_y_ = position_x_,position_y_-1 #move_left(position_x,position_y)
#         move_list_.append((new_position_x_,new_position_y_))
#         move_played_=True
#     return new_position_x_,new_position_y_,move_list_,move_played_


def main():
    global maze
    print("maze solver by Hassan Ammar")
    print(maze)
    END='+'
    START='.'
    MOVE=' '
    END_X,END_Y=latter_indexing(END)
    START_X,START_Y=latter_indexing(START)
    position_x,position_y = START_X,START_Y
    move_list=[]
    # move_played=False
    while not check(position_x,position_y,END):
        move_list = check(position_x,position_y,MOVE)
        # if move_list:
        #     move_list.append(move_list)
        print("Beging move list:  ",move_list)
        minimum_value_index=get_min_distance_value(move_list,END_X,END_Y)
        print("index of minimum value_: ",minimum_value_index)
        print("minimum value: ",move_list[minimum_value_index])
        best_move_index,best_move = move_list[minimum_value_index]
        print("best_move_index: ",best_move_index)
        print("best_move: ",best_move)
        best_move_index_x,best_move_index_y=best_move_index
        # print(best_move_index_x,best_move_index_y,best_move)
        move(best_move_index_x,best_move_index_y,best_move)
        position_x,position_y=best_move_index_x,best_move_index_y
        # print(maze)
        win_status=[check(position_x,position_y,END)=='up',
                    check(position_x,position_y,END)=='down',
                    check(position_x,position_y,END)=='right',
                    check(position_x,position_y,END)=='left']
        if any(win_status):
            print("Solustion Found")
            break

        if not move_list :
            print("No Solutio Found")
            break
        move_list.pop(minimum_value_index)

    print("Done.")
    print(maze)

if __name__ == "__main__":
    main()
