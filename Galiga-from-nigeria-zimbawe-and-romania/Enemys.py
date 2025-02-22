import pygame
import time
import random
from Enemy import lasar 
# class creates multiple enemies within the game in a square formation
# This class is complete
class enemy:
    def __init__(self, x, y,):
        self.direction_x =  False
        self.img = pygame.image.load("Galiga-from-nigeria-zimbawe-and-romania\pictures\Death.jpg")
        self.img = pygame.transform.scale(self.img,(35,35))
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.damage = 1
        self.random_laser_time = random.randint(1,10)
        self.life = 1
        self.start_time = time.time()

    def enemy_movement(self, list):
        # if you hit the left side, then move to the right and move down 10
        if self.rect.x <= 0:
            for dir in list:
                dir.direction_x = True
            for dir in list:
                dir.rect.x += 20
                dir.rect.y += 10

        # if you hit the right side, then move to the left and move down 10
        if self.rect.x >= 400:
            for dir in list:
                dir.direction_x = False
            for dir in list:
                dir.rect.x -= 20
                dir.rect.y += 10

        if self.direction_x == True:
            self.rect.x += 1
        
        if self.direction_x == False:
            self.rect.x -= 1



            
    def update(self, screen, list, lasers):
        current_time = time.time()
        screen.blit(self.img, self.rect)
        self.enemy_movement(list)
        if current_time - self.start_time >= self.random_laser_time:
            lasers.append(lasar(self.rect.x, self.rect.y))
            self.random_laser_time = random.randint(1,250)
            self.start_time = time.time()
            


