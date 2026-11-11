# A decorator is a function that takes another function, adds extra behaviour to it, and returns the modified function. It is a way to modify or enhance functions without changing their code. Decorators are often used for logging, access control, memoization and more. They are built on the concept of closures, which allow a function to remember the environment in which it was created.


from functools import wraps


def log_call(func):
    @wraps(func)                      # keeps the original name/docs
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_call                              # same as: calculate_fare = log_call(calculate_fare)
def calculate_fare(distance_km, rate_per_km=10):
    return distance_km * rate_per_km

calculate_fare(8)
# Calling calculate_fare with (8,)
# calculate_fare returned 80

print(calculate_fare.__name__)         # calculate_fare   (would be "wrapper" without @wraps)

# A decorator that takes its own argument needs one extra layer
def surge(multiplier):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs) * multiplier
        return wrapper
    return decorator

@surge(1.5)                            # rainy-day pricing
def base_fare(distance_km):
    return distance_km * 10

print(base_fare(8))                    # 120.0