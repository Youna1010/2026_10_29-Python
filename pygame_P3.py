import pygame_ce as pygame

pygame.init()

screen = pygame.display.set_mode((600, 300))
pygame.display.set_caption("Pygame練習")

running = True

while running:
    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, (255, 0, 0), (50, 50, 100, 100))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()