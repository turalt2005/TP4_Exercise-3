#Troy Tural 404
#Exercise 3

import math

class cercle:
   def __init__(self,rayon):
       self.rayon = rayon

   def aire_cercle(self):
       return math.pi * self.rayon * self.rayon

   def cironference_cercle(self):
       return 2 * math.pi * self.rayon
