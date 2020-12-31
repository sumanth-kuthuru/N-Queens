# -*- coding: utf-8 -*-
"""
N-Queens problem
@author: Sumanth Kuthuru
"""
import random
import numpy as np
from Board import Board
from Board import Queen
from HillClimbing_Variants import Steepest_Ascent_Hill_Climbing
from HillClimbing_Variants import Sideways_Move
from HillClimbing_Variants import Random_Restart_Steepest_Ascent
from HillClimbing_Variants import Random_Restart_Sideways_Move

board_size = input("Enter the the N value for number of queens in n-Queen problem: ")  #Enter N value
board_size=int(board_size)
runtime = input("Please enter the How many times you want to Run: ")                   #How may times you want to Run
runtime= int(runtime)

Board.set_size(board_size)
def generate_initial_state():                   # We generate state at each column a queen is placed at a random row
    state= []
    for i in range(Board.board_size):
        state.append(Queen(random.randint(0, Board.board_size - 1), i))
    return state

steepest_ascent_hill_climbing_success_sum=0
steepest_ascent_hill_climbing_average_success=0
steepest_ascent_hill_climbing_success_steps=0
steepest_ascent_hill_climbing_average_success_steps=0
steepest_ascent_hill_climbing_fail_steps=0
steepest_ascent_hill_climbing_average_fail_steps=0

sideways_moves_sum_success=0
sideways_moves_average_success=0
sideways_moves_success_steps=0
sideways_moves_average_success_steps=0
sideways_moves_fail_steps=0
sideways_moves_average_fail_steps=0

random_restart_steepest_ascent_sum_success=0
random_restart_steepest_ascent_average_success=0
random_restart_steepest_ascent_success_steps=0
random_restart_steepest_ascent_average_success_steps=0
random_restart_steepest_ascent_count=0

random_restart_side_moves_sum_success=0
random_restart_side_moves_average_success=0
random_restart_side_moves_success_steps=0
random_restart_side_moves_average_success_steps=0
random_restart_side_moves_count=0

for current_test in range(1, runtime+1):             #To run the algorithm as per user's run time input
    initial_state= generate_initial_state()

    '''
    steepest ascent hill climbing
    '''
    steepest_ascent_hill_climbing = Steepest_Ascent_Hill_Climbing(initial_state)   #creating an object
    steepest_ascent_hill_climbing_board = steepest_ascent_hill_climbing.hill_climb() #board that steepest ascent returns

    if steepest_ascent_hill_climbing_board.calculate_h()==0:  #If h = 0 then we found a possible solution
        suc = True
        steepest_ascent_hill_climbing_success_sum+=1
        steepest_ascent_hill_climbing_success_steps= steepest_ascent_hill_climbing.get_moves()
        steepest_ascent_hill_climbing_average_success_steps+=steepest_ascent_hill_climbing_success_steps

    else:
        suc = False
        steepest_ascent_hill_climbing_fail_steps=steepest_ascent_hill_climbing.get_moves()
        steepest_ascent_hill_climbing_average_fail_steps += steepest_ascent_hill_climbing_fail_steps

    #As described printing sequences for four different initial config
    if current_test==49:
        print("Path for 1st initial configuration of steepest ascent Hill climbing")
        x = steepest_ascent_hill_climbing.all_nodes()
        steepest_ascent_hill_climbing.print_path(x)
        print("Path cost: ", len(x))
        if suc:
            print("success")
        else:
            print("Failure")

    if current_test==99:

        print("Path for 2nd initial configuration of steepest ascent Hill climbing")
        x = steepest_ascent_hill_climbing.all_nodes()
        steepest_ascent_hill_climbing.print_path(x)
        print("Path cost: ", len(x))
        if suc:
            print("success")
        else:
            print("Failure")

    if current_test==199:
        print("Path for 3rd initial configuration of steepest ascent Hill climbing")
        x = steepest_ascent_hill_climbing.all_nodes()
        steepest_ascent_hill_climbing.print_path(x)
        print("Path cost: ",len(x))
        if suc:
            print("success")
        else:
            print("Failure")

    if current_test==299:
        print("Path for 4th initial configuration of steepest ascent Hill climbing")
        x = steepest_ascent_hill_climbing.all_nodes()
        steepest_ascent_hill_climbing.print_path(x)
        print("Path cost: ",len(x))
        if suc:
            print("success")
        else:
            print("Failure")
    '''
    sideways move hill climbing
    '''
    sideways_move = Sideways_Move(initial_state)     #creating an object
    sideways_move_board = sideways_move.hill_climb()   #board that sideways move hill climb returns

    if sideways_move_board.get_h() == 0:               #If h = 0 then we found a possible solution
        suc = True
        sideways_moves_sum_success += 1
        sideways_moves_success_steps = sideways_move.get_moves()
        sideways_moves_average_success_steps += sideways_moves_success_steps

    else:
        suc = False
        sideways_moves_fail_steps = sideways_move.get_moves()
        sideways_moves_average_fail_steps += sideways_moves_fail_steps

    #As described printing sequences for four different initial config
    if current_test == 59:
        print("Path for 1st initial configuration of sideways move Hill climbing")
        x = sideways_move.all_nodes()
        sideways_move.print_path(x)
        print("Path cost: ", len(x))
        if suc:
            print("success")
        else:
            print("Failure")

    if current_test == 109:
        print("Path for 2nd initial configuration of sideways move Hill climbing")
        x = sideways_move.all_nodes()
        sideways_move.print_path(x)
        print("Path cost: ", len(x))
        if suc:
            print("success")
        else:
            print("Failure")

    if current_test == 209:
        print("Path for 3rd initial configuration of sideways move Hill climbing")
        x = sideways_move.all_nodes()
        sideways_move.print_path(x)
        print("Path cost: ", len(x))
        if suc:
            print("success")
        else:
            print("Failure")

    if current_test == 309:
        print("Path for 4th initial configuration of sideways move Hill climbing")
        x = sideways_move.all_nodes()
        sideways_move.print_path(x)
        print("Path cost: ", len(x))
        if suc:
            print("success")
        else:
            print("Failure")
    '''
    random restart steepest ascent
    '''
    random_restart_steepest_ascent = Random_Restart_Steepest_Ascent(initial_state)
    random_restart_steepest_ascent_board = random_restart_steepest_ascent.hill_climb(initial_state)

    if random_restart_steepest_ascent_board.get_h() == 0:
        random_restart_steepest_ascent_sum_success += 1

        random_restart_steepest_ascent_success_steps = random_restart_steepest_ascent.get_moves()
        random_restart_steepest_ascent_average_success_steps += random_restart_steepest_ascent_success_steps
        random_restart_steepest_ascent_count += random_restart_steepest_ascent.get_random_restarts()

    '''
    random restart sideways move
    '''

    random_restart_sideways_move = Random_Restart_Sideways_Move(initial_state)
    random_restart_sideways_move_board= random_restart_sideways_move.hill_climb(initial_state)


    if random_restart_sideways_move_board.get_h() == 0:
        random_restart_side_moves_sum_success+=1
        random_restart_side_moves_success_steps=random_restart_sideways_move.get_moves()
        random_restart_side_moves_average_success_steps+= random_restart_side_moves_success_steps;
        random_restart_side_moves_count+=(random_restart_sideways_move.get_random_restarts());


#To calculate average sucess of four variants
steepest_ascent_hill_climbing_average_success= steepest_ascent_hill_climbing_success_sum / runtime
sideways_moves_average_success = sideways_moves_sum_success/ runtime
random_restart_steepest_ascent_average_success = random_restart_steepest_ascent_sum_success / runtime;
random_restart_side_moves_average_success =random_restart_side_moves_sum_success / runtime;


#Printing the results according the project description
print("Steepest Ascent :"

        " Success Count = ", steepest_ascent_hill_climbing_success_sum
      , " Success rate = ", steepest_ascent_hill_climbing_average_success
      , " Fail count = ", (runtime - steepest_ascent_hill_climbing_success_sum)
      , " Failure rate = ", (1 - steepest_ascent_hill_climbing_average_success)
      , " Avg Successful Steps = ", (steepest_ascent_hill_climbing_average_success_steps / steepest_ascent_hill_climbing_success_sum)
      , " Avg Failed Steps : ", ((steepest_ascent_hill_climbing_average_fail_steps) / (runtime - steepest_ascent_hill_climbing_success_sum)));

print("Sideways Move :"

       " Success Count = ", sideways_moves_sum_success
      , " Success rate = ", sideways_moves_average_success
      , " Fail count  = ", (runtime - sideways_moves_sum_success)
      , " Failure rate = ", (1 - sideways_moves_average_success)
      , " Avg Success Steps = ", (sideways_moves_success_steps / sideways_moves_sum_success)
      , " Avg Fail Steps = ", (np.float64(sideways_moves_average_fail_steps) / (runtime - sideways_moves_sum_success)));


print("Random Restart Steepest Ascent:"

                    , " Success Count = " , random_restart_steepest_ascent_sum_success
                    , " Success rate = " , random_restart_steepest_ascent_average_success
                    , " Fail Count = " , (runtime - random_restart_steepest_ascent_sum_success)
                    , " Failure rate = " , (1 - random_restart_steepest_ascent_average_success)
                    , " Avg Success Steps = " , ((random_restart_steepest_ascent_average_success_steps)/runtime)
                    , " Avg Random Restart =" , (random_restart_steepest_ascent_count/runtime));

print("Random Restart Sideways :"

                , " Success Count = " , random_restart_side_moves_sum_success
                , " Success rate = " , random_restart_side_moves_average_success
                , " Fail Count = " , (runtime - random_restart_side_moves_sum_success)
                , " Failure rate = " , (1 - random_restart_side_moves_average_success)
                , " Avg Success Steps = " , ((random_restart_side_moves_average_success_steps)/runtime)
                , " Avg Random Restart = " , (random_restart_side_moves_count)/runtime);
