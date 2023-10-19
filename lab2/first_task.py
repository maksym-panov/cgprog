import pygame as pg
from pygame.locals import QUIT
import random as rnd

WIDTH = 640
HEIGHT = 480
CENTER_ABSCISSA = WIDTH // 2
CENTER_ORDINATE = HEIGHT // 2

pg.init()
SCREEN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Task #1")

def draw_x_axis():
    pg.draw.line(
        SCREEN, 
        (255, 255, 255), 
        (0, HEIGHT // 2), 
        (WIDTH, HEIGHT // 2)
    )
    pg.display.flip()

def draw_y_axis():
    pg.draw.line(
        SCREEN,
        (255, 255, 255),
        (WIDTH // 2, 0),
        (WIDTH //2, HEIGHT)
    )
    pg.display.flip()

def rel_coord(x, y):
    return (CENTER_ABSCISSA + x, CENTER_ORDINATE - y)

def sign(a):
    return -1 if a < 0 else 1

def draw_bresenham_line(f_point, s_point):
    x1, y1 = f_point[0], f_point[1]
    x2, y2 = s_point[0], s_point[1]
    dx, dy = x2 - x1, y2 - y1
    color = (rnd.randint(0, 255), rnd.randint(0, 255), rnd.randint(0, 255))
    
    if dx == 0:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            SCREEN.set_at(rel_coord(x1, y), color)
        pg.display.flip()
        return

    x_axis = abs(dx) > abs(dy)
    iterations = 1 + dx if x_axis else dy
    x, y = x1, y1
    var_buffer = 0 
    
    while iterations:
        SCREEN.set_at(rel_coord(x, y), color)
        x += sign(dx) * 1 if x_axis else 0
        y += sign(dy) * 1 if not x_axis else 0
        var_buffer += abs(dy/dx if x_axis else dx/dy)
        if var_buffer >= 0.5:
            var_buffer -= 1
            x += sign(dx) * 1 if not x_axis else 0
            y += sign(dy) * 1 if x_axis else 0

        iterations -= 1

    pg.display.flip()

draw_x_axis()
draw_y_axis()
draw_bresenham_line((-200, -200), (200, 200))
draw_bresenham_line((-100, 0), (100, 0))
draw_bresenham_line((0, 150), (0, -150))
draw_bresenham_line((-127, 39), (220, -91))
draw_bresenham_line((99, -190), (20, 170))
draw_bresenham_line((-200, 20), (-100, 200))

pg.draw.line(
    SCREEN, 
    (255, 0, 0), 
    (CENTER_ABSCISSA + -200 + 20, CENTER_ORDINATE + -20), 
    (CENTER_ABSCISSA + -100 + 20, CENTER_ORDINATE + -200)
)
pg.display.flip()

while True:
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            break
