import pygame
import outcome
from turns import *

winner = ''

def run():
    global winner

    pygame.init()

    w, h = 600, 600
    s = pygame.display.set_mode((w, h))
    pygame.display.set_caption('Tic-Tac-Toe')
    # Add a clock to limit the frame rate.
    player = "X"

    while True:
        if outcome.xWin(board):
            winner = 'X'
            return
        elif outcome.oWin(board):
            winner = 'O'
            return
        elif outcome.tieGame(board):
            winner = 'Nobody'
            return
        else:
            pygame.draw.line(s, white, (200, 0), (200, 600), 14)
            pygame.draw.line(s, white, (400, 0), (400, 600), 14)
            pygame.draw.line(s, white, (0, 200), (600, 200), 14)
            pygame.draw.line(s, white, (0, 400), (600, 400), 14)

            player = turn(player)
