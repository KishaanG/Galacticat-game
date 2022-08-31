# -------------------------------------------------- Creates Level Objects
# Import the class
from Floor import Floor

# Constants.
NUM_FLOORS = 8

# Create a list to store all the floors in our game, making a temp floors with a loop. 
floor_list = [Floor(0, 0, 0, 0) for x in range(NUM_FLOORS)]

class Level:
    # ---------------------------------------------- Level Class Constructor
    def __init__(self, img):
        self.backgroundImg = img
        self.set_floors() # Calls the set_floors method so that our floors have dimensions. 
        self.totalEnemies = 1
        self.spawnTimer = 0
        self.spawnedEnemies = 0 # Enemies active in our game.
        self.number = 1
        self.defeatedEnemies = 0
        
        
    # ------------------------------------------------ Frame/Tick spawn timer
    
    def tickSpawnTimer(self):
        # Increases the timer by 1 each frame. 
        self.spawnTimer += 1
        # Frame rate for delay in timer
        if self.spawnTimer == 60:
            # Resets the timer so we can use this code again.
            self.spawnTimer = 0
            
            self.spawnedEnemies +=1 # Increase the amount of spawned enemies. 
            
            # If the spawned enemies are greater than the amount of total enemies, make them the same.
            if self.spawnedEnemies >= self.totalEnemies:
                self.spawnedEnemies = self.totalEnemies
        
# -------------------------------------------------- Display Method
    def display(self):
        image(self.backgroundImg, 0, 0)
        
        # Loop through all the floors to see if they are in the proper positions. 
        
        for i in range(NUM_FLOORS):
            floor_list[i].display()
            
    def reset(self):
        self.spawnTimer = 0
        self.spawnedEnemies = 0
        self.defeatedEnemies = 0
        
    # ---------------------------------------------- Setup Floors
    def set_floors(self):
        #Floor Layout
        # |____6   7____|
        # |   ___5___   |
        # |__3       4__|
        # |____1   2____|
        # |______0______|
        
        # Dimensions for the floor number 0.
        floor_list[0].left = -50
        floor_list[0].right = 689
        floor_list[0].top = 415
        floor_list[0].bottom = 443
        
        # Dimensions for the floor number 1.
        floor_list[1].left = -50
        floor_list[1].right = 246
        floor_list[1].top = 317
        floor_list[1].bottom = 334
        
        # Dimensions for the floor number 2.
        floor_list[2].left = 406
        floor_list[2].right = 689
        floor_list[2].top = 317
        floor_list[2].bottom = 334
        
        # Dimensions for the floor number 3.
        floor_list[3].left = -50
        floor_list[3].right = 101
        floor_list[3].top = 217
        floor_list[3].bottom = 233
        
        # Dimensions for the floor number 4.
        floor_list[4].left = 552
        floor_list[4].right = 689
        floor_list[4].top = 217
        floor_list[4].bottom = 233
        
        # Dimensions for the floor number 5.
        floor_list[5].left = 166
        floor_list[5].right = 482
        floor_list[5].top = 201
        floor_list[5].bottom = 219
        
        # Dimensions for the floor number 6.
        floor_list[6].left = -50
        floor_list[6].right = 270
        floor_list[6].top = 94
        floor_list[6].bottom = 111
        
        # Dimensions for the floor number 7.
        floor_list[7].left = 381
        floor_list[7].right = 689
        floor_list[7].top = 94
        floor_list[7].bottom = 111
        
