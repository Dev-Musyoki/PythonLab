# Class, object and constructor

# A class is the blueprint, and an object is one thing built from it. __init__ is the constructor, which runs automatically when you create an object. self is the object being built or used.
# (__init__) Constructor initializes an object when it is created. It runs automatically when you create an object.
# self refers to the particular object being worked on.
# Class attributes belong to the class itself, and are shared by all objects. Instance attributes belong to each object, and are separate for each other.



from matatu import InvalidFareError

# PART 1: CLASS DEFINITIONS (blueprints only; nothing runs yet)


class Route:
    currency = "Ksh"                      # class attribute: shared by ALL routes

    def __init__(self, route_no, name, fare):     # constructor
        self.route_no = route_no          # instance attributes: separate per object
        self.name = name
        self.fare = fare                  # goes through the fare setter below
        self._stages = []                 # leading underscore = "internal use, hands off"

    # --- property: controlled access to fare(attribute) ---
    # The getter: @property - A getter controls how an attribute is read
    # The setter: @attribute.setter - A setter controls what happens when someone assigns a value to the property. It can validate the value before setting it, and raise an exception if the value is invalid.


    @property
    def fare(self):
        return self._fare

    @fare.setter
    def fare(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise InvalidFareError(value)
        self._fare = value

    # --- ordinary methods --- #  A method is simply a function defined inside a class.
    def add_stage(self, stage):
        self._stages.append(stage)

    def stage_count(self):
        return len(self._stages)

    # Special methods: __str__() and __repr__(). Commoly called dunder methods because their names begin and end with double underscores. They are used to define how an object behaves in certain situations, such as when printed.
    # --- how the object prints ---
    def __str__(self):                    # Human-readable representation: print(route) 
        return f"Route {self.route_no}: {self.name} ({self.currency} {self.fare})"

    def __repr__(self):                   # for developers: shows how to rebuild it
        return f"Route({self.route_no!r}, {self.name!r}, {self.fare!r})"

    # Class methods: A class method receives cls, which refers to the class itself. cls rep the class on which the class method is called.
    # --- alternative constructor and utility ---
    @classmethod
    def from_dict(cls, data):
        return cls(data["route_no"], data["name"], data["fare"])

    # Static method is a function placed inside a class because it is logically related to that class, but it doesn't need access to a particular object, or the class itself.
    @staticmethod
    def is_valid_route_no(route_no):
        return route_no.isdigit() and len(route_no) <= 3


class Matatu:
    def __init__(self, plate, capacity=14):
        self.plate = plate
        self.capacity = capacity
        self.__passengers = 0             # private-ish (name-mangled) Name mangling: It changes the internal attribute name from __passengers to something like _Matatu__passengers. This helps preventing accidental access or overriding of the attribute.
    def board(self, count=1):
        if self.__passengers + count > self.capacity:
            print(f"Cannot board {count}: only {self.capacity - self.__passengers} seats left")
            return False
        self.__passengers += count
        return True

    @property
    def passengers(self):                 # read-only: getter, no setter
        return self.__passengers

    @property
    def is_full(self):
        return self.__passengers >= self.capacity



# PART 2: THE DEMO
# When Python initializes rongai and kikuyu: self refers to the rongai object, then to the kikuyu object. Hence self.route_no becomes "58" for rongai and "111" for kikuyu... Each obejct has its own data, but they share the class attribute currency.

# isinstance() checks whether an object is an instance of a particular class or one if its subclasses.

def main():
    #  Creating Objects:
    rongai = Route("58", "CBD - Rongai", 100)
    kikuyu = Route("111", "CBD - Kikuyu", 80)

    # Testing the objects:
    print(rongai)                     # Route 58: CBD - Rongai (Ksh 100)
    print(kikuyu.name)                # CBD - Kikuyu
    print(repr(rongai))               # Route('58', 'CBD - Rongai', 100)
    print(isinstance(rongai, Route))  # True

    # ---- Each object has its own data ----
    rongai.add_stage("CBD")
    rongai.add_stage("Bomas")
    print(rongai.stage_count())       # 2
    print(kikuyu.stage_count())       # 0

    # ---- Class attribute is shared ----
    print(Route.currency)             # Ksh
    print(rongai.currency)            # Ksh

    # ---- classmethod and staticmethod ----
    data = {"route_no": "24", "name": "CBD - Kawangware", "fare": 50}
    kawangware = Route.from_dict(data)
    print(kawangware)                 # Route 24: CBD - Kawangware (Ksh 50)
    print(Route.is_valid_route_no("58"))    # True
    print(Route.is_valid_route_no("58B"))   # False

    # ---- Property with validation ----
    rongai.fare = 120
    print(rongai.fare)                # 120

    try:
        rongai.fare = -5
    except InvalidFareError as e:
        print(e)                      # Invalid fare: -5. Fare must be a positive number.
    print(rongai.fare)                # 120 (unchanged)

    try:
        Route("99", "Test", 0)
    except InvalidFareError as e:
        print(f"Could not create route: {e}")
        # Could not create route: Invalid fare: 0. Fare must be a positive number.

    # ---- Encapsulation with Matatu ----
    van = Matatu("KDA 123X", capacity=14)
    van.board(10)
    print(van.passengers)             # 10
    van.board(6)                      # Cannot board 6: only 4 seats left
    print(van.is_full)                # False
    van.board(4)
    print(van.is_full)                # True

    # van.passengers = 99             # AttributeError: property has no setter
    # print(van.__passengers)         # AttributeError: name is mangled
    print(van._Matatu__passengers)    # 14 (reachable, but only by deliberately going around)


# Entry point of the script
if __name__ == "__main__":
    main()