from Sprite_Kishaan import Sprite, NORM, DEAD, REVIVE

class PowerUp(Sprite):
    def __init__(self, x, y, n, img):
        super(PowerUp, self).__init__(x, y, n, img)
        
    def animate(self):
        self.animCounter += 1
        
        if self.animCounter > 3: # Checks if 3 the animation counter is greater than 3.
            self.animCounter = 0 # Resets the animation counter.
            self.pose += 1 # Change to the next pose. 
            if self.pose > 9: # If the pose of the milk is greater than 9, reset to the 0th pose.
                self.pose = 0

    def reset(self):
        self.state = NORM
