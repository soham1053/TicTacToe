import game
import pygame

if __name__ == '__main__':
    game.run()

    pygame.init()

    white = (255, 255, 255)
    green = (0, 255, 0)
    blue = (0, 0, 128)

    width, height = game.width, game.height
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Tic-Tac-Toe')

    font = pygame.font.Font('freesansbold.ttf', 85)
    winStatement = game.winner + ' wins!'
    text = font.render(winStatement, True, green, blue)
    textRect = text.get_rect()
    textRect.center = (width // 2, height // 2)

    while True :
        screen.fill(white)
        screen.blit(text, textRect)
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                quit()
            pygame.display.update()
