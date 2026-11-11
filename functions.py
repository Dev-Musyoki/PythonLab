def calculate_fare(base, distance_km, rate_per_km=10):   # rate_per_km(default_value) is optional
    return base + distance_km * rate_per_km

print(calculate_fare(50, 8))                  
print(calculate_fare(50, 8, 15)) # (default overridden)

# Keyword argument: is an argument passed using the parameter's name.
print(calculate_fare(distance_km=5, base=30))# 80   (keyword args, any order)

# Positional argument: An argument passed to a function based on its position (order).

def total_fare(*fares):   # *args: any number of positional args
    return sum(fares)

print(total_fare(50, 80, 100))                  # 230

def route_info(**details):                      # **kwargs: any number of keyword args
    for key, value in details.items():
        print(f"{key}: {value}")

route_info(route_no="58", name="CBD - Rongai")  # route_no: 58
                                                # name: CBD - Rongai

def fare_stats(fares):                          # return several values as a tuple
    return min(fares), max(fares), sum(fares) / len(fares)

low, high, avg = fare_stats([50, 80, 100])
print(low, high, avg)                           # 50 100 76.66666666666667
