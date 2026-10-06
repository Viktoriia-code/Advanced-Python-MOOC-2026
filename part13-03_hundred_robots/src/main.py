import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))
window.fill((0, 0, 0))

robot = pygame.image.load("src/robot.png")
width = robot.get_width()
height = robot.get_height()

for i in range(1, 11):
    for y in range(1, 11):
        window.blit(robot, (i * 10 + y * (width - 10), height + i * 20))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
