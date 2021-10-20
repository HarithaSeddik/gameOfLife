#%% Initialize Libraries

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from numpy.core.fromnumeric import repeat
from numpy.lib.type_check import isreal

class gameOfLife():
    def __init__(self, board):
        self.board = board
        self.M,self.N = len(board), len(board[0])
        
    
    #Check against rules to determine life/death of a cell
    def checkCell(self, r,c):
        p = [(0,1),(0,-1), (1,0), (-1,0), (1,1), (-1, -1), (-1,1), (1,-1)] #Positions of all 8 neighbors

        count = 0
        for x,y in p:
            #if we are in bound of the board, and our neighbor is alive, count it!
            if 0<= r+x < self.M and 0<= c+y <self.N and self.board[r+x][c+y] ==1:
                count+=1
        
        #If the current cell was already alive
        if self.board[r][c] ==1:

            if count<2: 
                return 0 #DIES FROM ISOLATION
            elif 2<=count<=3: 
                return 1 # STAYS ALIVE
            else: 
                return 0 # DIES FROM OVERPOPULATION

        #If current cell was dead
        else: 
            if count==3:
                return 1 #REBIRTH
            else:
                return 0  #REMAINS DEAD

    def updatePopulation(self):
        temp = [ [None]*self.N for _ in range(self.M) ] #initialize temporary board

        #Fill out temp matrix
        for r in range (self.M):
            for c in range(self.N):
                temp[r][c] = self.checkCell(r,c)

        # Update original matrix
        for r in range (self.M):
            for c in range(self.N):
                self.board[r][c] = temp[r][c]
    
    #Update the population every time
    def animate(self, frame):
        self.updatePopulation()
        plt.imshow(self.board)
    
    def showEvolution(self):
        fig = plt.figure()
        #Animation!
        anim = animation.FuncAnimation( fig, self.animate, frames=100, interval = 500 , repeat='true')
        plt.show()
        anim()




#Main function

if __name__ == "__main__":
    
    #Read from text file
    with open('input.txt') as f:
       lines = f.readlines()[1:]
       lines = [line.strip() for line in lines]
    f.close()

    mat=[] #Intialize initial matrix
    for line in lines:
        row =[]
        for digit in line:
            if (digit.isnumeric()):
                row.append(int(digit))
        mat.append(row)
    
    solution = gameOfLife(mat)
    solution.showEvolution()