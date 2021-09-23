import pygame
import pickle
from os import path as ospath
from Node import Node
import heapq
import time

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
screen_text = ""

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('A Star')

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

environment = []  

# draw grids


def draw_grid():
    for grid in range(cols + 1):
        # vertical lines
        pygame.draw.line(screen, GREY, (grid * grid_size, 0),
                         (grid * grid_size, screen_height - margin))
        # horizontal lines
        pygame.draw.line(screen, GREY, (0, grid * grid_size),
                         (screen_width, grid * grid_size))


def draw():
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


def draw_text():
    img = FONT.render(screen_text, True, BLACK)
    screen.blit(img, (grid_size, screen_height - 60))


def get_h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return max(abs(x1 - x2), abs(y1 - y2))


def recreate_path(node):
    path = []
    current = node
    while current is not None:
        path.append(current.get_point())
        current = current.get_parent()

    return path[::-1]


def get_neighbors(node):
    neighbors = []

    for point in [(0, -1), (1, 0), (0, 1), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
        node_point = node.get_point()
        node_position = (node_point[0]+point[0], node_point[1]+point[1])

        # if out of range don't add to neighbor
        if node_position[0] > len(environment) - 1 or node_position[0] < 0 or node_position[1] > (
                len(environment[len(environment) - 1]) - 1) or node_position[1] < 0:
            continue

        # if obstacle don't add to neighbor
        if environment[node_position[1]][node_position[0]] == 1 or environment[node_position[1]][node_position[0]] == 2:
            continue

        new_node = Node(node_position)
        new_node.set_parent(node)
        neighbors.append(new_node)

    return neighbors


def a_star(start_point, end_point):
    count = 0
    start_node = Node(start_point)
    end_node = Node(end_point)
    opened = []
    closed = []

    start_node.set_h(get_h(start_point, end_point))
    heapq.heappush(opened, (start_node.get_f(), count, start_node))

    while len(opened) != 0:
        current_node = heapq.heappop(opened)[2]
        neighbors = get_neighbors(current_node)

        for neighbor in neighbors:

            neighbor.set_g(current_node.get_g() + 1)
            neighbor.set_h(get_h(neighbor.get_point(), end_point))

            if neighbor == end_node:
                return recreate_path(neighbor)

            # neighbor is already closed
            if len([visited_child for visited_child in closed if visited_child == neighbor]) > 0:
                continue

            # neighbor is in the opened list and g cost is already lower
            if len([i for i in opened if neighbor == i[2] and neighbor.get_g() >= i[2].get_g()]) > 0:
                continue

            count += 1
            heapq.heappush(opened, (neighbor.get_f(), count, neighbor))

        closed.append(current_node)

    return None


start = None
end = None
clicked = False
environment_number = input("Enter environment number :")
screen_text = f'Enivironment: {environment_number}'
# use environment number to update environment
if ospath.exists(f'environment{environment_number}_data'):
    pickle_in = open(f'environment{environment_number}_data', 'rb')
    environment = pickle.load(pickle_in)
else:
    for row in range(cols):
        r = [0] * cols
        environment.append(r)
    # create boundary
    for tile in range(0, cols):
        environment[cols - 1][tile] = 1
        environment[0][tile] = 1
        environment[tile][0] = 1
        environment[tile][cols - 1] = 1      

# main loop
run = True
while run:

    clock.tick(FPS)

    # draw background
    screen.fill(WHITE)
    screen.blit(bluebg, (0, 0))

    # show the grid and draw the level tiles
    draw_grid()
    draw()

    # text showing current environment
    draw_text()

    # event handler
    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            run = False

        # mouseclicks to select start and end grids
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
            pos = pygame.mouse.get_pos()
            x = pos[0] // grid_size
            y = pos[1] // grid_size
            grid = (x, y)

            # check that the coordinates are within the tile area
            if (x < cols and y < cols):
                # Left click on non-obstacle
                if pygame.mouse.get_pressed()[0] and environment[y][x] == 0:
                    if not start:
                        environment[y][x] = 4
                        start = grid
                    elif not end and grid != start:
                        environment[y][x] = 5
                        end = grid
                if pygame.mouse.get_pressed()[2]:  # Right click
                    if grid == start:
                        environment[y][x] = 0
                        start = None
                    elif grid == end:
                        environment[y][x] = 0
                        end = None

        if event.type == pygame.MOUSEBUTTONUP:
            clicked = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and start and end:
            start_time = time.time()
            path = a_star(start, end)
            end_time = time.time()
            print(f"Total time to find shortest path is {end_time - start_time}")
            if(path == None):
                screen_text = "Path Not Found!! "  
                environment[start[1]][start[0]] = 0
                start = None 
                environment[end[1]][end[0]] = 0
                end = None 
                clicked = False 
            else:
                screen_text = f'Enivironment: {environment_number}'
                print(path, len((path)))
                for p in path:
                    if (environment[p[1]][p[0]] == 0):
                        environment[p[1]][p[0]] = 3
                    elif (environment[p[1]][p[0]] == 4 or environment[p[1]][p[0]] == 5):
                        continue
                    elif (environment[p[1]][p[0]] == 1 or environment[p[1]][p[0]] == 2):
                        environment[p[1]][p[0]] = 6

        if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
            if ospath.exists(f'environment{environment_number}_data'):
                pickle_in = open(f'environment{environment_number}_data', 'rb')
                environment = pickle.load(pickle_in)
            else:
                environment = []
                for row in range(cols):
                    r = [0] * cols
                    environment.append(r)

                # create boundary
                for tile in range(0, cols):
                    environment[cols - 1][tile] = 1
                    environment[0][tile] = 1
                    environment[tile][0] = 1
                    environment[tile][cols - 1] = 1
            start = None
            end = None
            clicked = False

    # update game display window
    pygame.display.update()

pygame.quit()
