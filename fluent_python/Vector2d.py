class Vector:


    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x,y)

    def __mul__(self):
        raise NotImplemented

    def __repr__(self):
        return 'Vector({}, {})'.format(self.x, self.y)



v1 = Vector(2, 5)
v2 = Vector(3, 4)
print(v1)
print(v1 + v2)
