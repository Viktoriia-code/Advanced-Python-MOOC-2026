import pygame
import random

pygame.init()
window = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Asteroidit")

rock = pygame.image.load("src/rock.png")
robot = pygame.image.load("src/robot.png")

rocks = []
points = 0
robot_x = 0
robot_y = 480 - robot.get_height()

to_right = False
to_left = False
game_over = False

clock = pygame.time.Clock()
game_font = pygame.font.SysFont("Arial", 28)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False

    if not game_over:
        # Move robot
        if to_right and robot_x < 640 - robot.get_width():
            robot_x += 2
        if to_left and robot_x > 0:
            robot_x -= 2

        # Create new rocks
        if random.random() < 0.008:
            x = random.randint(0, 640 - rock.get_width())
            rocks.append([x, -rock.get_height()])

        robot_rect = pygame.Rect(
            robot_x, robot_y,
            robot.get_width(), robot.get_height()
        )

        # Move rocks and check collisions
        for r in rocks[:]:
            r[1] += 1

            rock_rect = pygame.Rect(
                r[0], r[1],
                rock.get_width(), rock.get_height()
            )

            if robot_rect.colliderect(rock_rect):
                rocks.remove(r)
                points += 1

            elif r[1] + rock.get_height() >= 480:
                game_over = True

    # Draw everything
    window.fill((0, 0, 0))

    for r in rocks:
        window.blit(rock, (r[0], r[1]))

    window.blit(robot, (robot_x, robot_y))

    text = game_font.render(f"Points: {points}", True, (255, 0, 0))
    window.blit(text, (520, 30))

    if game_over:
        message = game_font.render("Game Over!", True, (255, 0, 0))
        window.blit(message, (250, 200))

    pygame.display.flip()
    clock.tick(60)
