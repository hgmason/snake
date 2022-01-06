import pygame, sys
from pygame.locals import *
import time
import random

#KeyDown = 2
#KeyUp = 3
KeyDown = 768
KeyUp = 769
#UP_KEY = 273
UP_KEY = 1073741906
#RIGHT_KEY = 275
RIGHT_KEY = 1073741903
#DOWN_KEY = 274
DOWN_KEY = 1073741905
#LEFT_KEY = 276
LEFT_KEY = 1073741904
size = 20
snake = []
speed = 0
STOP = (0,0)
RIGHT = (0,1)
LEFT = (0,-1)
UP = (-1,0)
DOWN = (1,0)
dir = STOP
tic = 100
game_running = False
game_end = False
scalar = .99
# set up pygame
pygame.init()

# set up the window
height = 30*size
width = 30*size
windowSurface = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption('snakeu')
food = [0,0]

# set up the colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# set up fonts
basicFont = pygame.font.SysFont(None, 20)

# draw the white background onto the surface
windowSurface.fill(BLACK)

# draw the window onto the screen
pygame.display.update()

#draw a box around a top left
def draw_box(x,y):
    #(left, top, width, height)
    a = int(size*scalar)
    pygame.draw.rect(windowSurface, GREEN, (y,x,a,a))
def clear_box(x,y):
    a = int(size*scalar)
    pygame.draw.rect(windowSurface, BLACK, (y,x,a,a))
def draw_food():
    x = random.randint(0,int((height-1)/size))*size
    y = random.randint(0,int((width-1)/size))*size
    while([x,y] in snake):
        x = random.randint(0,int((height-1)/size))*size
        y = random.randint(0,int((width-1)/size))*size
    global food
    food = [x,y]
    a = int(size*scalar)
    pygame.draw.rect(windowSurface, RED, (y,x,a,a))

def end_game():
    global game_running
    game_running = False
    global game_end
    game_end = True
    text = basicFont.render("LENGTH: "+str(len(snake))+". Press space to restart.", True, RED)
    windowSurface.blit(text, text.get_rect())
    pygame.display.update()
    global dir
    dir = STOP


def move_snake():
    head = snake[0]
    next_box = [head[0] + dir[0]*size, head[1] + dir[1]*size]
    if (next_box in snake) or (next_box[0] >= height) or (next_box[1] >= width) or (next_box[0] < 0) or (next_box[1] < 0):
        end_game()
        return
    if (next_box[0] == food[0] and next_box[1] == food[1]):
        increase_snake()
        draw_food()
    snake.insert(0,next_box)
    tail = snake[len(snake)-1]
    snake.pop(len(snake)-1)
    draw_box(next_box[0],next_box[1])
    clear_box(tail[0],tail[1])
    return
def increase_snake():
    n = 3
    for i in range(n):
        snake.append(snake[len(snake)-1])
    return
def millis():
    return time.time()*1000

#initialze snake
snake = [[height//2, width//2]]
draw_box(snake[0][0],snake[0][1])
draw_food()
pygame.display.update()

start = millis()
# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KeyDown:
            if (event.key == 32 and game_end):
                windowSurface.fill(BLACK)
                snake = [[height//2, width//2]]
                draw_box(snake[0][0],snake[0][1])
                draw_food()
                game_end = False
                pygame.display.update()
            if not game_end:
                if event.key == UP_KEY:
                    if (dir != DOWN):
                        dir = UP
                        game_running = True
                if event.key == DOWN_KEY:
                    if (dir != UP):
                        dir = DOWN
                        game_running = True
                if event.key == LEFT_KEY:
                    if (dir != RIGHT):
                        dir = LEFT
                        game_running = True
                if event.key == RIGHT_KEY:
                    if (dir != LEFT):
                        dir = RIGHT
                        game_running = True

    if (millis() - start >= tic) and game_running:
        start = millis()
        move_snake()
        pygame.display.update()
