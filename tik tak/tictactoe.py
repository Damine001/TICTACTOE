import sys

from zmq import HEARTBEAT_IVL 
import pygame
from const import *
import numpy as np 

#PYGAME SETUP 
#22 ~
pygame.init()
screen = pygame.display.set_mode((WIDTH,HIGHT))
pygame.display.set_caption("TIC TAC TOE")
screen.fill(BG_COLOR)

class Board:
    def __init__(self) -> None:
              self.squares =  np.zeros((ROWS,COLS))
              self.mark_sqr(1,1,2)
              print(self.squares)
              
    def mark_sqr ( self,row,col,player):
        self.squares[row][col] = player 
    
    
class Game:
    
    def __init__(self):
        self.board = Board()
        self.show_lines()
    
    def show_lines(self):
         #Vertical lines
         pygame.draw.line(screen,LINE_COLOR,(SQSIZE,0),(SQSIZE,HIGHT),LINE_WIDTH)
         pygame.draw.line(screen,LINE_COLOR,(WIDTH-SQSIZE,0),(WIDTH-SQSIZE,HIGHT),LINE_WIDTH)
         
         #HORIZONTAL
         pygame.draw.line(screen,LINE_COLOR,(0,SQSIZE),(WIDTH,SQSIZE),LINE_WIDTH)
         pygame.draw.line(screen,LINE_COLOR,(0,HIGHT-SQSIZE),(WIDTH,HIGHT-SQSIZE),LINE_WIDTH)
        
def main():
    
    #OBJECT
    game=Game()
    
    while True :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

main()