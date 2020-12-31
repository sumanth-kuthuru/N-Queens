# -*- coding: utf-8 -*-
"""
N-Queens problem
@author: Sumanth Kuthuru
"""
import numpy as np

class Queen:                  #Defining a class with variables r, c

    def __init__(self, r, c):
        self.r = r
        self.c = c

    def get_rows(self):        #This Method returns row
        return self.r

    def get_columns(self):     #This Method returns columns
        return self.c

    def attack_pairs(self, q):          #This function checks if there are any attacking pairs and returns a bool value
        return self.r == q.get_rows() or self.c == q.get_columns() \
               or abs(self.c - q.get_columns()) == abs(self.r - q.get_rows())   #Checking for diagonal attacking pairs

    def move_down(self, moves):           #Move the queen down along the column according to no of steps specified
        self.r = (self.r + moves) % Board.get_size();



class Board:
    board_size = 8

    def __init__(self):
        self.state = []               #A list which stores Queen's row and column position
        self.next_state = []          #A list for all possible next_states
        self.h = 0

    def node(self, n):               #Method for how to append to state
        for i in range(Board.board_size):
            self.state.append(Queen(n.state[i].get_rows(), n.state[i].get_columns()))

    def get_size():                     #To get the size of board
        return Board.board_size

    def set_size(size):                 #To set the size of the board
        Board.board_size = size

    def calculate_h(self):              #To caluculate the heuristic value of current_node
        for i in range(Board.board_size - 1):
            for j in range(i + 1, Board.board_size):
                if (self.state[i].attack_pairs(self.state[j])):
                    self.h += 1
        return self.h
    def get_h(self):                     #To get the h value of the current_node
        return self.h

    def neighbour_node(self, initial_state):  # Method to find neighbour nodes
        count = 0
        for i in range(Board.board_size):
            for j in range(1, Board.board_size):
                new_board = Board()
                new_board.node(initial_state)
                self.next_state.insert(count, new_board)
                self.next_state[count].state[i].move_down(j)
                self.next_state[count].calculate_h()
                count += 1

        return self.next_state

    def heu_diff(self, n):                #To find the diff btw current_node and neighbour node
        if (self.h < n.get_h()):
            return -1
        elif (self.h > n.get_h()):
            return 1
        else:
            return 0



    def set_node(self, s):
        for i in range(Board.board_size):
            self.state.append(Queen(s[i].get_rows(), s[i].get_columns()))

    def print_board(self):          #Method to print boards from state which contains Queen's row and column position

        board = np.zeros((Board.get_size(),Board.get_size()), dtype=str)   #To have a initial Matrix filled with zeros
        for i in range(Board.board_size):
            for j in range(Board.board_size):
                board[i][j]="#"                    #Those empty posiitons that Queen is not present are marked as '#'
        for i in range(Board.board_size):
            board[self.state[i].get_rows()][self.state[i].get_columns()]="Q"  #Those positions Queen is present is represented using 'Q'
        return board
