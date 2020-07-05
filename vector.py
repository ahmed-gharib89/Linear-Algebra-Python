import math
class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

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
            return Vector([self.coordinates[i] + v.coordinates[i] for i in range(len(self.coordinates))])

    def __sub__(self, v):
        if self.dimension != v.dimension:
            raise ValueError('The 2 vectors must have the same dimensions')
        else:
            return Vector([self.coordinates[i] - v.coordinates[i] for i in range(len(self.coordinates))])

    def times_scaler(self, n):
        return Vector([x * n for x in self.coordinates])

    def magnitude(self):
        return math.sqrt(sum([x ** 2 for x in self.coordinates]))

    def normalized(self):
        try:
            return self.times_scaler(1 / self.magnitude())
        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector')


vector = Vector([-0.221, 7.437])
vector2 = Vector([8.813, -1.33, -6.247])
vec3 = Vector([5.581, -2.136])
vec4 = Vector([1.966, 3.108, -4.554])
print(Vector.magnitude(vector))
print(Vector.magnitude(vector2))
print(Vector.normalized(vec3))
print(Vector.normalizedgit(vec4))