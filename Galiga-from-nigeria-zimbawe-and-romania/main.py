import pygame, sys
from pygame.locals import QUIT
import pygame.time
from Enemy import Enemy
from laser import Hindi
import time
from Enemys import enemy


pygame.init()
Space = pygame.display.set_mode((400, 600))
pygame.display.set_caption('Space Game')

enemy_lasers = []
enemies = []
enemies.append(Enemy(100, 100))
Biden = []  # this stores all the lasers that I shoot out of the ship.
Ship_lives = 50000000000000000000


# an object is a thing you make from a class

x = 50 
y = 10
multiple_enemy = []
def create_row():
    global x
    for _ in range(5):
        multiple_enemy.append(enemy(x,y))
        x += 55

for _ in range(4):
    create_row()
    x = 50
    y += 30



# multiple_enemy[0] = enemy(0,0)



Noodles = pygame.image.load("Galiga-from-nigeria-zimbawe-and-romania/pictures/Donald_trump_ship.png") # image for ship loaded up
Noodles = pygame.transform.scale(Noodles,(40,40)) #changing size of spacehsip
Noodles = pygame.transform.rotate(Noodles, 0)
Noodles_rect = Noodles.get_rect() # This creates a rectangle the same size as the ship
Noodles_rect.x = 190
Noodles_rect.y = 500

# time() -> it returns the amount of seconds that have passed since Jan 1st, 1970

# time.time() is often used as a timer to record how many seconds have passed since a designated start time.

# current time- keeps track of time passing 
# start time- time which we first started.

# We need to keep track of the amount of seconds that have passed since we pressed bar

# start time is a time stamp
# start time records the time that you first start the game
start_time = time.time()# start time is a time stamp



while True:
  current_time = time.time() # current time constantly updates
  pygame.time.delay(10)
  Space.fill("Black")
  enemies[0].update(Space, Noodles_rect.x, enemy_lasers, Noodles_rect)
  for lasers in enemy_lasers:
      if lasers.rect.colliderect(Noodles_rect):
          enemy_lasers.remove(lasers)
          Ship_lives -= 1
          print(Ship_lives)
      if Ship_lives == 0:
          quit(0)
          
          
  Space.blit(Noodles, Noodles_rect)
  for enemy in multiple_enemy:
      enemy.update(Space)

  key = pygame.key.get_pressed()
  if key[pygame.K_RIGHT]:
      Noodles_rect.x += 3
    
  if key[pygame.K_LEFT]:
    Noodles_rect.x += -3
  
  if key[pygame.K_UP]:
        Noodles_rect.x += 3

  if key[pygame.K_DOWN]:
        Noodles_rect.x += 3

  if key[pygame.K_d]:
        Noodles_rect.x += 15

  if key[pygame.K_a]:
        Noodles_rect.x += -15
      
  if key[pygame.K_SPACE] and current_time - start_time >= 0.5:
      
      Biden.append(Hindi(Noodles_rect.x, Noodles_rect.y))
      start_time = time.time()


  for Donald in Biden:
      Donald.update(Space)
      if Donald.rect.y < 0 or Donald.rect.colliderect(enemies[0].rect): 
          Biden.remove(Donald)
          
          
    
      
      
  for event in pygame.event.get():
       if event.type == QUIT:
           pygame.quit()
           sys.exit()
  pygame.display.update()