import pygame

pygame.init()
dis = pygame.display.set_mode((400, 300))
pygame.display.update()
pygame.display.set_caption('First Game by pygame =)')
game_over=False
while not game_over:
    for event in pygame.event.get():
        print(event)

pygame.quit()
quit()
