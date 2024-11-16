import pygame




class enemy:
    def __init__(self, x, y):
        self.img = pygame.image.load("Galiga-from-nigeria-zimbawe-and-romania/pictures/Enemy's.png")
        self.img = pygame.transform.scale(self.img,(35,35))
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.damage = 0.5
        self.life = 1
    def update(self, screen):
        screen.blit(self.img, self.rect)