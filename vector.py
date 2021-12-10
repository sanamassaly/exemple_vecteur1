import math
class Vecteur:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def longueur(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    def set_x_y(self,x,y):
        assert isinstance(x, int), "Entrer la valeur entiere pas un(e) %r!"%type(x)
        assert isinstance(y, int), "Entrer la valeur entiere pas un(e) %r!"%type(y)
        self.x = x
        self.y = y

    def get_x_y(self):
        return self.x , self.y

    


vect1 = Vecteur(2, 5)
print(vect1.longueur())

    
