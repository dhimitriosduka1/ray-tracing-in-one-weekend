import math


class Vec3:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def dot_product(self, other) -> float:
        assert isinstance(other, Vec3)
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross_product(self, other):
        assert isinstance(other, Vec3)
        return Vec3(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )

    def magnitude(self) -> float:
        return math.sqrt(self.dot_product(self))

    def normalize(self):
        return self / self.magnitude()

    def __add__(self, other):
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

    def __sub__(self, other):
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        assert not isinstance(other, Vec3)
        return Vec3(self.x * other, self.y * other, self.z * other)

    def __imul__(self, other):
        assert not isinstance(other, Vec3)
        self.x *= other.x
        self.y *= other.y
        self.z *= other.z
        return self

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        assert not isinstance(other, Vec3)
        return self.__mul__(1 / other)

    def __itruediv__(self, other):
        return self.__truediv__(other)

    def __str__(self) -> str:
        return f'x: {self.x}, y: {self.y}, z:{self.z}'
