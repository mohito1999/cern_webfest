import ball_animations as ba
import pygame
import sys
import math

pygame.init()

screen_width = 800
screen_height = 600
i=35

launcher = pygame.image.load('../Assets/Projectile Launcher.png')
#launcher.set_colorkey((0,0,0))
background = pygame.image.load('../Assets/ChallengeRoom1.jpg')

target = pygame.image.load('../Assets/Target(1).png')
target_rect = pygame.Rect(screen_width * i/48, screen_height * 70/72, target.get_width() - 2, 1)

wall = pygame.Rect(screen_width / 120 * 60, screen_height * 66/100, screen_width / 120 * 5, screen_height * 34/100)
ball = pygame.Rect(screen_width / 120 * 30.4,screen_height / 80 * 64,15 ,15)
line = pygame.Rect(screen_width / 120 * 28,screen_height / 80 * 65,50, 3)

font = pygame.font.SysFont("comicsans", 30, True)

ball_speed_x = 0
ball_speed_y = 0
ball_angle_increment = 0
ball_angle = 0
ball_velocity_increment = 0
ball_velocity = 1
gravity = 9.8
lives = 3

def main1(screen1, color_select, clockSelec):
    while True:
        #return
        
        global ball_speed_x
        global ball_speed_y
        global ball_angle_increment
        global ball_angle
        global ball_velocity_increment
        global ball_velocity
        global gravity
        global lives
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    # Key Actions
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    ball_angle_increment += 0.2
                if event.key == pygame.K_UP:
                    ball_angle_increment -= 0.2
                if event.key == pygame.K_LEFT:
                    ball_velocity_increment -= 0.1
                if event.key == pygame.K_RIGHT:
                    ball_velocity_increment += 0.1
                if event.key == pygame.K_RETURN:
                    if ball_speed_x == 0 or ball_speed_y == 0:
                        ball_speed_x = ball_velocity * math.cos(ball_angle * math.pi/180)
                        ball_speed_y = ball_velocity * math.sin(ball_angle * math.pi/180)
                    else:
                        j = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    ball_angle_increment = 0
                if event.key == pygame.K_UP:
                    ball_angle_increment = 0
                if event.key == pygame.K_LEFT:
                    ball_velocity_increment = 0
                if event.key == pygame.K_RIGHT:
                    ball_velocity_increment = 0
            

        
        ba.ball_animation()
        ba.update1()
        #ball_velocity += ball_velocity_increment
        #ball_angle += ball_angle_increment
        ball_speed_y += gravity/60  
        #line_animation()

        #Visuals
        screen1.fill(color_select)
        screen1.blit(background, (0,0))
        screen1.blit(target, (screen_width * i/48, screen_height * 36/40))
        target_rect = pygame.Rect(screen_width * i/48, screen_height * 69/72, target.get_width(), 2)
        pygame.draw.ellipse(screen1, (0,200,200), ball)
        pygame.draw.rect(screen1, (0,0,0), line)
        text = font.render("Angle " + str(-1 * ball_angle), 30, (200,0,0))
        text1 = font.render("Velocity " + str(ball_velocity), 30, (200,0,0))
        textlives = font.render("Lives Left: " + str(lives), 30, (200,0,0))
        screen1.blit(textlives, (screen_width * 6/8, screen_height * 1/12))
        screen1.blit(text1, (screen_width/6, screen_height/8))
        screen1.blit(text, (screen_width/6, screen_height/12))
        #Launcher Animation
        launcher_copy = pygame.transform.rotate(launcher, -1 * ball_angle)
        screen1.blit(launcher_copy, (screen_width / 120 * 27 - int(launcher_copy.get_width() / 4), screen_height / 120 * 95 - int(launcher_copy.get_height() /2)))
        
        pygame.display.flip()
        clockSelec.tick(60)
        