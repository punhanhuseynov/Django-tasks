import pygame
import random
from pygame.sprite import  Group
x=0
y=0
coinX=random.randint(10,500)
coinY=random.randint(10,500)
playerspeed=0.50

pygame.init()
screen=pygame.display.set_mode((500,500))

pygame.display.set_caption('game')

running = True

class Player(pygame.sprite.Sprite):
     def __init__(self):
          super().__init__()
          self.image= pygame.image.load('player.png').convert_alpha()
          self.image=pygame.transform.scale(self.image,(100,100))
          self.rect=self.image.get_rect()
          self.rect.center=[x,y]
          
class Coin(pygame.sprite.Sprite):
     def __init__(self):
          super().__init__()
          self.image=pygame.Surface((20,20))
          self.image.fill((255,0,0))

          self.rect=self.image.get_rect()
          self.rect.center= (coinX,coinY)

     

all_sprites=pygame.sprite.Group()
player=Player()
coin=Coin()
all_sprites.add(player)
all_sprites.add(coin)



while running:

        for event in pygame.event.get():
           if event.type == pygame.QUIT:
               running = False
          
           if event.type==pygame.MOUSEBUTTONDOWN:
                 print(f'cOIN - {coinX},{coinY}')
                 print(f'Player - {x},{y}')


          
        keys=pygame.key.get_pressed()

        if keys[pygame.K_w]:
            
             if y<-50:
                  y=550
             y-=playerspeed
        
        elif keys[pygame.K_s]:
          
             if y>550:
                  y=-50
             y+=playerspeed
        
        elif keys[pygame.K_a]:
             if x <-50:
                  x=550
             x-=playerspeed
        
        elif keys[pygame.K_d]:
             if x>550:
                  x=-50
             x+=playerspeed
     

        if coinX-50<x<coinX+50 and coinY-50<y<coinY+50 :
          
             coinX=random.randint(10,500)
             coinY=random.randint(10,500)
             coin.rect.center=[coinX,coinY]
        player.rect.center=[x,y]
        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
        pygame.display.update()

pygame.quit()
