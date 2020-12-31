# -*- coding: utf-8 -*-
"""
N-Queens problem
@author: Sumanth Kuthuru
"""
import random
from Board import Board
from Board import Queen

class Steepest_Ascent_Hill_Climbing:              #Class for simple Hill Climbing search

    def __init__(self,s):
        self.moves = 0
        self.print_nodes=[]
        self.start_node = Board()
        initial_state= []
        for i in range(Board.get_size()):
            initial_state.append((Queen(s[i].get_rows(), s[i].get_columns())))
        self.start_node.set_node(initial_state)
        self.start_node.calculate_h()


    def hill_climb(self):              #Hill Climbing search algorithm

        current_node = self.start_node

        while True:                                  #Infinite loop breaks when solution is found or not found
            nieghbours = current_node.neighbour_node(current_node)            #All neighbours of current node
            better_heu = False                        #bool value which checks if better heurisitc exists
            self.print_nodes.append(current_node)
            self.moves+=1

            for i in range(len(nieghbours)):
                if(nieghbours[i].heu_diff(current_node) < 0):   #To find closest of all neighbours nodes to solution
                    current_node=nieghbours[i]                  #The current node is neghbour node with lesser heuristic value
                    better_heu= True
                    #break                                      #breaks once it finds the neighbour node that is closest to solution

            if not better_heu:
                return current_node             #returns the current node
    def all_nodes(self):                  #stores all nodes generated
        return self.print_nodes

    def print_path(self, print_nodes):          #prints the path the algorithm took
        for i in range(len(self.print_nodes)):
            print(self.print_nodes[i].print_board())

    def get_start_node(self):                   #Method to get start node
        return self.start_node

    def get_moves(self):                        #gets all moves
        return self.moves


class Sideways_Move:              #Class for Sideways Move Hill Climbing search

    def __init__(self, s):
        initial_state = []
        self.start_node = Board()
        self.moves = 0
        self.print_nodes = []
        for i in range(Board.get_size()):
            initial_state.append((Queen(s[i].get_rows(), s[i].get_columns())))
        self.start_node.set_node(initial_state)
        self.start_node.calculate_h()

    def hill_climb(self):           #Hill Climbing search algorithm
        current_node = self.start_node
        count = 0

        while True:                 #Infinite loop breaks when solution is found or not found
            neighbours = current_node.neighbour_node(current_node)       #All neighbours of current node
            select_random_neighbours = []

            better_heu = False;              #bool value which checks if better heurisitc exists
            best_heu = False                 #bool value which checks if best heurisitc exists

            self.print_nodes.append(current_node)

            for i in range(len(neighbours)):
                if count == 100:
                   break
                if (neighbours[i].heu_diff(current_node) <= 0):
                    if (neighbours[i].heu_diff(current_node) < 0):      #To find closest of all neighbours nodes to solution
                        count = 0
                        select_random_neighbours = []
                        current_node = neighbours[i]
                        better_heu = True
                        self.moves += 1
                    elif (neighbours[i].heu_diff(current_node) == 0):   # If heu diff = 0, then we have to select a random neighbour
                        select_random_neighbours.append(neighbours[i])

            if not better_heu and select_random_neighbours:           # To select a random neighbour
                current_node = select_random_neighbours[random.randint(0, len(select_random_neighbours)) - 1]
                best_heu = True
                count += 1
                self.moves += 1
            if not best_heu and not better_heu:                 # Return current node either if solution is found or not found
                return current_node

    def get_start_node(self):                                   #Method to get start node
        return self.start_node

    def print_path(self, print_nodes):                          #prints the path the algorithm took
        for i in range(len(self.print_nodes)):
            print(self.print_nodes[i].print_board())

    def all_nodes(self):                                         #stores all nodes generated
        return self.print_nodes

    def get_moves(self):                                        #gets all moves
        return self.moves


class Random_Restart_Steepest_Ascent:                       # Class for Random Restart

    def __init__(self, s):
        self.moves = 0
        self.initial_state = 0
        self.steepest_ascent_object = Steepest_Ascent_Hill_Climbing(s) # Creating an object using steepest ascent hill climbing class
        Random_Restart_Steepest_Ascent.restart_used = 1

    def hill_climb(self, s): # Hill climbing algorithm
        current_node = self.steepest_ascent_object.get_start_node()   # To get the start node
        self.set_initial_state(current_node)
        h = current_node.get_h()                            # To get the h value
        self.moves = 0

        while h != 0:
            next_state = self.steepest_ascent_object.hill_climb()     # Stores the node returned by hill climb
            self.moves += self.steepest_ascent_object.get_moves()     # To get moves
            h = next_state.get_h()                                    # To get h

            if h != 0:
                s = Random_Restart_Steepest_Ascent.generate_initial_state()     # To generate  random initial state
                self.steepest_ascent_object = Steepest_Ascent_Hill_Climbing(s)
                Random_Restart_Steepest_Ascent.restart_used += 1              # Incrementing number of restarts
            else:                                                            # If found solution we assign the node returned
                current_node = next_state
                self.moves -= self.steepest_ascent_object.get_moves()
                Random_Restart_Steepest_Ascent.restart_used += 1
        return current_node

    def generate_initial_state():                   # Method to generate random initial state
        state = []
        for i in range(8):
            state.append(Queen(random.randint(0, Board.get_size() - 1), i))
        return state

    def set_initial_state(self, current_board):
        self.initial_state = current_board

    def get_moves(self):
        return self.moves

    def get_random_restarts(self):                                     # To get the number of restarts used
        return Random_Restart_Steepest_Ascent.restart_used


class Random_Restart_Sideways_Move: #class for random restart sideways move

    def __init__(self, s):
        self.steps = 0
        self.start = 0
        self.sideways_move_object = Sideways_Move(s)
        Random_Restart_Sideways_Move.restart_used = 1

    def hill_climb(self, s):   #hill climbing algoritjm
        current_node = self.sideways_move_object.get_start_node()
        self.set_start_node(current_node)
        h = current_node.get_h()
        self.steps = 0

        while h != 0:                      #If not found the solution then
            next_board = self.sideways_move_object.hill_climb()     #we call hill climb method
            self.steps += self.sideways_move_object.get_moves()
            h = next_board.get_h()

            if h != 0:
                s = Random_Restart_Sideways_Move.generate_initial_state() #we generate an another initial state
                self.sideways_move_object = Sideways_Move(s)
                Random_Restart_Sideways_Move.restart_used += 1      #we keep track of no of restarts
            else:
                current_node = next_board       #we return this node if h=0
        return current_node

    def generate_initial_state():     #To generate random initial config
        start = []
        for i in range(8):
            start.append(Queen(random.randint(0, Board.get_size() - 1), i))
        return start

    def set_start_node(self, current_board):    #To set start node
        self.start = current_board

    def get_moves(self):                #To get moves
        return self.steps

    def get_random_restarts(self):      #To get total random restarts
        return Random_Restart_Sideways_Move.restart_used
