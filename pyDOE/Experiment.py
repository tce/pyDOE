from pyDOE.doe_factorial import *


d1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
d2 = [10, 11, 12, 13, 14]
d3 = ['a', 'b', 'c']


all_experiments = fullfact([d1.__len__(), d2.__len__(), d3.__len__()])


def exp(sample):
    print(d1[int(sample[0])],  d2[int(sample[1])],  d3[int(sample[2])])


for x in range(10):
    exp(all_experiments[x])


def eval(p1, p2, p3):
    print(p1, p2, p3)




