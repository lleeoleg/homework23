"""
task 2
"""
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    def __str__(self):
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {-self.imag}i"
    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)
    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)
    def __mul__(self, other):
        new_real = self.real * other.real - self.imag * other.imag
        new_imag = self.real * other.imag + self.imag * other.real
        return Complex(new_real, new_imag)
    def __truediv__(self, other):
        denominator = other.real**2 + other.imag**2
        new_real = (self.real * other.real + self.imag * other.imag) / denominator
        new_imag = (self.imag * other.real - self.real * other.imag) / denominator
        return Complex(new_real, new_imag)

if __name__ == "__main__":
    c1 = Complex(2, 3)
    c2 = Complex(4, -5)
    print("c1 =", c1)
    print("c2 =", c2)
    print("c1 + c2 =", c1 + c2)
    print("c1 - c2 =", c1 - c2)
    print("c1 * c2 =", c1 * c2)
    print("c1 / c2 =", c1 / c2)
