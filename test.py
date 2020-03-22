# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 10:50:55 2019

@author: Carter
"""

#test Code
from vector import Vector
from line import Line
from plane import Plane

#Test Vector class
v1 = Vector([8.462,7.893,-8.187])
v2 = Vector([6.984,-5.975,4.778]) 

v1 = Vector([7.35,0.221,5.188])
v2 = Vector([2.751,8.259,3.985]) 

v3 = v1.minus(v2)

v1.dot_angle(v2)


#test Line code
#test code    
l1 = Line([2,3],6)
l2 = Line([2,3],6)
l3 = Line([4,5],3)

a = l1.is_parallel(l2)
b = l1.is_parallel(l3)
##print a
##print b

#test is_equal Function
m = Line([2,3],4)
n = Line([3,6],8)
m = Line([3,6],8)
out = m.is_equal(n, debug=False)
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


#test Plane Class

A = Plane([-0.412, 3.806,0.728], -3.46)
B = Plane([1.03,-9.515, -1.82], 8.65)
A.is_parallel(B)
A.is_equal(B)

C = Plane([2.611, 5.528,0.283], 4.6)
D = Plane([7.715,8.306, 5.342], 3.76)
C.is_parallel(D)
C.is_equal(D)

E= Plane([-7.926, 8.625,-7.212], -7.952)
F= Plane([-2.642, 2.875,-2.404], -2.443)

E.is_parallel(F)
E.is_equal(F)