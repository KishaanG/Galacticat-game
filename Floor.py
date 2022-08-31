# Floor class

class Floor:
    # ------------------------------------------ Floor class constructor

    def __init__(self, left, right, top, bottom):
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom
        
    # ------------------------------------------
    
    def display(self): # Self checks for anything inside of this class.
        # Filling the rectangle with RGB (first 3 parameters) and transparency (last parameter).
        fill(255, 255, 255, 100)
        
        # Calculate the height and width of our floors. 
        # Calculate the width of the floor. 
        w = self.right - self.left # Right is always the higher number because it is further right on the screen.
        
        # Calculate the height of the floor.
        h = self.bottom - self.top # Bottom is always the higher number because it is further down the screen.
        
        # Draw a temporary rectangle to see if the floors are drawn.
        rect(self.left, self.top, w, h)
        
        
