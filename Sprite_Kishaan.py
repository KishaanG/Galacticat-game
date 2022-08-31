'''
Sprite Class
'''

#--------------------------------- Import levels and FLoors

from Level import floor_list, NUM_FLOORS

#--------------------------------- Global Constants
GRAVITY = 2
TERMINAL_VELOCITY = 7

# Sprite states
NORM = 0
DEAD = 1
REVIVE = 2
FLIP = 3

#--------------------------------- Creates Sprite Objects
class Sprite(object):
    #----------------------------- Sprite Class Constructor
    # Constructor - It will build the class with a starting value of variables. Can add parameters that we can take when calling it.
    # Parameter - newMethod(value1, value2, value3) - The values inside are parameters. Requirments to use the method.
    def __init__ (self, x, y, n, img): # THIS IS THE CONSTRUCTOR! 
        # n is the number of images we have in total.
        self.xPos = x # self.nameOfVariable - That allows for a variable to be created inside the Sprite class.
        self.yPos = y # Sets the y-position for our Sprite.
        self.playerFullImage = img # Gets the full image of the player.
        self.spriteWidth = img.width # This will be the width of our sprite.
        self.spriteHeight = img.height/n # This will get the height of ONE sprite image.
        self.xSpeed = 0 # Sets the speed of our sprite.
        # Starting speeds of our sprite.
        self.rightSpeed = 0
        self.leftSpeed = 0
        self.ySpeed = 0 # Sets the y speed of our sprite. 
        self.animCounter = 0 # Starts the counter at 0.
        self.pose = 0 # Starting animation pose.
        self.facingR = True
        
        self.radius = self.spriteWidth / 2
        self.state = NORM # This starts us at normal.
        
  #-------------------------------------------------------------- Sprite Display      
    def display(self): # Displays the image to the screen.
        copy(self.playerFullImage, 0, self.spriteHeight * self.pose, self.spriteWidth, self.spriteHeight, \
             self.xPos, self.yPos, self.spriteWidth, self.spriteHeight)
  #-------------------------------------------------------------- Sprite Move
    def move(self):
        # Change the position and increase the speed.
        # Calculate the xSpeed.
        self.xSpeed = self.rightSpeed + self.leftSpeed
        
        # Increases the position based on the x speed. 
        self.xPos += self.xSpeed
        
        # Call the new method for setting ySpeed
        self.set_y_speed()


        # Increases the y position based on the y speed.
        self.yPos += self.ySpeed   
        
        # Screen wrapping
        # Check if the right side of the sprite past the origin of the x axis.
        if self.state == NORM:
            if self.xPos + self.spriteWidth < 0:
                self.xPos = 640
                # If the player leaves the screen on the bottom floor, they teleport to the top of the screen. 
                if self.yPos + self.spriteHeight >= floor_list[0].top:
                    self.yPos = 0
            
            # Check if we go off the right, then spawn on left "in the void."
            elif self.xPos > 640:
                self.xPos = 0 - self.spriteWidth
                # If the player leaves the screen on the bottom floor, they teleport to the top of the screen. 
                if self.yPos + self.spriteHeight >= floor_list[0].top:
                    self.yPos = 0
            
        elif self.yPos > 640:
            self.ySpeed = 0
            self.rightSpeed = 0
            self.leftSpeed = 0
#-------------------------------------------------------------- Set y speed (Floor logic)
    def set_y_speed(self):
        self.ySpeed += GRAVITY

        # Float when falling instead of crashing down. 
        if self.ySpeed > TERMINAL_VELOCITY:
            self.ySpeed = TERMINAL_VELOCITY
            
            
        if self.state == DEAD:
            return
        
        bottom = self.yPos + self.spriteHeight
        nextBottom = bottom + self.ySpeed
        nextTop = self.yPos + self.ySpeed
        
        # For every floor, check if we are on the floor. 
        for i in range(NUM_FLOORS):
            # Check if sprite's xPosition is the same as the floor on the x axis.
            if self.xPos < floor_list[i].right and self.xPos + self.spriteWidth > floor_list[i].left:
                
                # Check if the sprite's next y position hits the floor's top.
                # AND if the sprite's image bottom is still above the floor's top. 
                if nextBottom > floor_list[i].top and bottom <= floor_list[i].top:
                    
                    # Set sprite y position above the floor and stop it's y speed. 
                    self.yPos = floor_list[i].top - self.spriteHeight
                    self.ySpeed = 0
                # Checks if the nextTop is h
                if nextTop < floor_list[i].bottom and self.yPos >= floor_list[i].bottom:
                    self.yPos  = floor_list[i].bottom
                    self.ySpeed = 0
            
#-------------------------------------------------------------- Animate Move

    def animate(self):
        self.animCounter += 1 # Starts increasing the counter. 
        
        # If the counter is greater than 3 times, then resets the counter.
        if self.animCounter > 3:
            # Reset the counter
            self.animCounter = 0
            # Increase the pose by 1.
            self.pose += 1
            
            
        
        if self.state == NORM:
            # Jumping animations.
            if self.ySpeed <> 0:
                # Check if you're facing right or left.
                if self.facingR:
                    self.pose = 8
                else:
                    self.pose = 9
                    
            # Moving to the left animation.
            elif self.xSpeed < 0:
                # Checking the range of poses between 3 and 5 in our sprite sheet.
                # Set the pose to 3.
                if self.pose < 3 or self.pose > 5:
                    self.pose = 3
                    
            # Moving to the right animation.
            elif self.xSpeed > 0:
                # Checking the range of poses between 0 and 2 in our sprite sheet.
                # Set the pose to 0.
                if self.pose > 2:
                    self.pose = 0
            
            # Idle animation.
            elif self.xSpeed == 0:
                if self.facingR:
                    self.pose = 6
                else:
                    self.pose = 7
        
        elif self.state == DEAD:
            if self.pose < 12 or self.pose > 13:
                self.pose = 12
            
        elif self.state == REVIVE:
            self.pose = 14
                
#-------------------------------------------------------------- Animate Move
    def colliding(self, other):
        # Determine collision using pythag theorem
        a = other.xPos - self.xPos
        b = other.yPos - self.yPos
        
        # Rearrange theorem to solve for c. sqrt = 
        c = sqrt(a**2 + b**2)
        
        
        if c < self.radius + other.radius:
            return True
        else:
            return False
