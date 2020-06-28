import pygame 
import random
screen_width = 800
screen_height = 600
i = 35


wall = pygame.Rect(screen_width / 120 * 60, screen_height * 66/100, screen_width / 120 * 5, screen_height * 34/100)
ball = pygame.Rect(screen_width / 120 * 30.4,screen_height / 80 * 64,15 ,15)
line = pygame.Rect(screen_width / 120 * 28,screen_height / 80 * 65,50, 3)

target = pygame.image.load('Target(1).png')
target_rect = pygame.Rect(screen_width * i/48, screen_height * 70/72, target.get_width() - 2, 1)


ball_speed_x = 0
ball_speed_y = 0
ball_angle_increment = 0
ball_angle = 0
ball_velocity_increment = 0
ball_velocity = 1
gravity = 9.8
lives = 3

def ball_animation():
    global ball_speed_x, ball_speed_y, ball_angle, lives, i
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.bottom >= screen_height* 78/80:
        ball_speed_x = 0
        ball_speed_y = 0
        ball.bottom = screen_height / 80 * 64
        ball.left = screen_width / 120 * 30.4
        lives -= 1
    if ball.colliderect(line):
        ball_speed_y = 0
    if ball.colliderect(target_rect):
        ball_speed_x = 0
        ball_speed_y = 0
        completed()
    if ball.colliderect(wall):
        ball_speed_x = 0
        ball_speed_y = 0
        ball.bottom = screen_height / 80 * 64
        ball.left = screen_width / 120 * 30.4
        lives -= 1

    #if ball.top <= -15:
    #    ball_speed_x = 0
    #    ball_speed_y = 0
    #    ball.bottom = 650
    #    ball.left = 304
    #    lives -= 1

    if ball.right >= screen_width + 20:
        ball_speed_x = 0
        ball_speed_y = 0
        ball.bottom = screen_height / 80 * 64
        ball.left = screen_width / 120 * 30.4
        lives -= 1

def update1():
    global ball_velocity, ball_angle, lives, i
    if lives == 0:
        i = random.randrange(27, 36, 1)
        lives = 3
    if ball_velocity <= 7:
        ball_velocity = 7
    if ball_velocity > 20:
        ball_velocity = 20
    if ball_velocity <= 20:
        ball_velocity += ball_velocity_increment
    if ball_angle < -80:
        ball_angle = -80
    if ball_angle > 0:
        ball_angle = 0
    if ball_angle >= -80:
        ball_angle += ball_angle_increment