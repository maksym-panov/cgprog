# Variant 14. Task #1 (#5 in task list)
# Build a rounded_rectangle with rounded corners,
# trapezoid and a rhombus
import pygame as pg
from pygame.locals import *

WIDTH = 640
HEIGHT = 480

pg.init()
SCREEN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Task #3")

BG_COLOR = (87, 57, 87)
AXIS_COLOR = (233, 255, 0)
RECT_INNER_COLOR = (0, 255, 17)
RECT_OUTER_COLOR = (255, 175, 5)
TRAP_INNER_COLOR = (165, 42, 42)
TRAP_OUTER_COLOR = (255, 255, 0)
RHOMBUS_INNER_COLOR = (0, 100, 0)
RHOMBUS_OUTER_COLOR = (255, 165, 0)

def build_coordinate_system():
    SCREEN.fill(BG_COLOR)
    pg.draw.line(SCREEN, AXIS_COLOR, (640, 240), (0  , 240), 1) 
    pg.draw.line(SCREEN, AXIS_COLOR, (320,   0), (320, 480), 1)
    pg.display.flip()

def build_rounded_rectangle():
    rectangle = pg.Rect(360, 40, 240, 160)
    pg.draw.rect(SCREEN, RECT_INNER_COLOR, rectangle, 0, 10, 10, 10, 10)
    pg.draw.rect(SCREEN, RECT_OUTER_COLOR, rectangle, 4, 10, 10, 10, 10)
    pg.display.flip()

def build_trapezoid():
    trapezoid = [(110, 70), (50, 170), (270, 170), (210, 70)]
    pg.draw.polygon(SCREEN, TRAP_INNER_COLOR, trapezoid, 0)
    pg.draw.polygon(SCREEN, TRAP_OUTER_COLOR, trapezoid, 4)
    pg.display.flip()

def build_rhombus():
    rhombus = [(160, 260), (60, 360), (160, 460), (260, 360)]
    pg.draw.polygon(SCREEN, RHOMBUS_INNER_COLOR, rhombus, 0)
    pg.draw.polygon(SCREEN, RHOMBUS_OUTER_COLOR, rhombus, 3)
    pg.draw.line(SCREEN, RHOMBUS_OUTER_COLOR, [160, 260], [160, 460], 1)
    pg.draw.line(SCREEN, RHOMBUS_OUTER_COLOR, [60, 360], [260, 360], 1)
    pg.display.flip()

build_coordinate_system()
build_rounded_rectangle()
build_trapezoid()
build_rhombus()

while True:
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit() 
            break

