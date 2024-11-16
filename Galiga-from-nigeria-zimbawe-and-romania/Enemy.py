import pygame
import time


class freind:
    def __init__(self,x,y):
        self.image = pygame.image.load("Dad_cameback.png")


class lasar:
    def __init__(self,x,y):
        self.image = pygame.image.load("Galiga-from-nigeria-zimbawe-and-romania/pictures/Chimeny_Gamer.png")
        self.image = pygame.transform.scale(self.image, (10,10))
        self.image = pygame.transform.rotate(self.image, -90)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, Space, enemy_lasers, ship):
        Space.blit(self.image, self.rect)
        self.rect.y +=1
        for laser in enemy_lasers:
            if laser.rect.y < 0:
                enemy_lasers.remove(laser)
           
class Enemy(pygame.sprite.Sprite):
    # costructor - a fucntion that you use to create the off your object
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.Snake = pygame.image.load("Galiga-from-nigeria-zimbawe-and-romania/pictures/Death.jpg")
        self.image = pygame.transform.scale(self.Snake, (75,75))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.start = time.time()
        
    def movement(self, ship_x, list):
        current = time.time()
        if self.rect.x > ship_x:
            self.rect.x -= 1
        elif self.rect.x < ship_x:
            self.rect.x += 1

            
        if self.rect.x == ship_x and current - self.start >= 0.5:
            self.start = time.time()
            self.shoot(list)
            
    def shoot(self, list):
        list.append(lasar(self.rect.x+39, self.rect.y))
        
    
    def update(self, Space, ship_x, list, ship):
        Space.blit(self.image, self.rect)
        self.movement(ship_x, list)
        for enemy in list:
            enemy.update(Space, list, ship)
          