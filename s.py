import pygame

pygame.init()

white = (255, 255, 255)
grey = (178, 147, 74)
green = (0, 255, 0)
red = (255, 0, 0)

dis_width = 800
dis_height = 800
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('First Game by pygame =)')
game_over = False
x1 = dis_width/2
y1 = dis_height/2

objS = 10

x1_change = 0
y1_change = 0

clock = pygame.time.Clock()
speed = 30

font_style = pygame.font.SysFont(None, 50)


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/2, dis_height/2])


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            if event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            if event.key == pygame.K_UP:
                y1_change = -10
                x1_change = 0
            if event.key == pygame.K_DOWN:
                y1_change = 10
                x1_change = 0
    x1 += x1_change
    y1 += y1_change
    dis.fill(grey)
    pygame.draw.rect(dis, green, [x1, y1, 10, 10])
    pygame.display.update()
    clock.tick(30)
pygame.quit()
quit()
