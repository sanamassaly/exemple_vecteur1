import math
class Vecteur:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def longueur(self):
        return math.sqrt(self.x**2 + self.y**2)
vect1 = Vecteur(2, 5)
print(vect1.longueur())

    
