import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        l = []
        for k in self.__dict__:
            for i in range(self.__dict__[k]):
                l.append(k)
        self.contents = l

    def draw (self, NumBalls):
        res = []
        if NumBalls <= len(self.contents):
            for i, val in enumerate(self.contents):
                if i < int(NumBalls) :
                    x = random.randint(0, len(self.contents) - 1)
                    res.append(self.contents[x])
                    self.contents.pop(x)
            return res
        else:
            return self.contents

def comparelist (list1, list2):
    #for i, val in enumerate(list2):
    i = 0
    while i < len(list2):
        if len(list2) == 0:
            return True    
        for j, val in enumerate(list1):
            if list2[i] == list1[j]:
                list2.pop(i)
                list1.pop(j)
                i = 0
                break
            if j == len(list1) - 1:
                i = i + 1
    if len(list2) == 0:
        return True
    else:
        return False


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0
    exp = []
    res = []
    for k in expected_balls:
        for i in range(expected_balls[k]):
            exp.append(k)
    for i in range(num_experiments):
        l = copy.deepcopy(hat)
        res = l.draw(num_balls_drawn)
        exp2 = copy.deepcopy(exp)
        check = comparelist(res, exp2)
        if check:
            M = M + 1
    return M/num_experiments


hat = Hat(blue=3,red=2,green=6)
probability = experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000)
print(probability)