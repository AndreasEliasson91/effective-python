class Shape:
    pass


class Point2D(Shape):
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point2D({self.x}, {self.y})'


class Point3D(Point2D):
    __slots__ = ('z',)

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z


if __name__ == '__main__':
    point = Point2D(10, 10)
    print(point.__dict__)  # Without Shape -> Attribute Error

    point.color = 'Black'
    print(point.__dict__)
