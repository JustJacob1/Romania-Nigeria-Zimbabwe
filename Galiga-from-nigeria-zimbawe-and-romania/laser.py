import pygame
class Hindi:
  def __init__(self,x,y,): # constructor- creating the basics details of your object
      self.img = pygame.image.load("Galiga-from-nigeria-zimbawe-and-romania/pictures/Block.png")
      self.img = pygame.transform.scale(self.img, (10,15))
      self.rect = self.img.get_rect()
      self.rect.x = x + 13
      self.rect.y = y
  def update(self, Space):
      Space.blit(self.img, self.rect)
      self.rect.y -= 2