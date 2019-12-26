# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 10:50:55 2019

@author: Carter
"""

#test Code
from vector import Vector
from line import Line


#Test Vector class
v1 = Vector([8.462,7.893,-8.187])
v2 = Vector([6.984,-5.975,4.778]) 

v3 = v1.minus(v2)

#test Line code
#test code    
l1 = Line([2,3],4)
l2 = Line([2,3],6)
l3 = Line([4,5],3)

a = l1.is_parallel(l2)
b = l1.is_parallel(l3)
##print a
##print b

#test is_equal Function
m = Line([2,3],4)
n = Line([3,6],8)

out = m.is_equal(n)
print(out)


#test intersection
print(m.intersection(n))

#quiz lines
A = Line([4.046, 2.836], 1.21)
B = Line([10.115,7.090], 3.025)
print(A.intersection(B))

C = Line([7.204, 3.182], 8.68)
D=  Line([8.172, 4.114], 9.883)
print(C.intersection(D))

E = Line([1.182,5.562], 6.744)
F = Line([1.773, 8.343], 9.525)
print(E.intersection(F))
print(E.is_parallel(F))