#import pygame, and system library to use for rendering and quitting
import sys
import pygame

#init objects for pygame
screenDim = 300
pygame.init()
pygame.font.init()
FPS = pygame.time.Clock()

#creates area to render on screen screenDimxscreenDim pixels
DisplaySurf = pygame.display.set_mode((screenDim,screenDim))

#defines frames per second
FPS.tick(25)

#define player information
playerX = 0
playerY = 0
playerXVel = 0
playerYVel = 0
playerDim = 50
playerImg = pygame.image.load('player.png')
# Scale the image to your needed size
playerImg = pygame.transform.scale(playerImg, (playerDim, playerDim))


#define obstacles in game or collidable objects
obstacles = [[50, 150, 50, 75], [200, 100, 75, 50]]

#define background elements in game of non-collidable objects
backgroundElements = [[100, 50, 60, 75], [25, 140, 60, 25]]

startTime = pygame.time.get_ticks()
endTime = pygame.time.get_ticks()

#basic game loop
while True:

#calculate how many frames should have been rendered since last render to use as multiplier for velocity
#position = velocity * time + initialPosition
 deltaTime = endTime - startTime
 startTime = pygame.time.get_ticks()

#Game logic here:
#move player position by vel*change in time
 playerY += playerYVel * deltaTime
 playerX += playerXVel * deltaTime

#check for collisions
 collision = False

#check for collisions with every obstacle
 for obstacle in obstacles:

#get this obstacle's data
     obstacleX = obstacle[0]
     obstacleY = obstacle[1]
     obstacleWidth = obstacle[2]
     obstacleHeight = obstacle[3]

#detect collision with one obstacle that is rectangular
     if(playerX < obstacleX + obstacleWidth and playerX + playerDim > obstacleX):
      if (playerY < obstacleY + obstacleHeight and playerY + playerDim > obstacleY):
       collision = True


#detect collisions with walls to keep player on screen
 if(playerX < 0 or playerX + playerDim > screenDim or playerY < 0 or playerY + playerDim > screenDim):
  collision = True

#undo movement if collision detected
 if(collision):
  playerY -= playerYVel * deltaTime
  playerX -= playerXVel * deltaTime

#start of rerender here:
#Fill background with white each frame
#the last parameter is a tuple of 4 numbers(like a list) representing the 
# x, y, width, and height of the rectangle to be drawn in pixels
#pygame.Color allows us to create a color object that can store red, green, and blue values between 0 and 255
 pygame.draw.rect(DisplaySurf, pygame.Color(255, 255, 255), (0, 0 , screenDim, screenDim))

#render background here:
 for backgroundElement in backgroundElements:
     backgroundElementX = backgroundElement[0]
     backgroundElementY = backgroundElement[1]
     backgroundElementWidth = backgroundElement[2]
     backgroundElementHeight = backgroundElement[3]
     pygame.draw.rect(DisplaySurf, pygame.Color(0,255,0), (backgroundElementX, backgroundElementY, backgroundElementWidth, backgroundElementHeight))

#render player, and obstacles here:
 for obstacle in obstacles:
     obstacleX = obstacle[0]
     obstacleY = obstacle[1]
     obstacleWidth = obstacle[2]
     obstacleHeight = obstacle[3]
     pygame.draw.rect(DisplaySurf, pygame.Color(255,0,0), (obstacleX, obstacleY, obstacleWidth, obstacleHeight))

#render player:
 DisplaySurf.blit(playerImg, (playerX, playerY))

#Push updates in what has been rendered to the screen
 pygame.display.update()

#Defining event handlers
 for event in pygame.event.get():
#Handle quitting the game
  if (event.type == pygame.QUIT):
   pygame.quit()
   sys.exit()
  else:
   if (event.type == pygame.KEYDOWN):
#key pressed handlers
    if(event.key == pygame.K_DOWN):
     playerYVel += 0.5
    elif(event.key == pygame.K_UP):
     playerYVel -= 0.5
    if(event.key == pygame.K_RIGHT):
     playerXVel += 0.5
    elif(event.key == pygame.K_LEFT):
     playerXVel -= 0.5
#key released handlers
   elif event.type == pygame.KEYUP:
    if(event.key == pygame.K_DOWN or event.key == pygame.K_UP):
     playerYVel = 0
    if(event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT):
     playerXVel = 0
    
 endTime = pygame.time.get_ticks()