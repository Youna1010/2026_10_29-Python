import pygame

pygame.init()

screen = pygame.display.set_mode((600, 300))

x = 0

running = True
while running:

    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, (255, 0, 0), (x, 50, 100, 100))

    x += 1

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()