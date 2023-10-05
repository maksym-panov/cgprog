# Variant 14. Task #1 (#5 in task list)
# Build a circle with two points - radius 
# and random point of the circle
import pygame as pg
from pygame.locals import *
import math

WIDTH = 1366
HEIGHT = 768

pg.init()
SCREEN = pg.display.set_mode((WIDTH, HEIGHT));
pg.display.set_caption("Task #1")

def length(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def build_circle(points):
    radius = length(points[0], points[1])
    print(
      "Building a circle with center ", 
      points[0], 
      " and radius ", 
      radius 
    )
    pg.draw.circle(
        SCREEN, 
        (255, 255, 255), 
        points[0], 
        radius,
        2, True, True, True, True
    )

points = []
hasBeenDrawn = False
while True: 
    point = None
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            break
        if event.type == MOUSEBUTTONDOWN:
            point = pg.mouse.get_pos()
            points.append(point)
    if not hasBeenDrawn and len(points) > 1:
        build_circle(points)
        hasBeenDrawn = True
        pg.display.flip()
        pg.time.wait(100)
