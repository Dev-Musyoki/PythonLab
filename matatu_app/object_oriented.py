# Object Oriented Programming: Inheritance, Abstraction, Polymorphism, Overloading
# ABC provides a way to define abstract base classes in Python. abstractmethod marks a method that subclasses are required to implement.

from abc import ABC, abstractmethod
from functools import singledispatchmethod

# PART 1: INHERITANCE (Vehicle -> Matatu, Bus): Concept that allows a class to inherit attributes and methods from another class. The parent class is called the superclass, and the child class is called the subclass. The subclass can override or extend the functionality of the superclass.

# It involves a IS-A relationship: Example: A Matatu IS-A Vehicle, A Bus IS-A Vehicle.
class Vehicle: # The parent class (Superclass/Base class)
    def __init__(self, plate, capacity):
        self.plate = plate
        self.capacity = capacity
        self._passengers = 0

    def board(self, count=1):
        if self._passengers + count > self.capacity:
            print(f"{self.plate}: cannot board {count}, {self.seats_left} seats left")
            return False
        self._passengers += count
        return True

    @property
    def seats_left(self):
        return self.capacity - self._passengers

    def describe(self):
        return f"{self.plate} ({type(self).__name__}, {self.capacity} seats)"


class Matatu(Vehicle):
    def __init__(self, plate, capacity=14, sacco="Unaffiliated"):
        super().__init__(plate, capacity)      # let the parent set up plate/capacity
        self.sacco = sacco

    def describe(self):                        # override: extend the parent's version
        return f"{super().describe()} - Sacco: {self.sacco}"


class Bus(Vehicle):
    def __init__(self, plate, capacity=50, has_wifi=False):
        super().__init__(plate, capacity)
        self.has_wifi = has_wifi



# PART 2: ABSTRACTION (an abstract base class) + POLYMORPHISM
# Abstraction: Concept of hiding the complex implementation details and showing only the essential features of an object.

class FareStrategy(ABC): # (Abstract base class) - Set of rules that concrete classes must follow.
    @abstractmethod
    def calculate(self, base_fare):
        """Every concrete strategy MUST implement this."""

    def label(self):                           # concrete method, inherited as-is
        return type(self).__name__


class StandardFare(FareStrategy):
    def calculate(self, base_fare):
        return base_fare


class PeakFare(FareStrategy):
    def calculate(self, base_fare):
        return base_fare * 1.5


class RainyDayFare(FareStrategy):
    def calculate(self, base_fare):
        return base_fare + 20


class StudentFare(FareStrategy):
    def calculate(self, base_fare):
        return base_fare * 0.8

# Composition: A design principle where a class is composed of one or more objects from other classes, allowing for flexible and reusable code. It means building a class using objects of other classes as components. It involves a HAS-A relationship: Example: A Trip HAS-A FareStrategy.
class Trip:
    """Has-a strategy (composition): the Trip doesn't care WHICH strategy it holds."""

    def __init__(self, route_name, base_fare, strategy):
        self.route_name = route_name
        self.base_fare = base_fare
        self.strategy = strategy

    def fare(self):
        return self.strategy.calculate(self.base_fare)


class HolidayFare:   # NOT a FareStrategy subclass: duck typing. An object suitability is often determined by the operations it supports, rather than its exact class type. If it walks like a duck and quacks like a duck, treat it like a duck. HolidayFare has a calculate() method, so it can be used as a strategy in Trip.fare().
    def calculate(self, base_fare):
        return base_fare * 2



# PART 3: METHOD OVERLOADING: Concept where multiple methods can have the same name but accept different parameters (number or type) or arguments.


class FareCalculator:
    # Python has no method overloading by signature: use defaults and *args
    def price(self, distance_km, rate_per_km=10, *surcharges):
        return distance_km * rate_per_km + sum(surcharges)


class Payment:
    # Dispatch on the TYPE of the argument
    # The singledispatchmethod decorator allows a method to have different impementations based on the type of its first non-self argument.
    @singledispatchmethod 
    def pay(self, method):
        return "Unsupported payment"

    @pay.register(int)
    def _(self, amount):
        return f"Paid Ksh {amount} cash"

    @pay.register(str)
    def _(self, phone):
        return f"M-Pesa prompt sent to {phone}"


class Fare:
    # Operator overloading: make + < == work on our own objects : Operator overloading allows us to customize how operators behave when used with objects of our own classes.
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Fare(self.amount + other.amount)

    def __lt__(self, other):
        return self.amount < other.amount

    def __eq__(self, other):
        return self.amount == other.amount

    def __str__(self):
        return f"Ksh {self.amount}"



# THE DEMO

def main():
    print("--- Inheritance ---")
    van = Matatu("KDA 123X", sacco="Rongai Sacco")
    bus = Bus("KCB 456Y", has_wifi=True)

    print(van.describe())
    print(bus.describe())
    van.board(10)
    print(van.seats_left)
    van.board(6)
    print(isinstance(van, Vehicle))
    print(isinstance(van, Bus))
    print(issubclass(Bus, Vehicle))
    print([cls.__name__ for cls in Matatu.__mro__]) # MRO: Method Resolution Order:demonstrates the order python uses when searching for attributes and methods in a class hierarchy.
    
    print("--- Polymorphism (vehicles) ---")
    for vehicle in [van, bus]:
        print(vehicle.describe())

    print("--- Abstraction ---")
    try:
        FareStrategy()
    except TypeError as e:
        print(type(e).__name__, "- cannot instantiate an abstract class")

    print("--- Polymorphism (fare strategies) ---")
    strategies = [StandardFare(), PeakFare(), RainyDayFare(), StudentFare()]
    for strategy in strategies:
        print(f"{strategy.label():<13} -> Ksh {strategy.calculate(100):.0f}")

    print("--- Swapping behaviour at runtime ---")
    trip = Trip("CBD - Rongai", 100, StandardFare())
    print(trip.fare())
    trip.strategy = RainyDayFare()
    print(trip.fare())
    trip.strategy = HolidayFare()
    print(trip.fare())

    print("--- Overloading, Python style ---")
    calc = FareCalculator()
    print(calc.price(8))
    print(calc.price(8, 15))
    print(calc.price(8, 15, 20, 10))

    payment = Payment()
    print(payment.pay(100))
    print(payment.pay("0712345678"))
    print(payment.pay(None))

    print("--- Operator overloading ---")
    print(Fare(50) + Fare(80))
    print(Fare(50) < Fare(80))
    print(Fare(50) == Fare(50))
    print([str(f) for f in sorted([Fare(100), Fare(50), Fare(80)])])


if __name__ == "__main__":
    main()