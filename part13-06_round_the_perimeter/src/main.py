import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("src/robot.png")

x = 0
y = 0
velocity = 1
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    if velocity > 0 and x + robot.get_width() < 640:
        x += velocity
    elif velocity > 0 and y + robot.get_height() < 480:
        y += velocity
    elif velocity > 0:
        velocity = -velocity
    elif velocity < 0 and x > 0:
        x += velocity
    elif velocity < 0 and y > 0:
        y += velocity
    else:
        velocity = -velocity

    clock.tick(60)
