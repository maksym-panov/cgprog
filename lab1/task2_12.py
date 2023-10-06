# Variant 14. Task #2 (#12 in task list)
# Build a hexagon based on its 
# circumscribed circle
import pygame as pg
from pygame.locals import *
import math
from sympy import Circle, intersection
import time

WIDTH = 1366
HEIGHT = 768

pg.init()
SCREEN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Task #2")

def length(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def circle_circle_intersection(o1, p1, o2, p2):
    r1, r2 = length(o1, p1), length(o2, p2)
    c1, c2 = Circle(o1, r1), Circle(o2, r2)
    inter = intersection(c1, c2)
    p1 = list(inter[0].evalf())
    p1[0] = math.ceil(p1[0])
    p1[1] = math.ceil(p1[1])
    p2 = list(inter[1].evalf())
    p2[0] = math.ceil(p2[0])
    p2[1] = math.ceil(p2[1])
    return [p1, p2]

def build_point(p):
    pg.draw.circle(SCREEN, (0, 255, 0), p, 5, 0)

def build_circle(o, p):
    r = length(o, p)
    pg.draw.circle(SCREEN, (255, 255, 255), o, r, 1)

def build_side(p1, p2):
    pg.draw.line(SCREEN, (255, 0, 0), p1, p2, 3)

def points_equals(p1, p2):
    return (
        p1 != None and p2 != None and 
        abs(p1[0] - p2[0]) < 5 and 
        abs(p1[1] - p2[1]) < 5
    )


def build_hexagon(o, p):
    prev_p = None
    build_circle(o, p)
    pg.display.flip()
    time.sleep(1)
    for _ in range(6):
        inter = circle_circle_intersection(o, p, p, o)
        build_circle(p, o)
        pg.display.flip()
        time.sleep(1)
        print(inter)
        build_side(p, inter[0])
        build_side(p, inter[1])
        pg.display.flip()
        time.sleep(1)
        if (points_equals(inter[0], prev_p)):
            prev_p = p
            p = inter[1]
        else:
            prev_p = p
            p = inter[0]
        

points = []
while True:
    point = None
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            break
        if event.type == MOUSEBUTTONDOWN:
            point = pg.mouse.get_pos()
            points.append(point)
            build_point(point)
            pg.display.flip()
    if len(points) > 1:
        A, B = points[0], points[1]
        O = [(A[0] + B[0]) // 2, (A[1] + B[1]) // 2]
        build_hexagon(O, points[1])
        points = []
        pg.display.flip()









