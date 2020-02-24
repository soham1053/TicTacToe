import pygame
import math

pygame.init()
board = [['', '', ''], ['', '', ''], ['', '', '']]
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
white = (255, 255, 255)
black = (0, 0, 0)

def turn(player):
    if player == "X":
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()
                    if isOpen(mx, my):
                        draw(mx, my, player)
                        player = "O"
                        return player

            pygame.display.flip()
            clock.tick(60)  # Limit the frame rate to 60 FPS.
#----------------------------------------------------- PLAYER CHANGE -----------------------------------------------------#
    elif player == "O":
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()
                    if isOpen(mx, my):
                        draw(mx, my, player)
                        player = "X"
                        return player

            pygame.display.flip()
            clock.tick(60)  # Limit the frame rate to 60 FPS.

def draw(mx, my, player):
    mx /= 200
    my /= 200
    floormx, floormy = math.floor(mx), math.floor(my)
    mx, my = floormx*200, floormy*200

    if board[floormy][floormx] == '':
        if player == "X":
            board[floormy][floormx] = "X"
            pygame.draw.line(screen, white, (mx, my), (mx+200, my+200), 10)
            pygame.draw.line(screen, white, (mx, my+200), (mx+200, my), 10)

        elif player == "O":
            board[floormy][floormx] = "O"
            pygame.draw.circle(screen, white, (mx+100, my+100), 100)
            pygame.draw.circle(screen, black, (mx+100, my+100), 80)

def isOpen(mx, my):
    mx /= 200
    my /= 200
    floormx, floormy = math.floor(mx), math.floor(my)
    return board[floormy][floormx] == ''
