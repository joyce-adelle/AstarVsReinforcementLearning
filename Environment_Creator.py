import pygame
import pickle
from os import path


pygame.init()
clock = pygame.time.Clock()

FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
FONT = pygame.font.SysFont('Futura', 24)


# game window
grid_size = 20
cols = 30
margin = 90
screen_width = grid_size * cols
screen_height = (grid_size * cols) + margin

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Environment Creator')

# image upload
wall = pygame.image.load("img/wall.png")
bluebg = pygame.image.load("img/bluebg.jpg")
save = pygame.image.load('img/save.png')
load = pygame.image.load('img/load.png')

bluebg = pygame.transform.scale(bluebg, (screen_width, screen_height - margin))

wall.convert()
bluebg.convert()
save.convert()
load.convert()

# define game variables
clicked = False
environment = 1

# create empty environment list
environment_data = []
for row in range(cols):
    r = [0] * cols
    environment_data.append(r)

# create boundary
for tile in range(0, cols):
    environment_data[cols - 1][tile] = 1
    environment_data[0][tile] = 1
    environment_data[tile][0] = 1
    environment_data[tile][cols - 1] = 1

# draw grids


def draw_grid():
    for grid in range(cols + 1):
        # vertical lines
        pygame.draw.line(screen, GREY, (grid * grid_size, 0),
                         (grid * grid_size, screen_height - margin))
        # horizontal lines
        pygame.draw.line(screen, GREY, (0, grid * grid_size),
                         (screen_width, grid * grid_size))


def draw_environment():
    for row in range(cols):
        for col in range(cols):
            if environment_data[row][col] > 0:
                if environment_data[row][col] == 1:
                    # walls
                    img = pygame.transform.scale(wall, (grid_size, grid_size))
                    screen.blit(img, (col * grid_size, row * grid_size))
                if environment_data[row][col] == 2:
                    # barriers
                    screen.fill(BLACK, pygame.Rect(col * grid_size,
                                row * grid_size, grid_size, grid_size))

# function for outputting text onto the screen


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


def draw_save():
    action = False
    rect = save.get_rect()
    rect.center = 470, 650
    clicked = False

    # get mouse position
    pos = pygame.mouse.get_pos()

    # check mouseover and clicked conditions
    if rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == 1 and clicked == False:
        action = True
        clicked = True

    if pygame.mouse.get_pressed()[0] == 0:
        clicked = False

        # draw button
    screen.blit(save, (rect.x, rect.y))

    return action


def draw_load():
    action = False
    rect = load.get_rect()
    rect.center = 560, 650
    clicked = False

    # get mouse position
    pos = pygame.mouse.get_pos()

    # check mouseover and clicked conditions
    if rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == 1 and clicked == False:
        action = True
        clicked = True

    if pygame.mouse.get_pressed()[0] == 0:
        clicked = False

        # draw button
    screen.blit(load, (rect.x, rect.y))

    return action


# main game loop
run = True
while run:

    clock.tick(FPS)

    # draw background
    screen.fill(WHITE)
    screen.blit(bluebg, (0, 0))

    # load and save environment
    if draw_save():
        # print(environment_data)
        # save environment data
        pickle_out = open(f'environment{environment}_data', 'wb')
        pickle.dump(environment_data, pickle_out)
        pickle_out.close()

    # load in environment data
    if draw_load() and path.exists(f'environment{environment}_data'):
        pickle_in = open(f'environment{environment}_data', 'rb')
        environment_data = pickle.load(pickle_in)

    # show the grid and draw the environment tiles
    draw_grid()
    draw_environment()

    # text showing current environment
    draw_text(f'Enivironment: {environment}', FONT,
              BLACK, grid_size, screen_height - 60)
    draw_text('Press UP or DOWN keys to set environment number',
              FONT, BLACK, grid_size, screen_height - 40)

    # event handler
    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            run = False
        # mouseclicks to change tiles
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
            pos = pygame.mouse.get_pos()
            x = pos[0] // grid_size
            y = pos[1] // grid_size
            # check that the coordinates are within the tile area
            if x < cols and y < cols:
                # update tile value
                if pygame.mouse.get_pressed()[0]:
                    environment_data[y][x] += 1
                    if environment_data[y][x] > 2:
                        environment_data[y][x] = 0
                elif pygame.mouse.get_pressed()[2]:
                    environment_data[y][x] -= 1
                    if environment_data[y][x] < 0:
                        environment_data[y][x] = 2
        if event.type == pygame.MOUSEBUTTONUP:
            clicked = False
        # up and down key presses to change environment number
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                environment += 1
            elif event.key == pygame.K_DOWN and environment > 1:
                environment -= 1

    # update game display window
    pygame.display.update()

pygame.quit()
