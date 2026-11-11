# A module is a file containing Python definitions and statements. It allows you to organize your code logically, making it easier to understand. They also enable code reuse.
# Its simply a python file within a package.

#User-defined exceptions
#Try/except/else is the handling side: catching errors that something else raised. User-defined exceptions are the raising side: you invent a new kind of error so the failure has a meaningful name.


class MatatuError(Exception):
    """Base class for every error in our app."""

class InvalidFareError(MatatuError):
    def __init__(self, fare):
        self.fare = fare
        super().__init__(f"Invalid fare: {fare}. Fare must be a positive number.")

class RouteNotFoundError(MatatuError):
    def __init__(self, route_no):
        self.route_no = route_no
        super().__init__(f"Route {route_no} not found")