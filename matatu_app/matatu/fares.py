from matatu.exceptions import (  # relative import (same package)
    InvalidFareError,
    RouteNotFoundError,
)


def validate_fare(fare):
    if not isinstance(fare, (int, float)) or fare <= 0:
        raise InvalidFareError(fare)        # raise = trigger an exception yourself
    return fare

def get_fare(routes, route_no):
    for route in routes:
        if route["route_no"] == route_no:
            return validate_fare(route["fare"])
    raise RouteNotFoundError(route_no)