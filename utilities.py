import pygame

clock = pygame.time.Clock()

FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)

# game window
grid_size = 30
cols = 20
margin = 90
screen_width = grid_size * cols
screen_height = (grid_size * cols) + margin

screen = pygame.display.set_mode((screen_width, screen_height))

# image upload
wall = pygame.image.load("img/wall.png")
walk = pygame.image.load("img/footprints.png")
wrong = pygame.image.load("img/fos.png")
startimg = pygame.image.load("img/walk.png")
finish = pygame.image.load("img/finish.png")
bluebg = pygame.image.load("img/bluebg.jpg")

bluebg = pygame.transform.scale(bluebg, (screen_width, screen_height - margin))

wall.convert()
walk.convert()
wrong.convert()
startimg.convert()
finish.convert()
bluebg.convert()

epsilon = 0.9
discount_factor = 0.8
learning_rate = 0.95

# draw grids
def draw_grid():
    for grid in range(cols + 1):
        # vertical lines
        pygame.draw.line(screen, GREY, (grid * grid_size, 0),
                         (grid * grid_size, screen_height - margin))
        # horizontal lines
        pygame.draw.line(screen, GREY, (0, grid * grid_size),
                         (screen_width, grid * grid_size))


def draw(environment):
    for row in range(cols):
        for col in range(cols):
            if environment[row][col] == 1:
                # walls
                img = pygame.transform.scale(wall, (grid_size, grid_size))
                screen.blit(img, (col * grid_size, row * grid_size))
            elif environment[row][col] == 2:
                # barriers
                screen.fill(BLACK, pygame.Rect(col * grid_size,
                                               row * grid_size, grid_size, grid_size))
            elif environment[row][col] == 3:
                # path
                img = pygame.transform.scale(walk, (grid_size, grid_size))
                screen.blit(img, (col * grid_size, row * grid_size))

            elif environment[row][col] == 4:
                # start
                img = pygame.transform.scale(startimg, (grid_size, grid_size))
                screen.blit(img, (col * grid_size, row * grid_size))

            elif environment[row][col] == 5:
                # finish
                img = pygame.transform.scale(finish, (grid_size, grid_size))
                screen.blit(img, (col * grid_size, row * grid_size))

            elif environment[row][col] == 6:
                # wrong path
                img = pygame.transform.scale(wrong, (grid_size, grid_size))
                screen.blit(img, (col * grid_size, row * grid_size))

