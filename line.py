from decimal import Decimal, getcontext

from vector import Vector

getcontext().prec = 30


class Line(object):

    NO_NONZERO_ELTS_FOUND_MSG = 'No nonzero elements found'

    #defines the line by its normal vector and the constant for the line's equation
    #equation in the form of Ax + By = k, [A B] <- normal vector, k <- constant
    def __init__(self, normal_vector=None, constant_term=None):
        self.dimension = 2

        if not normal_vector:
            all_zeros = ['0']*self.dimension
            normal_vector = Vector(all_zeros)
        self.normal_vector = normal_vector

        if not constant_term:
            constant_term = Decimal('0')
        self.constant_term = Decimal(constant_term)

        self.set_basepoint()
        #print 'Line Initialized'


    def set_basepoint(self):
        try:
            n = self.normal_vector
            c = self.constant_term
            basepoint_coords = ['0']*self.dimension

            initial_index = Line.first_nonzero_index(n)
            initial_coefficient = n[initial_index]

            basepoint_coords[initial_index] = float(c)/float(initial_coefficient)
            self.basepoint = Vector(basepoint_coords)

        except Exception as e:
            if str(e) == Line.NO_NONZERO_ELTS_FOUND_MSG:
                self.basepoint = None
            else:
                raise e


    def __str__(self):

        num_decimal_places = 3

        def write_coefficient(coefficient, is_initial_term=False):
            coefficient = round(coefficient, num_decimal_places)
            if coefficient % 1 == 0:
                coefficient = int(coefficient)

            output = ''

            if coefficient < 0:
                output += '-'
            if coefficient > 0 and not is_initial_term:
                output += '+'

            if not is_initial_term:
                output += ' '

            if abs(coefficient) != 1:
                output += '{}'.format(abs(coefficient))

            return output

        n = self.normal_vector

        try:
            initial_index = Line.first_nonzero_index(n)
            terms = [write_coefficient(n[i], is_initial_term=(i==initial_index)) + 'x_{}'.format(i+1)
                     for i in range(self.dimension) if round(n[i], num_decimal_places) != 0]
            output = ' '.join(terms)

        except Exception as e:
            if str(e) == self.NO_NONZERO_ELTS_FOUND_MSG:
                output = '0'
            else:
                raise e

        constant = round(self.constant_term, num_decimal_places)
        if constant % 1 == 0:
            constant = int(constant)
        output += ' = {}'.format(constant)

        return output

    def is_parallel(self, Line):
        v1 = Vector(self.normal_vector)
        v2 = Vector(Line.normal_vector)
        return v1.parallel(v2)

        #TODO finish this function for seeing if two lines are equal
    def is_equal(self, Line):
        if not self.is_parallel(Line):
                return False
        a = self.basepoint
        b = Line.basepoint 
        
        if a.coordinates == b.coordinates:
            return True
        else:
            return False
        
    def intersection(self, Line):
        #check if the lines are parallel /equal
        if self.is_parallel(Line):
            if self.is_equal(Line):
                print("SAME LINE")
                return (float("inf"), float("inf"))
            else:
                print("NO INTERSECTION")
                return (None,None)
        
        A = float(self.normal_vector[0])
        B = float(self.normal_vector[1])
        C = float(Line.normal_vector[0])
        D = float(Line.normal_vector[1])
        k1 = float(self.constant_term)
        k2 = float(Line.constant_term)
        
        denom = A*D - B*C
        x = (D*k1 - B*k2)/denom
        y = (-C*k1 + A*k2)/denom
        return (x,y)
        
        
            
    @staticmethod
    def first_nonzero_index(iterable):
        for k, item in enumerate(iterable):
            if not MyDecimal(item).is_near_zero():
                return k
        raise Exception(Line.NO_NONZERO_ELTS_FOUND_MSG)


class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps




