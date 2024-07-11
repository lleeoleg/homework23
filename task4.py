"""
task 4
"""
class Flat:
    def __init__(self, square, price):
        self.square = square
        self.price = price
    def __eq__(self, other):
        return self.square == other.square
    def __ne__(self, other):
        return self.square != other.square
    def __gt__(self, other):
        return self.price > other.price
    def __lt__(self, other):
        return self.price < other.price
    def __ge__(self, other):
        return self.price >= other.price
    def __le__(self, other):
        return self.price <= other.price
if __name__ == "__main__":
    flat1 = Flat(70, 20000000)
    flat2 = Flat(100, 25000000)
    print(f"Площади квартир равны: {flat1 == flat2}")
    print(f"Площади квартир неравны: {flat1 != flat2}")
    print(f"Квартира 1 дороже квартиры 2: {flat1 > flat2}")
    print(f"Квартира 1 дешевле квартиры 2: {flat1 < flat2}")
    print(f"Квартира 1 дороже или равна по цене квартире 2: {flat1 >= flat2}")
    print(f"Квартира 1 дешевле или равна по цене квартире 2: {flat1 <= flat2}")
