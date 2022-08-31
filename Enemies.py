'''
Enemy Class.
'''

# Imports:
from Sprite_Kishaan import Sprite, FLIP, NORM, DEAD, REVIVE

# ----------------------------------------------------- Main

class Enemies(Sprite): # Make sure Sprite is in the circle brackets to avoid any errors with inheritance.
    # ----------------------------------------------------------- Constructor
    def __init__(self, x, y, n, img, speed):
        super(Enemies, self).__init__(x, y, n, img)
        self.rightSpeed = speed
        self.maxFlipDuration = int(random(50, 350))
        self.flipTimer = 0
        self.startSpeed = self.rightSpeed
        
        
    def flip(self):
        self.state = FLIP
        self.leftSpeed = 0
        self.rightSpeed = 0
        self.ySpeed = -12
        
    def unflip(self):
        self.state = NORM
        self.rightSpeed = self.startSpeed
        self.flipTimer = 0
        
    def checkUnflip(self):
        self.flipTimer += 1
        if self.flipTimer >= self.maxFlipDuration:
            self.unflip()
        
    def die(self, other):
        self.state = DEAD
        self.ySpeed = -20
        self.rightSpeed = other.xSpeed * 2
        
        
    # ---------------------------------------------------------- Animate
    
    def animate(self): # Overriding
        # Starts increasing the counter so that the images can cycle through.
        self.animCounter += 1
        
        # If the animation timer reaches 3 frames.
        if self.animCounter > 3:
        # Reset the animation counter.
            self.animCounter = 0
            # Increase the pose by 1.
            self.pose += 1
                
        
        if self.state == FLIP:
            if self.pose < 8 or self.pose > 9:
                self.pose = 8
                
        else: 

            # If self.ySpeed does not equal zero.
            if self.ySpeed <> 0:
                # If pose is less than 4 or greater than 7.
                if self.pose < 4 or self.pose > 7:
                    self.pose = 4
            
            # If xSpeed is greater than 0.
            elif self.xSpeed > 0:
                # If pose is greater than 1.
                if self.pose > 1:
                    self.pose = 0
                    
            # If xSpeed is less than 0.
            elif self.xSpeed < 0:
                # If pose if less than 2 or greater than 3.
                if self.pose > 3 or self.pose < 2:
                    self.pose = 2
                    
            # If the player is not moving
            elif self.xSpeed == 0:
                # If the player if facing right.
                if self.facingR:
                    self.pose = 0
                else:
                    self.pose = 2
