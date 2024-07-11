"""
task 3
"""
class Airplane:
    def __init__(self, type, passengers):
        self.type = type
        self.passengers = passengers
    def __eq__(self, other):
        return self.type == other.type
    def __gt__(self, other):
        return self.passengers > other.passengers
    def __lt__(self, other):
        return self.passengers < other.passengers
    def __ge__(self, other):
        return self.passengers >= other.passengers
    def __le__(self, other):
        return self.passengers <= other.passengers
    def __add__(self, other):
        return Airplane(self.type, self.passengers + other)
    def __sub__(self, other):
        return Airplane(self.type, self.passengers - other)
    def __iadd__(self, other):
        self.passengers += other
        return self
    def __isub__(self, other):
        self.passengers -= other
        return self
    def __str__(self):
        return f"Type: {self.type}, Passengers: {self.passengers}"

if __name__ == "__main__":
    airplane1 = Airplane("Boeing", 60)
    airplane2 = Airplane("Scat", 40)
    
    print("--------")
    print(airplane1 == airplane2)
    print(airplane1 > airplane2)
    print(airplane1 < airplane2)
    print(airplane1 >= airplane2)
    print(airplane1 <= airplane2) 
    print("---------")
    
    airplane1 += 20
    print(airplane1)
    
    airplane2 -= 10
    print(airplane2)
