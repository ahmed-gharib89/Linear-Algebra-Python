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

    def __mul__(self, n):
        return Vector([self.coordinates[i] * n for i in range(len(self.coordinates))])


vector = Vector([1.671, -1.012, -0.318])
vector2 = Vector([-8.223, 0.878])
print(vector * 7.41)