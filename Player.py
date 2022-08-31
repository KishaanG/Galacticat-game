# Player class - Deals with everything to do with the player. 

# Import Sprite file into player.
from Sprite_Kishaan import Sprite, NORM, DEAD, REVIVE

# Inheritance works like this, we give a super class with brackets. 
class Player(Sprite):
    
    # ------------------------------------------------------------------------------------ Player Constructor
    
    def __init__(self, x, y, n, img):
        # Super calls the inheritance class so we can build on top of it.
        super(Player, self).__init__(x, y, n, img)
        self.startingXVal = x
        self.startingYVal = y
        self.lives = 3
        
        
    def die(self):
        self.state = DEAD
        self.leftSpeed = 0
        self.rightSpeed = 0
        self.ySpeed = -12
        self.lives -= 1
        
    def revive(self):
        self.state = REVIVE
        self.xPos = 310
        self.yPos = -50
        self.ySpeed = 0
        
    def reset(self):
        self.xPos = self.startingXVal
        self.yPos = self.startingYVal
        self.state = NORM
        self.ySpeed = 0
        self.lives = 3
