import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

ball = pygame.image.load("src/ball.png")

x = 0
y = 0
velocity_x = 2
velocity_y = 2

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    x += velocity_x
    y += velocity_y

    if x + ball.get_width() >= 640 or x <= 0:
        velocity_x = -velocity_x

    if y + ball.get_height() >= 480 or y <= 0:
        velocity_y = -velocity_y

    window.fill((0, 0, 0))
    window.blit(ball, (x, y))
    pygame.display.flip()

    clock.tick(60)
