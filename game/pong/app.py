from typing import Any
import pygame
from pygame.sprite import  Group
import math 
angle=math.radians(45)
pygame.init()
WIDTH=700
HEIGHT=500
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Pong')

running=True
speed=1
x_pos=50
y_pos=100
color=(255,255,255)
ballmoveH='right'
ballmoveV='down'
direction=False
direction2=False

ball_speedx=speed*math.cos(angle)
ball_speedy=speed*math.sin(angle)

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.Surface((50,50),pygame.SRCALPHA)
      
        pygame.draw.circle(self.image,color,(10,10),10)
        self.rect=self.image.get_rect()
        self.rect.center=[x_pos,y_pos]

class Playerone(pygame.sprite.Sprite):
    x=30
    y=0
    def __init__(self):
        super().__init__()
        self.image=pygame.Surface((20,100))
        self.image.fill(color)
        self.rect=self.image.get_rect()
        self.rect.center=[self.x,self.y]
    def update(self):
        self.rect.center=[self.x,self.y]

class Playertwo(pygame.sprite.Sprite):
    x=WIDTH-30
    y=100
    def __init__(self):
        super().__init__()
        self.image=pygame.Surface((20,100))
        self.image.fill(color)
        self.rect=self.image.get_rect()
        self.rect.center=[self.x,self.y]
    def update(self):
        self.rect.center=[self.x,self.y]


all_sprites=pygame.sprite.Group()
ball=Ball()
player1=Playerone()
player2=Playertwo()
all_sprites.add(ball,player1,player2)

while running:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
         
    # Player movement
    keys=pygame.key.get_pressed()
    
    if keys[pygame.K_w]:
        player1.y-=speed
    
    elif keys[pygame.K_s]:
        player1.y+=speed
    
    if keys[pygame.K_UP]:
        player2.y-=speed
   
    elif keys[pygame.K_DOWN]:
        player2.y+=speed



    if ball.rect.colliderect(player1) and direction==False:
        angle=math.atan2(ball.rect.centery - player1.rect.centery,ball.rect.centerx - player1.rect.centerx)

        if ballmoveH=='right':
            ballmoveH='left'
        elif ballmoveH=='left':
            ballmoveH='right'
       
        direction=True
        direction2=False
        print(ballmoveV)
    
    if ball.rect.colliderect(player2) and direction2==False:

        print(ballmoveH)
        if ballmoveH=='right':
            ballmoveH='left'
        elif ballmoveH=='left':
             ballmoveH='right'
        print(ballmoveV)
        direction2=True
        direction=False
        

    # Ball movement
    if ballmoveH=='right':
        if ball.rect.centerx>WIDTH:
            
            ballmoveH='left'
            direction=False
            direction2=False
        
            
        x_pos+=speed*math.cos(angle)
      
    elif ballmoveH=='left':
      
        if ball.rect.centerx<0:
            ballmoveH='right'
            direction=False
            direction2=False
     
        x_pos-=speed*math.cos(angle)

    if ballmoveV=='up':
        
        if ball.rect.centery<0:
          ballmoveV='down'
          direction=False
          direction2=False
        y_pos-=speed*math.sin(angle)

    elif ballmoveV=='down':
      
            
        if  ball.rect.centery>HEIGHT:
            ballmoveV='up'
            direction=False
            direction2=False
        y_pos+=speed*math.sin(angle)

    
    # Update screen
    all_sprites.update()
    ball.rect.center=[x_pos,y_pos]
    screen.fill((0,0,0))
   
    all_sprites.draw(screen)
    pygame.display.update()

pygame.quit()