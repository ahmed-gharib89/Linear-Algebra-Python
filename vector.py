import math
from decimal import Decimal, getcontext

getcontext().prec = 30

class Vector(object):

    CANNOT_NORMALIZE_ZERO_VECTOR_MSG = 'Cannot normalize the zero vector'

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(self.coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be iterable')

    def __str__(self):
        return f'Vector: {self.coordinates}'

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def __add__(self, v):
        if self.dimension != v.dimension:
            raise ValueError('The 2 vectors must have the same dimensions')
        else:
            return Vector([x + y for x, y in zip(self.coordinates, v.coordinates)])

    def __sub__(self, v):
        if self.dimension != v.dimension:
            raise ValueError('The 2 vectors must have the same dimensions')
        else:
            return Vector([x - y for x, y in zip(self.coordinates, v.coordinates)])

    def times_scaler(self, c):
        return Vector([x * Decimal(c) for x in self.coordinates])

    def magnitude(self):
        return Decimal(math.sqrt(sum([x ** 2 for x in self.coordinates])))

    def normalized(self):
        try:
            return self.times_scaler(Decimal('1.0') / self.magnitude())
        except ZeroDivisionError:
            raise Exception(self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG)

    def dot(self, v):
        return sum([x * y for x,y in zip(self.coordinates, v.coordinates)])

    def angle_with(self, v, in_degrees=False):
        try:
            u1 = self.normalized()
            u2 = v.normalized()
            angle_in_radians = math.acos(u1.dot(u2))

            if in_degrees:
                degrees_per_radian = 180. / math.pi
                return angle_in_radians * degrees_per_radian
            else:
                return angle_in_radians

        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception('Cannot compute an angle with the zero vector')
            else:
                raise e


vec1 = Vector([7.887, 4.138])
vec2 = Vector([-8.802, 6.776])
vec3 = Vector([-5.955, -4.904, -1.874])
vec4 = Vector([-4.496, -8.755, 7.103])
print(vec1.angle_with(vec2, in_degrees=True))
