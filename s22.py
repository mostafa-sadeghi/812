import pygame
pygame.init()
size = (700, 500)
screen = pygame.display.set_mode(size)
BLACK = (0, 0, 0)
ORANGE = (255, 100, 50)
WHITE = (255, 255, 255)
clock = pygame.time.Clock()
xposition = 0
yposition = 0
Y_Change = 1
done = True
while done:  # main loop
    for event in pygame.event.get():  # event loop
        if event.type == pygame.QUIT:
            done = False

    screen.fill(ORANGE)
    pygame.draw.rect(screen, BLACK, [xposition, yposition, 50, 50])
    xposition += 1
    yposition += Y_Change

    if yposition > 450:
        Y_Change = -1 * Y_Change


    pygame.display.flip()
    clock.tick(60)
