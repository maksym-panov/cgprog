# Variant 14. Task #3 (#2 in task list)
# Build a watch by the given template
import math
import pygame as pg 
from pygame.locals import *

pg.init()

width = 640
height = 480
width_half = width // 2
height_half = height // 2 

screen = pg.display.set_mode((width, height))
pg.display.set_caption("The clock")
font = pg.font.SysFont("Castellar", 50)
screen.fill([255, 255, 255])

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()

    pg.draw.circle(screen, (0, 0, 0), (320, 240), 8, 0)
    pg.draw.polygon(screen, (0, 0, 0), [(320, 315), (327, 300), (313, 300)], 0)
    pg.draw.polygon(screen, (0, 0, 0), [(440, 240), (415, 235), (415, 245)], 0)

    for i in range(60):
        line = math.radians(i * 30 - 90)
        length_line = 14 
        x_starting = int(math.cos(line) * 150 + width_half)
        y_starting = int(math.sin(line) * 150 + height_half)
        x_ending = int(math.cos(line) * (150 - length_line) + width_half)
        y_ending = int(math.sin(line) * (150 - length_line) + height_half)
        pg.draw.line(screen, (0, 0, 0), (x_starting, y_starting), (x_ending, y_ending), 2)
        

    for i in range(1, 13):
        numbers = math.radians(i * 30 - 90)
        x = int(math.cos(numbers) * 190 + width_half)
        y = int(math.sin(numbers) * 190 + height_half)
        number = font.render(str(i), True, (0, 0, 0))
        screen.blit(number, (x - number.get_width() // 2, y - number.get_height() // 2))

    hour = math.radians(90)
    length_hour = 60
    x_ending_hour = int(math.cos(hour) * length_hour + width_half)
    y_ending_hour = int(math.sin(hour) * length_hour + height_half)
    pg.draw.line(screen, (0, 0, 0), (width_half, height_half), (x_ending_hour, y_ending_hour), 4)

    minutes = math.radians(0)
    length_minutes = 110
    x_ending_minutes = int(math.cos(minutes) * length_minutes + width_half)
    y_ending_minutes = int(math.sin(minutes) * length_minutes + height_half)
    pg.draw.line(screen, (0, 0, 0), (width_half, height_half), (x_ending_minutes, y_ending_minutes), 3)

    pg.display.flip()
    pg.time.wait(100)

