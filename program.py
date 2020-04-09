import pygame
import sys

pygame.init()
grid = []

number = 0
resolution = width, height = 400,400
black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
width = 40
height = 40
pos = 0,0

screen = pygame.display.set_mode(resolution)
colour = white

def draw_grid_rect(screen,width,height,pos):
    for x in range(1, 400, 50):
        for y in range(1, 400, 50):
            if pos[0] > x and pos[0] < x+50:
                if pos[1] > y and pos[1] < y+50:
                    colour = red
                    pygame.draw.rect(screen, colour, (x, y, width, height))
                else:
                    colour = white
                    pygame.draw.rect(screen, colour, (x, y, width, height))
                    pygame.display.update()

for x in range(1, 400, 50):
    for y in range(1, 400, 50):
        pygame.draw.rect(screen, colour, (x, y, width, height))
        pygame.display.update()

while True:
    screen.set_alpha(None)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            print(pos[0])
            print(pos[1])

        draw_grid_rect(screen,width,height,pos)
