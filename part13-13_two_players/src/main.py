import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot_image = pygame.image.load("src/robot.png")

class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    
    def to_right(self):
        if self.x < 640 - robot_image.get_width():
            self.x += 2
    def to_left(self):
        if self.x > 0:
            self.x -= 2
    def to_down(self):
        if self.y < 480 - robot_image.get_height():
            self.y += 2
    def to_up(self):
        if self.y > 0:
            self.y -= 2
    
    def update(self):
        if self.moving_right:
            self.to_right()
        if self.moving_left:
            self.to_left()
        if self.moving_up:
            self.to_up()
        if self.moving_down:
            self.to_down()

robot1 = Robot(50, 50)
robot2 = Robot(640 - 50 - robot_image.get_width(), 480 - 50 - robot_image.get_height())

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            # 1st robot
            if event.key == pygame.K_LEFT:
                robot1.moving_left = True
            if event.key == pygame.K_RIGHT:
                robot1.moving_right = True
            if event.key == pygame.K_UP:
                robot1.moving_up = True
            if event.key == pygame.K_DOWN:
                robot1.moving_down = True
            # 2nd robot
            if event.key == pygame.K_a:
                robot2.moving_left = True
            if event.key == pygame.K_d:
                robot2.moving_right = True
            if event.key == pygame.K_w:
                robot2.moving_up = True
            if event.key == pygame.K_s:
                robot2.moving_down = True

        if event.type == pygame.KEYUP:
            # 1st robot
            if event.key == pygame.K_LEFT:
                robot1.moving_left = False
            if event.key == pygame.K_RIGHT:
                robot1.moving_right = False
            if event.key == pygame.K_UP:
                robot1.moving_up = False
            if event.key == pygame.K_DOWN:
                robot1.moving_down = False
            # 2nd robot
            if event.key == pygame.K_a:
                robot2.moving_left = False
            if event.key == pygame.K_d:
                robot2.moving_right = False
            if event.key == pygame.K_w:
                robot2.moving_up = False
            if event.key == pygame.K_s:
                robot2.moving_down = False
            
        if event.type == pygame.QUIT:
            exit()

    robot1.update()
    robot2.update()

    window.fill((0, 0, 0))
    window.blit(robot_image, (robot1.x, robot1.y))
    window.blit(robot_image, (robot2.x, robot2.y))
    pygame.display.flip()

    clock.tick(60)
