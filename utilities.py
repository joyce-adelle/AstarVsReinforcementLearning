import pygame

clock = pygame.time.Clock()

FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)

# game window
grid_size = 20
cols = 30
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
discount_factor = 0.95
learning_rate = 0.9

