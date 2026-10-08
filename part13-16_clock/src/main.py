import pygame
import math
from datetime import datetime

pygame.init()
pygame.display.set_caption("Great Adventure")
display = pygame.display.set_mode((640, 480))
display.fill((0, 0, 0))

# Center of the clock
center_x = 320
center_y = 240

# Clock radius
radius = 180

pygame.draw.circle(display, (255, 0, 0), (center_x, center_y), 200)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    now = datetime.now()
    pygame.display.set_caption(now.strftime("%H:%M:%S"))

    pygame.draw.circle(display, (0, 0, 0), (center_x, center_y), 195)
    pygame.draw.circle(display, (255, 0, 0), (center_x, center_y), 10)

    hours = now.hour
    minutes = now.minute
    seconds = now.second

    # Calculate angles
    second_angle = seconds * 2 * math.pi / 60
    minute_angle = minutes * 2 * math.pi / 60
    hour_angle = (hours % 12) * 2 * math.pi / 12 + minute_angle / 12

    # Second hand
    second_x = center_x + math.sin(second_angle) * 170
    second_y = center_y - math.cos(second_angle) * 170

    pygame.draw.line(display, (0, 0, 255), (center_x, center_y), (second_x, second_y), 1)

    # Minute hand
    minute_x = center_x + math.sin(minute_angle) * 140
    minute_y = center_y - math.cos(minute_angle) * 140

    pygame.draw.line(display, (0, 0, 255), (center_x, center_y), (minute_x, minute_y), 2)

    # Hour hand
    hour_x = center_x + math.sin(hour_angle) * 110
    hour_y = center_y - math.cos(hour_angle) * 110

    pygame.draw.line(display, (0, 0, 255), (center_x, center_y), (hour_x, hour_y), 4)

    pygame.display.flip()
    clock.tick(1)
