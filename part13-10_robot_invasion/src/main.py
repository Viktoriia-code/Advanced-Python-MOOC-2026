import pygame
import random

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("src/robot.png")

robots = []

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    if random.random() < 0.02:
        x = random.randint(0, 640 - robot.get_width())
        if x < 320:
            velocity_x = -2
        else:
            velocity_x = 2
        robots.append([x, -robot.get_height(), 2, velocity_x])

    for r in robots:
        if r[1] + robot.get_height() < 480:
            r[1] += r[2]
        else:
            r[0] += r[3]

    robots = [r for r in robots if -robot.get_width() < r[0] < 640]

    window.fill((0, 0, 0))

    for r in robots:
        window.blit(robot, (r[0], r[1]))

    pygame.display.flip()

    clock.tick(60)