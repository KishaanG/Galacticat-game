
'''
This is the start of our game
'''


# ----------------------------------------------------------------------
# Import classes from different files. 

from Sprite_Kishaan import Sprite, NORM, DEAD, REVIVE, FLIP
from Level import Level
from Player import Player
from Enemies import Enemies
from PowerUps import PowerUp

# ----------------------------------------------------------------------

def setup():
    size(640, 600) # Sets the size of the game screen. size(width, height).
    this.surface.setTitle("Galacticat by Kishaan")
    frameRate(60)
    # Declares a global variable that can be used anywhere.
    global background_image
    global player_image
    global player
    global level
    global enemy_image
    global enemy_list
    global powerUpImage
    global milk
    
    
    initImages()
    initObjects()
    
    
#---------------------------------------------- draw method - runs continuously
    
def draw(): # This method will always run. It will keep updating.
    background(0) # Sets the colour of the background. background(RGB) or background(R, G, B) 0-255.
    
    if player.lives > 0 and level.defeatedEnemies < level.totalEnemies:
        updateLevel()
        updatePlayer()
        
        updateEnemies()
        updateMilk()
        checkHittingEnemy()
        updateUI()
        
    else:
        showEndMenu()
    
def updateLevel():
    level.display() # Draw the background to the screen. image(image, starting x-position, starting y-position).
    level.tickSpawnTimer() # Start the timer to draw enemies.
    
#---------------------------------------------- Input - Runs when a key is pressed.

def keyPressed():
    if player.state == NORM or player.state == REVIVE:
        player.state = NORM
        if keyCode ==  RIGHT: # If the right arrow is clicked then,
            player.rightSpeed = 5 # Sets the speed to 5.
            player.facingR = True
        elif keyCode == LEFT: # If the left arrow is clicked then,
            player.leftSpeed = -5 # Sets the speed to -5.
            player.facingR = False
        elif keyCode == UP and player.ySpeed == 0:
            player.ySpeed = -23 # Controls the height of your jump. 
    
    if key == ENTER or key == RETURN:
        if player.lives == 0:
            gameOverReset()
        if level.defeatedEnemies == level.totalEnemies:
            nextLevel()
            
            
            
#---------------------------------------------- Input - Runs only when a key is released.

def keyReleased():
    if player.state == NORM or player.state == REVIVE:
        if keyCode ==  RIGHT: # If the right arrow is clicked then,
            player.rightSpeed = 0 # Sets the speed to 5.
        elif keyCode == LEFT: # If the left arrow is clicked then,
            player.leftSpeed = 0 # Sets the speed to -5.
        
        
        
def initImages():
    
    global background_image
    global player_image
    global enemy_image
    global powerUpImage
    
    # It sets the variable to the value of the image we want.
    background_image = loadImage("Pics/bckgrnd.bmp")
    player_image = loadImage("Pics/Galacticat.png")
    enemy_image = loadImage("Pics/Fangs.png")
    powerUpImage = loadImage("Pics/milk.png")



def initObjects():
    
    global player
    global level
    global milk   
    
    #Initialize the player class.
    player = Player(250, 150, 15, player_image) # YOU MUST GIVE SPRITE 2 VALUES TO START (x, y)
    level = Level(background_image) # Sets the background image for the game inside of level. 
    milk = PowerUp(310, 300, 10, powerUpImage)
    init_enemies() # Initializes the enemies, loads the enemies. 


# --------------------------------------------- Initialize enemy
def init_enemies():
    global enemy_list # Can be used in any method.
    
    enemy_list = [Enemies(80, -50, 10, enemy_image, 3) for x in range (level.totalEnemies)] # Enemies(80, -50, 10, enemy_image, 3)
    # for x in range (2) --> What is this? Makes two enemies.
    
    for i in range(level.totalEnemies):
        # This will check if the total number of enemies is divisible by 2. If it is spawn on the lft.
        if i % 2 == 0:
    
            enemy_list[i] = Enemies(80, -50, 10, enemy_image, 3)
        # else i is an odd number and spawn on the right.
        else:
            enemy_list[i] = Enemies(500, -50, 10, enemy_image, -3)
            
# --------------------------------------------- Updating enemies
def updateEnemies():
    # Making enemies move, animate and display.
    for i in range(level.spawnedEnemies):
        enemy_list[i].move()
        enemy_list[i].animate()
        enemy_list[i].display()
        if enemy_list[i].state == FLIP:
            enemy_list[i].checkUnflip()
            
        # If both the enemy and player states are normal and they collided, print boom.
        if enemy_list[i].colliding(player) and player.state == NORM and enemy_list[i].state == NORM:
            player.die()
            
def updatePlayer():
    player.move() # Makes the player move.
    player.animate() # Animates the player.
    player.display() # Draws the player to the screen.
    
    # Check if player is not alive and the y position is off screen
    if player.yPos >= 600 and player.state != NORM:
        player.revive()
    elif player.state == REVIVE and player.yPos > 25:
        player.yPos = 25
        player.ySpeed = 0
        
def checkHittingEnemy():
    jumpHitbox = Sprite(player.xPos, player.yPos - player.spriteHeight, 15, player_image)
    
    for i in range(level.spawnedEnemies):
        if enemy_list[i].ySpeed == 0 and enemy_list[i].state != DEAD:
            if jumpHitbox.colliding(enemy_list[i]) and player.state == NORM:
                enemy_list[i].flip()
        if player.colliding(enemy_list[i]) and enemy_list[i].state == FLIP and player.state == NORM:
            enemy_list[i].die(player)
            level.defeatedEnemies += 1
                
                
def updateMilk():
    if milk.state == NORM:
        milk.display()
        milk.animate()
        checkHittingMilk()
        
def checkHittingMilk():
    if player.colliding(milk) and player.state == NORM and milk.state == NORM and player.ySpeed < 0:
        player.ySpeed = 1 # The player ySpeed is positive to fall down. 
        milk.state = DEAD
        for i in range(level.spawnedEnemies):
            if enemy_list[i].ySpeed == 0 and enemy_list[i].state != DEAD:
                enemy_list[i].flip()
        
def updateUI():
    fill(255)
    textSize(30)
    text("Lives: " + str(player.lives), 520, 490) # str converts/casts player.lives into a string to be displayed.
    text("Level: " + str(level.number), 5, 490)
    
    
def resetGame():
    player.reset()
    level.reset()
    milk.reset()
    init_enemies()
    
def showEndMenu():
    if level.defeatedEnemies == level.totalEnemies:
        textSize(50)
        fill(255)
        text("YOU BEAT THE LEVEL!!!", 50, 200)
        textSize(30)
        fill(255)
        text("ENTER to continue \n\n ESC to exit", 200, 300)
        
    else:
        textSize(100)
        fill(255)
        text("YOU LOSE.", 50, 200)
        textSize(30)
        fill(255)
        text("ENTER to restart \n\n ESC to exit", 200, 300)
    
    
def nextLevel():
    level.totalEnemies += 1 # You have to increase the num of enemies before resetting the game.
    resetGame()
    level.number += 1
    
    
    
def gameOverReset():
    resetGame()
    level.number = 1
