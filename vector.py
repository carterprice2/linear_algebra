# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 19:51:51 2019

@author: Carter
"""
import math
import decimal

# note all vectors must have the same length

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(self.coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')
    
    def plus(self,v):
        #new_coordinates = [x+y for x,y in zip(self.coordinates, v.coordinates)]
        new_coordinates = []
        n = len(self.coordinates)
        for i in range(n):
            new_coordinates.append(self.coordinates[i] + v.coordinates[i])
        return Vector(new_coordinates)
    
    def minus(self,v):
        new_coordinates = [x-y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)
    
    def scalar(self, c):
        new_coordinates = [c*x for x in self.coordinates]
        return Vector(new_coordinates)
    
    #returns the magnitude of the vector 
    def magnitude(self):
        sum_square = 0
        n = len(self.coordinates)
        for i in range(n):
            sum_square = sum_square + self.coordinates[i]**2
        a = math.sqrt(sum_square)
        return a
    
    #this function returns the unit vector
    def normalize(self):
        try:
            m = self.magnitude()
            unit_coordinates = []
            n = self.dimension
            for i in range(n):
                unit_coordinates.append(1/m * self.coordinates[i])
            return Vector(unit_coordinates)
        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector')
     
    #dot product or inner product
    def dot(self,v):
        n = len(self.coordinates)
        sum = 0
        for i in range(n):
            sum = sum + self.coordinates[i]*v.coordinates[i]
        return sum
    
    #find angle between two vectors
    def dot_angle(self,v):
        dot = self.dot(v)
        mag1 = self.magnitude()
        mag2 = v.magnitude()
        intermediate = dot/(mag1*mag2)
        angle = math.acos(intermediate)
        return angle
    
    #check parallel
    def parallel(self,v):
        if  self.is_zero() or v.is_zero() or abs(self.dot_angle(v)) < 1e-10 or self.dot_angle(v) == math.pi:
            return True
        else:
            return False
        
    def orthogonal(self,v):
        return (self.dot(v) < 1e-10)
    
    def is_zero(self):
        return (self.magnitude() < 1e-10)
    
    # projection of vector onto a basis vector
    def projection(self,basis):
        new_vector = []
        inter1 = basis.normalize()
        inter2 = self.dot(inter1)
        return inter1.scalar(inter2)
    
    def proj_orth(self,basis):
        intermediate = self.projection(basis)
        new_vector = self.minus(intermediate)
        return new_vector
    
    #only works for x,y,z coordinate vectors
    def cross_product(self, w):
        new_vector = []
        new_vector.append(self.coordinates[1]*w.coordinates[2] - w.coordinates[1]*self.coordinates[2])
        new_vector.append(-(self.coordinates[0]*w.coordinates[2] - w.coordinates[0]*self.coordinates[2]))
        new_vector.append(self.coordinates[0]*w.coordinates[1] - w.coordinates[0]*self.coordinates[1])
        return Vector(new_vector)
    
    def area_parallelogram(self,v):
        cp = self.cross_product(v)
        return cp.magnitude()
    
    def area_tri(self,v):
        return self.area_parallelogram(v) / 2.0
    
    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates
    
    
v1 = Vector([8.462,7.893,-8.187])
v2 = Vector([6.984,-5.975,4.778])  
