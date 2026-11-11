# A package is simply a directory containing a special file called __init__.py. This file can be empty, but its presence indicates that the directory should be treated as a package. 
# Packages can have sub-packages, forming a hierarchy of modules. This allows for better organization of code, especially in larger projects.

from .exceptions import InvalidFareError, MatatuError, RouteNotFoundError
from .fares import get_fare, validate_fare
from .storage import load_routes, log_event, save_routes

__all__ = [
    "InvalidFareError",
    "MatatuError",
    "RouteNotFoundError",
    "get_fare",
    "load_routes",
    "log_event",
    "save_routes",
    "validate_fare",
]