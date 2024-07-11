"""
task 5
"""
class Roman:
    def __init__(self, roman_numeral):
        self.roman_numeral = roman_numeral
    @staticmethod
    def to_integer(roman):
        roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        prev_value = 0
        for char in roman[::-1]:
            value = roman_numerals[char]
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value
        return total
    def __add__(self, other):
        result = self.value + other.value
        return Roman(Roman.to_roman(result))
    def __sub__(self, other):
        result = self.value - other.value
        return Roman(Roman.to_roman(result))
    def __mul__(self, other):
        result = self.value * other.value
        return Roman(Roman.to_roman(result))
    def __truediv__(self, other):
        result = self.value // other.value
        return Roman(Roman.to_roman(result))
    def __str__(self):
        return self.roman_numeral
roman1 = Roman('XII')
roman2 = Roman('IV')