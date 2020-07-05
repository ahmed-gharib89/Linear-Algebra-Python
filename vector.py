class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimintion = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be iterable')

    def __str__(self):
        return f'Vector: {self.coordinates}'

    def __eq__(self, v):
        return self.coordinates == v.coordinates

vector = Vector([1, 2, 3])

print(vector)