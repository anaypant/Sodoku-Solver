import pygame
import sys
from settings import *
from utils import *
from solver import *
import keyboard
import copy

pygame.init()
game_over = False
screen = pygame.display.set_mode((GUI, GUI))
grid = generate_board()

solved_grid = copy.deepcopy(solve_sudoku(copy.deepcopy(grid)))
grid_stored = copy.deepcopy(grid)


font = pygame.font.Font("freesansbold.ttf", int(CELL_W * 0.8))
texts = []
selected = [-1, -1]

if solved_grid == -1:
    print("Problem")
    quit()

for i in range(10):
    texts.append(font.render(str(i), True, (0, 0, 0)))


def get_pressed():
    for i in range(1, 10):
        if keyboard.is_pressed(str(i)):
            return i
    return 0


while True:
    screen.fill((128, 128, 128))
    # draw the boxes and lines

    if not game_over:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                mX = mouse[1] // CELL_W
                mY = mouse[0] // CELL_W
                selected = [mX, mY]

            if event.type == pygame.QUIT:
                sys.exit()

        key = get_pressed()
        if key != 0 and selected != [-1, -1]:
            if solved_grid[selected[0]][selected[1]] == key:
                grid[selected[0]][selected[1]] = key

                if grid == solved_grid:
                    pygame.display.set_caption("Congrats!")
                    game_over = True
            else:
                pygame.display.set_caption("Incorrect!")

        if keyboard.is_pressed("s"):
            grid = solved_grid[:]
        elif keyboard.is_pressed("c"):
            grid = grid_stored[:]
    for col in range(len(grid)):
        for row in range(len(grid[col])):
            # color = (128, 128, 128)
            if row == selected[0] and col == selected[1]:
                pygame.draw.rect(
                    screen,
                    (255, 190, 190),
                    [col * CELL_W, row * CELL_W, CELL_W, CELL_W],
                )

            elif (
                selected != [-1, -1]
                and grid[row][col] == grid[selected[0]][selected[1]]
                and grid[row][col] != 0
            ):
                pygame.draw.rect(
                    screen,
                    (255, 130, 130),
                    [col * CELL_W, row * CELL_W, CELL_W, CELL_W],
                )
            elif row == selected[0] or col == selected[1]:
                pygame.draw.rect(
                    screen,
                    (160, 160, 160),
                    [col * CELL_W, row * CELL_W, CELL_W, CELL_W],
                )

            pygame.draw.rect(
                screen, (72, 72, 72), [col * CELL_W, row * CELL_W, CELL_W, CELL_W], 2
            )
            if grid[row][col] != 0:
                screen.blit(
                    texts[grid[row][col]],
                    (col * CELL_W + CELL_W // 4, row * CELL_W + CELL_W // 5),
                )

            if (row + 1) % 3 == 0:
                pygame.draw.line(
                    screen,
                    (0, 0, 0),
                    [0, (row + 1) * CELL_W],
                    [GUI, (row + 1) * CELL_W],
                    width=4,
                )

    for col in range(9):
        if (col + 1) % 3 == 0:
            pygame.draw.line(
                screen,
                (0, 0, 0),
                [(col + 1) * CELL_W, 0],
                [(col + 1) * CELL_W, GUI],
                width=4,
            )

    pygame.display.update()
