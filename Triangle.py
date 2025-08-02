import math
class Triangle:
    __object_count = 0

    def __init__(self, sideA=None, sideB=None, sideC=None):
        if sideA is None and sideB is None and sideC is None:   # Similar to Default Construtor
            self._sideA = 1.0
            self._sideB = 1.0
            self._sideC = 1.0

        elif sideA is not None and sideB is None and sideC is None:
            if isinstance(sideA, Triangle):                     # Clone constructor
                self._sideA = sideA._sideA
                self._sideB = sideA._sideB
                self._sideC = sideA._sideC
            else:                                                # One-parameter constructor (equilateral)
                self._sideA = sideA
                self._sideB = sideA
                self._sideC = sideA

        elif sideA is not None and sideB is not None and sideC is None:   # Two-parameter constructor (isosceles x, x, y)
            self._sideA = sideA
            self._sideB = sideA
            self._sideC = sideB

        elif sideA is not None and sideB is not None and sideC is not None:    # Three-parameter constructor
            self._sideA = sideA
            self._sideB = sideB
            self._sideC = sideC

        else:
            print("Invalid input")
            self._sideA = 0.0
            self._sideB = 0.0
            self._sideC = 0.0

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