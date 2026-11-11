# Advanced OOP: Enums, Dataclasses, Mixins, Dunder methods, Context managers

import json
from contextlib import contextmanager
from dataclasses import FrozenInstanceError, asdict, dataclass, field, replace
from enum import Enum, IntEnum

# 1. ENUMS: a fixed set of named choices


class VehicleType(Enum):
    MATATU = "matatu"
    BUS = "bus"
    TUK_TUK = "tuk-tuk"


class SafetyRating(IntEnum):              # IntEnum: members behave like ints, so they compare
    POOR = 1
    FAIR = 2
    GOOD = 3
    EXCELLENT = 4

# Design consideration: Use ordinary Enum when you want distinct named choices, and IntEnum when integer compatibility or numeric ordering is genuinely useful.

# 2. DATACLASSES: classes that mainly hold data


@dataclass(frozen=True)                   # frozen = immutable, which also makes it hashable
class Stage:
    name: str
    lat: float
    lng: float


@dataclass
class Route:
    route_no: str
    name: str
    fare: int
    vehicle_type: VehicleType = VehicleType.MATATU
    stages: list[Stage] = field(default_factory=list, repr=False)   # safe mutable default

    def __post_init__(self):              # runs right after the generated __init__
        if self.fare <= 0:
            raise ValueError(f"Invalid fare: {self.fare}")

    def add_stage(self, stage):
        self.stages.append(stage)



# 3. MIXINS: small reusable behaviours, combined by multiple inheritance
# Mixin: A small class designed to add a particular behaviour to another class.
# Serialization: converting an object into a representation that can be stored, transferred or processed anywhere.

class SerializableMixin:
    def to_dict(self):
        return asdict(self) # asdict(): Converts a dataclass instance into a dictionary.

    def to_json(self):
        def convert(obj):                 # teach json how to write Enums
            return obj.value if isinstance(obj, Enum) else str(obj)
        return json.dumps(self.to_dict(), indent=2, default=convert)


class AuditMixin: # Records changes made to an object(Audit logging)
    def log_change(self, message):
        if not hasattr(self, "_history"):
            self._history = []
        self._history.append(message)

    @property
    def history(self):
        return list(getattr(self, "_history", []))


@dataclass
class PublishedRoute(SerializableMixin, AuditMixin, Route):
    rating: SafetyRating = SafetyRating.FAIR

    def update_fare(self, new_fare):
        if new_fare <= 0:
            raise ValueError(f"Invalid fare: {new_fare}")
        self.log_change(f"fare {self.fare} -> {new_fare}")
        self.fare = new_fare


# ---- the MRO and cooperative super() ----

class Notifier:
    def send(self, msg):
        print(f"  [base] {msg}")


class SmsNotifier(Notifier):
    def send(self, msg):
        print(f"  [SMS] {msg}")
        super().send(msg)                 # hands over to the NEXT class in the MRO


class EmailNotifier(Notifier):
    def send(self, msg):
        print(f"  [Email] {msg}")
        super().send(msg)


class AlertService(SmsNotifier, EmailNotifier):
    pass



# 4. DUNDER METHODS: make our own class behave like a built-in container
# Dunder: short for double undersocres
class RouteCollection:
    def __init__(self, routes=()):
        self._routes = list(routes)

    def add(self, route):
        if route.route_no in self:
            raise ValueError(f"Route {route.route_no} already exists")
        self._routes.append(route)

    def __len__(self):                    # len(collection)
        return len(self._routes)

    def __iter__(self):                   # for route in collection
        yield from self._routes

    def __contains__(self, item):         # "58" in collection / route in collection
        if isinstance(item, str):
            return any(r.route_no == item for r in self._routes)
        return item in self._routes

    def __getitem__(self, key):           # collection[0], collection[1:3], collection["58"]
        if isinstance(key, str):
            for r in self._routes:
                if r.route_no == key:
                    return r
            raise KeyError(key)
        if isinstance(key, slice):
            return RouteCollection(self._routes[key])
        return self._routes[key]

    def __add__(self, other):             # collection + collection
        return RouteCollection(self._routes + other._routes)

    def __repr__(self):
        return f"RouteCollection({[r.route_no for r in self._routes]})"


# 5. CONTEXT MANAGERS: guaranteed setup and cleanup around a block


class RouteEditor:
    """Edits a collection; undoes everything if an error happens inside the block."""

    def __init__(self, collection):
        self.collection = collection

    def __enter__(self):                  # runs on entering the `with` block
        self._backup = list(self.collection._routes)
        print("  editor opened")
        return self.collection            # this is what `as` receives

    def __exit__(self, exc_type, exc_value, traceback):   # runs on leaving, always
        if exc_type is not None:
            self.collection._routes = self._backup
            print(f"  error ({exc_value}): changes rolled back")
        else:
            print("  changes kept")
        return False                      # False = don't swallow the exception


@contextmanager                           # the shortcut: a generator instead of a class
def trip_session(name):
    print(f"  trip '{name}' started")
    try:
        yield
    finally:
        print(f"  trip '{name}' ended")



# THE DEMO

def main():
    print("--- Enums ---")
    print(VehicleType.MATATU)
    print(VehicleType.MATATU.name, "|", VehicleType.MATATU.value)
    print(VehicleType("bus"))
    print([v.name for v in VehicleType])
    print(SafetyRating.GOOD > SafetyRating.FAIR)
    try:
        VehicleType("train")
    except ValueError as e:
        print("ValueError:", e)

    print("--- Dataclass basics ---")
    cbd = Stage("CBD", -1.2864, 36.8172)
    bomas = Stage("Bomas", -1.3573, 36.7803)
    print(cbd)
    print(cbd == Stage("CBD", -1.2864, 36.8172))
    try:
        cbd.name = "Town"
    except FrozenInstanceError:
        print("FrozenInstanceError: Stage is immutable")
    print(len({cbd, Stage("CBD", -1.2864, 36.8172), bomas}))

    rongai = Route("58", "CBD - Rongai", 100)
    print(rongai)
    print(rongai == Route("58", "CBD - Rongai", 100))
    rongai.add_stage(cbd)
    rongai.add_stage(bomas)
    print(len(rongai.stages))
    print(len(Route("111", "CBD - Kikuyu", 80).stages))
    higher = replace(rongai, fare=120)
    print(rongai.fare, higher.fare)
    try:
        Route("99", "Test", 0)
    except ValueError as e:
        print("ValueError:", e)

    print("--- Mixins ---")
    pub = PublishedRoute("58", "CBD - Rongai", 100, rating=SafetyRating.GOOD)
    pub.add_stage(cbd)
    pub.update_fare(120)
    pub.update_fare(130)
    print(pub.history)
    print(pub.to_json())
    print([c.__name__ for c in PublishedRoute.__mro__])

    print("--- MRO and super() ---")
    print([c.__name__ for c in AlertService.__mro__])
    AlertService().send("Route 58 delayed")

    print("--- Container dunder methods ---")
    routes = RouteCollection([
        Route("58", "CBD - Rongai", 100),
        Route("111", "CBD - Kikuyu", 80),
    ])
    routes.add(Route("24", "CBD - Kawangware", 50))
    print(len(routes))
    print(routes)
    print([r.name for r in routes])
    print("24" in routes, "46" in routes)
    print(routes[0].name)
    print(routes["111"].fare)
    print(routes[1:])
    print(routes + RouteCollection([Route("46", "CBD - Ngong", 60)]))
    print(bool(routes), bool(RouteCollection()))
    try:
        routes.add(Route("58", "Duplicate", 90))
    except ValueError as e:
        print("ValueError:", e)

    print("--- Context managers ---")
    with RouteEditor(routes) as editable:
        editable.add(Route("46", "CBD - Ngong", 60))
    print(len(routes))

    try:
        with RouteEditor(routes) as editable:
            editable.add(Route("33", "CBD - Thika", 120))
            editable.add(Route("58", "Duplicate", 90))
    except ValueError as e:
        print("  caught outside:", e)
    print(len(routes), "33" in routes)

    with trip_session("58 to Rongai"):
        print("  boarding passengers")


if __name__ == "__main__":
    main()