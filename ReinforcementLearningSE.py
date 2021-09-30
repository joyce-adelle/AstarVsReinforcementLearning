import pygame
import pickle
from os import path as ospath
import numpy as np
import time
from utilities import *

pygame.init()
pygame.display.set_caption('Reinforcement Learning')

FONT = pygame.font.SysFont('Futura', 24)
screen_text = ""

# a 3D numpy array to hold the current Q-values for each state and action pair: Q(s, a) and initialized to 0.
q_table = np.zeros((cols, cols, 8))
# 2D numpy array to hold rewards, intialized to -100
rewards = np.full((cols, cols), -100)
# number of iterations for learning
episode = 20000


def draw_text():
    img = FONT.render(screen_text, True, BLACK)
    screen.blit(img, (grid_size, screen_height - 60))

'''
    determines if specified grid is a terminal state
'''
def is_terminal_state(grid):
    if rewards[grid[1], grid[0]] == -1.:
        return False
    else:
        return True

'''
    determines action using epsilon greedy algorithm
'''
def get_next_action(grid):
    if np.random.random() < epsilon:
        actions = np.where(q_table[grid[1], grid[0]] ==
                           np.max(q_table[grid[1], grid[0]]))[0]
        return np.random.choice(actions)
    else:
        return np.random.randint(8)

'''
    gets next grid based on action
'''
def get_next(grid, action):
    row, col = grid
    switch = {
        0: (row + 0, col + -1),
        1: (row + 1, col + 0),
        2: (row + 0, col + 1),
        3: (row + -1, col + 0),
        4: (row + 1, col + -1),
        5: (row + 1, col + 1),
        6: (row + -1, col + 1),
        7: (row + -1, col + -1)
    }

    next_grid = switch.get(action, (row, col))

    if next_grid[0] > cols - 1 or next_grid[0] < 0 or next_grid[1] > (cols - 1) or next_grid[1] < 0:
        return (row, col)
    return next_grid

'''
    learns environment
'''
def learn(start):
    for _ in range(episode):
        grid = start

        while not is_terminal_state(grid):
            action = get_next_action(grid)
            old_grid = grid
            grid = get_next(grid, action)

            reward = rewards[grid[1], grid[0]]
            old_q = q_table[
                old_grid[1], old_grid[0], action]
            temporal_difference = reward + (discount_factor *
                                            np.max(q_table[grid[1], grid[0]])) - old_q

            new_q = old_q + (learning_rate * temporal_difference)
            q_table[old_grid[1], old_grid[0],
                    action] = new_q

    print('Training completed!')

'''
    get an optimal path
'''
def get_shortest_path(start_grid):
    if is_terminal_state(start_grid):
        return []

    else:
        current_grid = start_grid
        path = []
        path.append(current_grid)
        while not is_terminal_state(current_grid):
            action = np.argmax(q_table[current_grid[1], current_grid[0]])
            current_grid = get_next(current_grid, np.min(action))
            if(current_grid not in path):
                path.append(current_grid)
            else:
                return None

        return path

'''
    utility function to print all optimal paths recursively
'''
def print_all_shortest_paths_util(current, end, visited, path, total_num_of_alternative):
    visited[current[1], current[0]] = True
    path.append(current)

    if total_num_of_alternative[0] >= 10 and current[0] == end[0] and current[1] == end[1]:
        total_num_of_alternative[0] += 1

    elif current[0] == end[0] and current[1] == end[1]:
        print(path, len(path))
        total_num_of_alternative[0] += 1
    else:
        actions = np.where(q_table[current[1], current[0]] ==
                           np.max(q_table[current[1], current[0]]))[0]
        grids = []
        for action in actions:
            grids.append(get_next(current, action))

        for i in grids:
            if visited[i[1], i[0]] == False and total_num_of_alternative[0] <= 50000:
                print_all_shortest_paths_util(
                    i, end, visited, path, total_num_of_alternative)

    path.pop()
    visited[current[1], current[0]] = False

'''
    prints all optimal paths from source to destination
'''
def print_all_shortest_paths(start, end):
    visited = np.full((cols, cols), False)
    path = []
    total_num_of_alternative = [0]

    print_all_shortest_paths_util(
        start, end, visited, path, total_num_of_alternative)
    if total_num_of_alternative[0] <= 50000:
        print("total number of alternative paths ",
              total_num_of_alternative[0])
    else:
        print("total number of alternative paths greater than 50000")


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

for row in range(cols):
    for col in range(cols):
        if environment[row][col] == 0:
            rewards[row, col] = -1

# main loop
run = True
while run:

    clock.tick(FPS)

    # draw background
    screen.fill(WHITE)
    screen.blit(bluebg, (0, 0))

    # show the grid and draw the level tiles
    draw_grid()
    draw(environment)

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
            print("grid  ", grid)
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
                        # set the reward for the goal to 100
                        rewards[y, x] = 100
                if pygame.mouse.get_pressed()[2]:  # Right click
                    if grid == start:
                        environment[y][x] = 0
                        start = None
                    elif grid == end:
                        environment[y][x] = 0
                        rewards[y, x] = -1.
                        end = None

        if event.type == pygame.MOUSEBUTTONUP:
            clicked = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and start and end:
            start_time = time.time()
            learn(start)
            end_time = time.time()
            print(f"Total learning time is {end_time - start_time}")
            start_time = time.time()
            path = get_shortest_path(start)
            end_time = time.time()
            print(
                f"Total time to find shortest path is {end_time - start_time}")
            if(path == None):
                screen_text = "Path Not Found!! "
                environment[start[1]][start[0]] = 0
                start = None
                clicked = False
            else:
                screen_text = f'Enivironment: {environment_number}'
                for p in path:
                    if (environment[p[1]][p[0]] == 0):
                        environment[p[1]][p[0]] = 3
                    elif (environment[p[1]][p[0]] == 4 or environment[p[1]][p[0]] == 5):
                        continue
                    elif (environment[p[1]][p[0]] == 1 or environment[p[1]][p[0]] == 2):
                        environment[p[1]][p[0]] = 6

                print("path ", path, len(path))
                print_all_shortest_paths(start, end)

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
            if end:
                rewards[end[1], end[0]] = -1

            q_table = np.zeros((cols, cols, 8))
            start = None
            end = None
            is_trained = False
            clicked = False

    # update game display window
    pygame.display.update()

pygame.quit()
