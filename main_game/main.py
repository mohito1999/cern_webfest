'''module/class import'''
import os
import pygame
from game_settings import Screen
from animsprite import AnimatedSprite
from buttons import Buttons
import math
from sec_round import main1
import random
import sys

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode()
bg_color = (255, 255, 255)

home_image = pygame.image.load("Foundation (d2) - Copy/57.jpg")
screen = pygame.display.set_mode((screen_width, screen_height))
FPS = 57
i = 35
j = 1
ball_initial_pos = (0, 200, 200)
'''
backgrounds = ["Challenge Room1.jpg", "JupiterChallengeRoom.png", "MarsChallengeRoom.jpg"]
background_games = ['Challenge Room1(game scene).jpg', "JupiterChallengeRoom(Game Scene).png", "MarsChallengeRoom(Game Scene).jpg"]
gs = [9.8, 24.79, 3.711]
k = 0  # index for above lists

backgrounds_dooropen = ["Challenge Room1(Door1Open).jpg", "JupiterChallengeRoom(Door1Open).png", "MarsChallengeRoom(Door1Open).jpg"]
l = 0  # index for background_dooropen list (different from k)
'''

play = pygame.image.load("Buttons/Play-Button.png").convert_alpha()
play_button = pygame.Rect(325, 500, 150, 50)

clock = pygame.time.Clock()


def completed():
    global background, player_x, walkcount
    global background_game, gravity
    #background = pygame.image.load('Challenge Room1(Door1Open).jpg')
    if walkcount + 1 >= 27:
        walkcount = 0
    screen.blit(background, (0,0))
    screen.blit(launcher, (screen_width / 120 * 27 - int(launcher.get_width() / 4), screen_height / 120 * 95 - int(launcher.get_height() /2)))
    screen.blit(background, (0,0))
    screen.blit(launcher, (screen_width / 120 * 27 - int(launcher.get_width() / 4), screen_height / 120 * 95 - int(launcher.get_height() /2)))
    screen.blit(target, (screen_width * i/48, screen_height * 36/40))
    screen.blit(text_launcher, (screen_width *2 / 6, screen_height/8))
    screen.blit(astronaut, (screen_width * 4/6, screen_height / 60 *39))
    screen.blit(player_walking [walkcount//7], (player_x, player_y))
    screen.blit(door_frame, (screen_width * 46 / 100, screen_height * 66 / 100))
    player_x += 1.5
    walkcount += 1
    background = pygame.image.load('JupiterChallengeRoom.png')
    background_game = pygame.image.load('JupiterChallengeRoom(Game Scene).png')
    gravity = 24.79
    


    pygame.display.update()
    


def ball_animation():
    global ball_speed_x, ball_speed_y, ball_angle, lives, i, player_x, background, background_game
    screen.fill(bg_color)
    screen.blit(background_game, (0,0))
    screen.blit(target, (screen_width * i/48, screen_height * 36/40))
    screen.blit(astronaut, (screen_width * 4/6, screen_height / 60 *39))
    target_rect = pygame.Rect(screen_width * i/48, screen_height * 69/72, target.get_width(), 2)
    pygame.draw.ellipse(screen, (0,200,200), ball)
    pygame.draw.rect(screen, (0,0,0), line)
    launcher_copy = pygame.transform.rotate(launcher, -1 * ball_angle)
    screen.blit(launcher_copy, (screen_width / 120 * 27 - int(launcher_copy.get_width() / 4), screen_height / 120 * 95 - int(launcher_copy.get_height() /2)))

    text = font.render("Angle " + "{:.0f}".format(-1 * ball_angle), 30, (200,0,0))
    text1 = font.render("Velocity " + "{:.1f}".format(ball_velocity), 30, (200,0,0))
    textlives = font.render("Lives Left: " + str(lives), 30, (200,0,0))
    screen.blit(textlives, (screen_width * 6/8, screen_height * 1/12))
    screen.blit(text1, (screen_width/6, screen_height/8))
    screen.blit(text, (screen_width/6, screen_height/12))
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
        ball.bottom = screen_height / 80 * 64
        ball.left = screen_width / 120 * 30.4
        while player_x < 700:    
            background = pygame.image.load('Challenge Room1(Door1Open).jpg')
            completed()
    if ball.colliderect(wall):
        ball_speed_x = 0
        ball_speed_y = 0
        ball.bottom = screen_height / 80 * 64
        ball.left = screen_width / 120 * 30.4
        lives -= 1


    if ball.right >= screen_width + 20:
        ball_speed_x = 0
        ball_speed_y = 0
        ball.bottom = screen_height / 80 * 64
        ball.left = screen_width / 120 * 30.4
        lives -= 1

def update():
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

def fill():
    global player_x
    screen.blit(background, (0,0))
    screen.blit(launcher, (screen_width / 120 * 27 - int(launcher.get_width() / 4), screen_height / 120 * 95 - int(launcher.get_height() /2)))
    screen.blit(target, (screen_width * i/48, screen_height * 36/40))
    screen.blit(text_launcher, (screen_width *2 / 6, screen_height/8))
    screen.blit(astronaut, (screen_width * 4/6, screen_height / 60 *39))
    screen.blit(player_standing, (player_x, player_y))

def player_animation():
    global walkcount, player_x, i, font, text_launcher, walking, sound1, sound2, j, speech
    screen.blit(background, (0,0))
    screen.blit(launcher, (screen_width / 120 * 27 - int(launcher.get_width() / 4), screen_height / 120 * 95 - int(launcher.get_height() /2)))
    screen.blit(target, (screen_width * i/48, screen_height * 36/40))
    screen.blit(text_launcher, (screen_width *2 / 6, screen_height/8))
    screen.blit(astronaut, (screen_width * 4/6, screen_height / 60 *39))
    if walkcount + 1 >= 27:
        walkcount = 0
    if player_x < 0:
        player_x = 0
    if walking:
        screen.blit(player_walking [walkcount//7], (player_x, player_y))
        walkcount += 1
    if walking == False:
        screen.blit(player_standing, (player_x, player_y))
    if player_x > screen_width / 100 * 41:
        player_x = screen_width / 100 * 41
        if j == 1:
            speech = speech_1
            screen.blit(speech, (screen_width * 3/8, screen_height * 3/8))
            pygame.display.flip()
            sound1.play()
            pygame.time.delay(12000)
            sound2.play()
            pygame.time.delay(14000)
            fill()
            screen.blit(speech_2, (screen_width * 3/8, screen_height * 3/8))
            pygame.display.flip()
            sound3.play()
            pygame.time.delay(3000)
            fill()
            screen.blit(speech_3, (screen_width * 3/8, screen_height * 3/8))
            pygame.display.flip()
            pygame.time.delay(3000)
            fill()
            screen.blit(speech_4, (screen_width * 3/8, screen_height * 3/8))
            pygame.display.flip()
            fill()
            pygame.time.delay(3000)
            screen.blit(speech_5, (screen_width * 3/8, screen_height * 3/8))
            pygame.display.flip()
            pygame.time.delay(3800)
            fill()
            screen.blit(speech_6, (screen_width * 3/8, screen_height * 3/8))
            pygame.display.flip()
            pygame.time.delay(3000)
            fill()
            text_launcher = font.render("Press Enter At Launcher", 40, (200,0,0))
            j = 0
    if j == 0: 
        if player_x < screen_width / 100 * 25 and player_x > screen_width / 100:
                border = pygame.Rect(screen_width / 100 * 15, screen_height / 100 * 66, 215, 26)
                pygame.draw.rect(screen, (0,0,0), border)
                text_enter = font.render("[Press Enter Here]",  30, (255,255,255))
                screen.blit(text_enter, (screen_width / 100 * 15, screen_height / 100 * 66))
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                                intro = False
                                playing = True
        
    pygame.display.update()


target = pygame.image.load('Target(1).png')
target_rect = pygame.Rect(screen_width * i/48, screen_height * 70/72, target.get_width() - 2, 1)

wall = pygame.Rect(screen_width / 120 * 60, screen_height * 66/100, screen_width / 120 * 5, screen_height * 34/100)
ball = pygame.Rect(screen_width / 120 * 30.4,screen_height / 80 * 64,15 ,15)
line = pygame.Rect(screen_width / 120 * 28,screen_height / 80 * 65,50, 3)

launcher = pygame.image.load('Projectile-Launcher.png').convert_alpha()

background = pygame.image.load('ChallengeRoom1.jpg')
background_game = pygame.image.load('Challenge Room1(game scene).jpg')
door_frame = pygame.image.load('DoorFrame.png')
astronaut = pygame.image.load('astronaut instructor.png')

player = pygame.image

font = pygame.font.SysFont("comicsans", 30, True)
text_launcher = font.render("", 40, (200,0,0))


ball_speed_x = 0
ball_speed_y = 0
ball_angle_increment = 0
ball_angle = 0
ball_velocity_increment = 0
ball_velocity = 7
gravity = 9.8
lives = 3

speech_1 = pygame.image.load("intro_text/IntroText(1).png")
speech_2 = pygame.image.load("intro_text/IntroText(1).png")
speech_3 = pygame.image.load("intro_text/IntroText(3).png")
speech_4 = pygame.image.load("intro_text/IntroText(4).png")
speech_5 = pygame.image.load("intro_text/IntroText(5).png")
speech_6 = pygame.image.load("intro_text/IntroText(6).png")

sound1 = pygame.mixer.Sound('voice_overs_wav/Part-1.wav')
sound2 = pygame.mixer.Sound('voice_overs_wav/Part-2.wav')
sound3 = pygame.mixer.Sound('voice_overs_wav/Part-3.wav')
sound4 = pygame.mixer.Sound('voice_overs_wav/Part-4_1.wav')
sound5 = pygame.mixer.Sound('voice_overs_wav/Part-5_1.wav')




player_walking = [pygame.image.load('charv2(1).png'), pygame.image.load('charv2(2).png'), pygame.image.load('charv2(3).png'), pygame.image.load('charv2(4).png')]
player_standing = pygame.image.load('charv2(5).png')
player_width = 110
player_height = 160
player_vel = 5
walkcount = 0
player_x = 0
player_y = screen_height / 60 *43
walking = False

intro = True
playing = False
'''
ball = pygame.Rect(304,640,20 ,20)
line = pygame.Rect(280,650,50, 3)
gravity = 9.8
'''
'''
#Graphics
launcher = pygame.image.load('/Users/mohitmotwani/Documents/GitHub/cern_webfest/assets/Projectile Launcher.png')
#launcher.set_colorkey((0,0,0))
background = pygame.image.load('/Users/mohitmotwani/Documents/GitHub/cern_webfest/assets/Challenge Room1.jpg')
#launcher.set_alpha(100)

bg_color = pygame.Color('grey12')
light_grey = (200,200,200)

font = pygame.font.SysFont("comicsans", 30, True)
'''


def load_images(path):
    images = []
    imagelist = sorted(os.listdir(path))
    imagelist = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg',  '6.jpg', '7.jpg', '8.jpg', '9.jpg', '10.jpg', '11.jpg', '12.jpg', '13.jpg', '14.jpg', '15.jpg', '16.jpg', '17.jpg', '18.jpg', '19.jpg', 
     '20.jpg', '21.jpg', '22.jpg', '23.jpg', '24.jpg', '25.jpg', '26.jpg', '27.jpg', '28.jpg', '29.jpg',  
    '30.jpg', '31.jpg', '32.jpg', '33.jpg', '34.jpg', '35.jpg', '36.jpg', '37.jpg', '38.jpg', '39.jpg', '40.jpg', 
    '41.jpg', '42.jpg', '43.jpg', '44.jpg', '45.jpg', '46.jpg', '47.jpg', '48.jpg', '49.jpg', '50.jpg', '51.jpg', 
    '52.jpg', '53.jpg', '54.jpg', '55.jpg', '56.jpg', '57.jpg']
    for file_name in imagelist:
        image = pygame.image.load(path + os.sep + file_name).convert()
        images.append(image)
    return images


def main():
    images = load_images(path="Foundation (d2) - copy")  # Make sure to provide the relative or full path to the images directory.
    player = AnimatedSprite(position=(0, 0), images=images)
    all_sprites = pygame.sprite.Group(player)  # Creates a sprite group and adds 'player' to it.

    running = True
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                pygame.quit()
        
        while running:

            dt = 1   # Amount of seconds between each loop.

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    

            all_sprites.update(dt)  # Calls the 'update' method on all sprites in the list (currently just the player).

            
            
            screen.fill(bg_color)
            all_sprites.draw(screen)
            pygame.display.update()
            clock.tick(100)
            if player.index == 56:
                running = False
                break
        
        screen.blit(home_image, (0, 0))
        screen.blit(play, [115, 300])
        pygame.display.update()
        
        playing1 = True
        while playing1:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    ## if mouse is pressed get position of cursor ##
                    pos = pygame.mouse.get_pos()
                    ## check if cursor is on button ##
                    if play_button.collidepoint(pos):
                        playing1=False            
                        break                   

                        #Group all of Ryan's code as a function and call it when mouse is pressed
        #main1(screen, screen_settings.bg_color, clock)
        while True:
            global ball_speed_x
            global ball_speed_y
            global ball_angle_increment
            global ball_angle
            global ball_velocity_increment
            global ball_velocity
            global gravity
            global lives
            global intro 
            global walking
            global player_x
            global playing
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


            while intro:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        player_x -= 1.5
                        walking = True
                    if event.key == pygame.K_RIGHT:
                        player_x += 1.5
                        walking = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        walking = False
                    if event.key == pygame.K_RIGHT:
                        walking = False
                    if event.key == pygame.K_RETURN:
                        if player_x < screen_width / 100 * 25 and player_x > screen_width / 100 * 18:
                            intro = False
                            playing = True
                            break

           
                #print(walking)
                player_animation()
                clock.tick(60)
        
        
        
        # Key Actions
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    ball_angle_increment += 0.02
                if event.key == pygame.K_UP:
                    ball_angle_increment -= 0.02
                if event.key == pygame.K_LEFT:
                    ball_velocity_increment -= 0.01
                if event.key == pygame.K_RIGHT:
                    ball_velocity_increment += 0.01
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
            

            
            ball_animation()
            update()
            #ball_velocity += ball_velocity_increment
            #ball_angle += ball_angle_increment
            ball_speed_y += gravity/60


            launcher_copy = pygame.transform.rotate(launcher, -1 * ball_angle)
            screen.blit(launcher_copy, (screen_width / 120 * 27 - int(launcher_copy.get_width() / 4), screen_height / 120 * 95 - int(launcher_copy.get_height() /2)))  
            


            '''
            ball_animation()
            update()
            #ball_velocity += ball_velocity_increment
            #ball_angle += ball_angle_increment
            ball_speed_y += gravity/60  
            '''
            '''
            #Visuals
            screen.fill(bg_color)
            screen.blit(background, (0,0))
            screen.blit(target, (screen_width * i/48, screen_height * 36/40))
            target_rect = pygame.Rect(screen_width * i/48, screen_height * 69/72, target.get_width(), 2)
            pygame.draw.ellipse(screen, (0,200,200), ball)
            pygame.draw.rect(screen, (0,0,0), line)
            text = font.render("Angle " + str(-1 * ball_angle), 30, (200,0,0))
            text1 = font.render("Velocity " + str(ball_velocity), 30, (200,0,0))
            textlives = font.render("Lives Left: " + str(lives), 30, (200,0,0))
            screen.blit(textlives, (screen_width * 6/8, screen_height * 1/12))
            screen.blit(text1, (screen_width/6, screen_height/8))
            screen.blit(text, (screen_width/6, screen_height/12))
            #Launcher Animation
            launcher_copy = pygame.transform.rotate(launcher, -1 * ball_angle)
            screen.blit(launcher_copy, (screen_width / 120 * 27 - int(launcher_copy.get_width() / 4), screen_height / 120 * 95 - int(launcher_copy.get_height() /2)))
            '''

            pygame.display.flip()
            clock.tick(30)
            
        
        

   
main()




