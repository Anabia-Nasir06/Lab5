import math
class Triangle:
    __object_count = 0

    def __init__(self, sideA=1.0, sideB=1.0, sideC=1.0, clone_from=None):
        if clone_from is not None:
            self._sideA = clone_from.sideA
            self._sideB = clone_from._sideB
            self._sideC = clone_from._sideC
        else:
            self._sideA = sideA
            self._sideB = sideB
            self._sideC = sideC

        Triangle.__object_count += 1

    @property
    def sideA(self):
        return self._sideA

    @sideA.setter
    def sideA(self, value):
        if value <= 0:
            raise ValueError("Side A must be positive")
        self._sideA = value

    @property
    def sideB(self):
        return self._sideB

    @sideB.setter
    def sideB(self, value):
        if value <= 0:
            raise ValueError("Side B must be positive")
        self._sideB = value

    @property
    def sideC(self):
        return self._sideC

    @sideC.setter
    def sideC(self, value):
        if value <= 0:
            raise ValueError("Side C must be positive")
        self._sideC = value

    def perimeter(self):
        return self.sideA + self.sideB + self.sideC

    def isRightAngled(self):
        a = self.sideA
        b = self.sideB
        c = self.sideC
        # Sort manually without using tuple
        if a > b:
            a, b = b, a
        if b > c:
            b, c = c, b
        if a > b:
            a, b = b, a
        return math.isclose(a * a + b * b, c * c, rel_tol=1e-9)
    
    @classmethod
    def objectCount(cls):
        return cls.__object_count

    def __str__(self):
        return f"\nTriangle with sides: {self.sideA}, {self.sideB}, {self.sideC}"