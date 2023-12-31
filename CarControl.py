import pygame
from pygame.locals import *
import random

size = width, height = (800, 800)
road_w = int(width/1.6)
roadmark_w = int(width/80)
EnemyRight_lane = width/2 + road_w/4
EnemyLeft_lane = width/2 - road_w/4
BlueCar_flag = 0

pygame.init()
running=True
#Set windows size
screen = pygame.display.set_mode(size)
#Set title
pygame.display.set_caption("Car Control Game (By Yousef Rahimy Akhondzadeh)")
#Set background color
screen.fill((60, 220, 0))

#Apply changes
pygame.display.update()

#Load MyCar(BlueCar)
BlueCar = pygame.image.load("BlueCar.png")
BlueCar_loc = BlueCar.get_rect()
BlueCar_loc.center = EnemyRight_lane, height*0.825

#Load EnemyCar(RedCar)
RedCar = pygame.image.load("RedCar.png")
RedCar_loc = RedCar.get_rect()
RedCar_loc.center = EnemyLeft_lane, height*0.2

counter = 0
speed = 1
#Game loop
while running:
    counter +=1
    if counter == 50000:
        speed += 0.15
        counter = 0
        print("Level up ", speed)

    RedCar_loc[1] += speed
    if RedCar_loc[1] > height:
        RedCar_loc[1] = -200
        if random.randint(0, 1) == 0:
            RedCar_loc.center = EnemyRight_lane, -200
        else:
            RedCar_loc.center = EnemyLeft_lane, -200

    #End game
    if BlueCar_loc[0] == RedCar_loc[0] and RedCar_loc[1] > BlueCar_loc[1] - 250:
        print("GAME OVER")
        break

    #Event listener
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key in [K_a, K_LEFT] and BlueCar_flag == 0:
                BlueCar_loc = BlueCar_loc.move([-int(road_w/2), 0, ])
                BlueCar_flag = 1
            if event.key in [K_d, K_RIGHT] and BlueCar_flag == 1:
                BlueCar_loc = BlueCar_loc.move([int(road_w/2), 0, ])
                BlueCar_flag = 0

    #Draw graphics
    #Draw road
    pygame.draw.rect(screen,(50, 50, 50),(width/2 - road_w/2, 0, road_w, height))
    #Draw road center line
    pygame.draw.rect(screen,(255, 240, 60),(width/2 - roadmark_w/2, 0, roadmark_w, height))
    #Draw road side lines
    pygame.draw.rect(screen,(255, 255, 255),(width/2 - road_w/2 + roadmark_w*2 , 0, roadmark_w, height))
    pygame.draw.rect(screen,(255, 255, 255),(width/2 + road_w/2 - roadmark_w*3 , 0, roadmark_w, height))
    
    screen.blit(BlueCar, BlueCar_loc)
    screen.blit(RedCar, RedCar_loc)
    pygame.display.update()

pygame.quit()