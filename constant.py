""" get the constants we need """

import os
from utlize import latter_indexing


# get the path of the maze file
FILE_PATH = input("maze path: ").strip('"\'')
assert os.path.exists(FILE_PATH), "File Not exists at: " + str(FILE_PATH)

# get the path of the solution
OUTFILE_PATH = input("output path: ").strip('"\'')
if not os.path.exists(OUTFILE_PATH):
    os.mkdir(OUTFILE_PATH)

# read the maze and get the hight and width
with open (FILE_PATH, 'r') as file:
    MAZE = file.read()
with open (FILE_PATH, 'r') as file:
    WIEDTH = len(file.readline()) - 1
    HIGHT = len(file.readlines())

# setting up other constant
START = input("start sample: ")
END = input("end sample: ")
MOVE = input("move sample: ")
END_X, END_Y = latter_indexing(END, FILE_PATH)
START_X, START_Y = latter_indexing(START, FILE_PATH)

