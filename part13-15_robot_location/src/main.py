import pygame
import random

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("src/robot.png")

x = random.randint(0, 640 - robot.get_width())
y = random.randint(0, 480 - robot.get_height())

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if x <= event.pos[0] <= x + robot.get_width() and y <= event.pos[1] <= y + robot.get_height():
                x = random.randint(0, 640 - robot.get_width())
                y = random.randint(0, 480 - robot.get_height())

        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    clock.tick(60)