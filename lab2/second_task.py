import pygame as pg
from pygame.locals import QUIT
import random as rnd

WIDTH = 640
HEIGHT = 480
CENTER_ABSCISSA = WIDTH // 2
CENTER_ORDINATE = HEIGHT // 2

pg.init()
SCREEN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Task #2")

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

def draw_octet(center, color, x, y):
    ox, oy = center[0], center[1]
    SCREEN.set_at(rel_coord(ox + x, oy + y), color)
    SCREEN.set_at(rel_coord(ox + x, oy - y), color)
    SCREEN.set_at(rel_coord(ox - x, oy + y), color)
    SCREEN.set_at(rel_coord(ox - x, oy - y), color)
    SCREEN.set_at(rel_coord(ox + y, oy + x), color)
    SCREEN.set_at(rel_coord(ox + y, oy - x), color)
    SCREEN.set_at(rel_coord(ox - y, oy + x), color)
    SCREEN.set_at(rel_coord(ox - y, oy - x), color)

def draw_michener_circle(center, radius):
    x, y = 0, radius
    param_P = 1.25 - radius
    color = (rnd.randint(0, 255), rnd.randint(0, 255), rnd.randint(0, 255))
    while x <= y:
        draw_octet(center, color, x, y)
        x += 1
        if param_P < 0:
            param_P += 2*x - 1
        else:
            y -= 1
            param_P += 2*(x - y) + 1
    pg.display.flip()

draw_x_axis()
draw_y_axis()

center = (-50, -50)
radius = 100
draw_michener_circle(center, radius)

center = (CENTER_ABSCISSA - 110, CENTER_ORDINATE + 110)
radius = 100
pg.draw.circle(SCREEN, (100, 100, 100), center, radius, 1)
pg.display.flip()

center = (200, 200)
radius = 50
draw_michener_circle(center, radius)

center = (133, -120)
radius = 79
draw_michener_circle(center, radius)

center = (-50, 210)
radius = 30
draw_michener_circle(center, radius)

while True:
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            break
