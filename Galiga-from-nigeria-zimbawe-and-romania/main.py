import pygame, sys
from pygame.locals import QUIT
import pygame.time
from Enemy import Enemy
from laser import Hindi
import time
from Enemys import enemy
from score import Score
score_counter = 0
highscore = Score()
#current_highscore = int(highscore.read_file)


pygame.init()
Space = pygame.display.set_mode((400, 600))
pygame.display.set_caption('Space Game')


# list that stores all the enemy lasers
enemy_lasers = []
# list that stores all of the enemies
enemies = []
enemies.append(Enemy(100, 100))
# this creates the screen for drawing the text on
text_screen = pygame.Surface((100,20))
text_screen_rect = text_screen.get_rect()
text_screen_rect.x = 0
text_screen_rect.y = 0
# this creates the font for the text and it's size
font = pygame.font.SysFont("Arial", 11)
# this is to create the text with the font that you created, as well as determine its color.
text = font.render("Points: " + str(score_counter), True, "white")

Biden = []  # this stores all the lasers that I shoot out of the ship.
Ship_lives = 5000000000000000000000000


# an object is a thing you make from a class


# Creates enemies in specific formation
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

score = ()

Noodles = pygame.image.load("Galiga-from-nigeria-zimbawe-and-romania\pictures\Donald_trump_ship.png") # image for ship loaded up
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
  highscore.high_score(score_counter, highscore.read_file())

  current_time = time.time() # current time constantly updates
  Space.fill("Black")
  pygame.time.delay(10)
  text = font.render("Points: " + str(score_counter), True, "white")
  Space.blit(text_screen, text_screen_rect)
  text_screen.fill("black")
  text_screen.blit(text, (10,10))


  enemies[0].update(Space, Noodles_rect.x, enemy_lasers, Noodles_rect)
  for lasers in enemy_lasers:
      if lasers.rect.colliderect(Noodles_rect):
          enemy_lasers.remove(lasers)
          Ship_lives -= 1
          print(Ship_lives)
      if Ship_lives == 0:
          quit(0)
          
          
  Space.blit(Noodles, Noodles_rect)
  # check to see whether lasers hit enemy
  for enemy in multiple_enemy:
      enemy.update(Space, multiple_enemy, enemy_lasers)
      for laser in Biden:
          if enemy.rect.colliderect(laser.rect):
                multiple_enemy.remove(enemy)
                score_counter += 10
                Biden.remove(laser)
        

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

      
  if key[pygame.K_SPACE] and current_time - start_time >= 0.2:
      
      Biden.append(Hindi(Noodles_rect.x, Noodles_rect.y))
      start_time = time.time()


  for Donald in Biden:
      Donald.update(Space)
      if Donald.rect.y < 0 or Donald.rect.colliderect(enemies[0].rect): 
          Biden.remove(Donald)
          score_counter += 50
          
    
      
      
  for event in pygame.event.get():
       if event.type == QUIT:
           pygame.quit()
           sys.exit()
  pygame.display.update()
