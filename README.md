# Maze Solver Based on A* Algorthim
This script takes a path of maze as txt file, output path, some information 
(beginning sample, end sample and the move) Then solve the maze and save in the output path
It's implementation of A* algorthim in pyrhon
### **Have Fun. :)**

## This is an example of how it's work:

```
python main.py
maze path: 'maze example/maze1.txt'
output path: 'maze example/maze solve1.txt'
start sample: .
end sample: +
move sample:  
your maze: 
########################################
#           #                         ##
#           # ####################### ##
#           # #            ###      # ##
#           # #            #+#      # ##
#  ########## #            # #      # ##
#  #          #            # #      # ##
#  # ##########            # #      # ##
#  # #         ############# ######## ##
#  # #         #                    # ##
#  # #         # ################## # ##
#  # #         # #                #   ##
#  # #         # #  ####################
#  # #         # #  #      #           #
#  # #         # #### #### #           #
#  # #         #      #  # #           #
#  # #         ########  # #           #
#  ####################### #           #
#  #                       #           #
####.###################################
Done
Solution Found: 
########################################
#           #                         ##
#           # ####################### ##
#           # #            ###      # ##
#           # #            #+#      # ##
#  ########## #            #|#      # ##
#  #          #            #|#      # ##
#  # ##########            #|#      # ##
#  # #         #############|######## ##
#  # #         #|------------       # ##
#  # #         #|################## # ##
#  # #         #|#                #   ##
#  # #         #|#  ####################
#  # #         #|#  #-----|#           #
#  # #         #|####|####|#           #
#  # #         #-----|#  #|#           #
#  # #         ########  #|#           #
#  #######################|#           #
#  #|----------------------#           #
####.###################################
```
