import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def get_contents(self):
        l = []
        for k in self.__dict__:
            for i in range(self.__dict__[k]):
                l.append(k)
        return l        
    
#def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

h = Hat(red = 2, blue = 1)
print(h.get_contents())