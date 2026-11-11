# Loops:
#1. for loops:
#routes = ["58", "111", "24", "46"]
#for route in routes:
#  print(route)

fares  =  [50, 70, 100, 150]
for fare in fares:
  if fare > 60:
     print(fare)

# building a new list while looping, using .append().
expensive_fares = []

for fare in fares:
    if fare > 60:
        expensive_fares.append(fare)

print(expensive_fares)

# Example
routes = [
    {"route_no": "58", "name": "CBD - Rongai", "fare": 100},
    {"route_no": "111", "name": "CBD - Kikuyu", "fare": 80},
    {"route_no": "24", "name": "CBD - Kawangware", "fare": 50},
]
expensive_routes = []

for route in routes:
    if route["fare"] > 60:
        expensive_routes.append(route["route_no"])

print(expensive_routes)

# Comprehension version
expensive_routes = [route["route_no"] for route in routes if route["fare"] > 70]
print(expensive_routes)

affordable_names = [route["name"] for route in routes if route["fare"] <= 80]
print(affordable_names)

all_fares = [route["fare"] for route in routes]
print(all_fares)


#Dictionary comprehension
# Loop version
fare_lookup = {}
for route in routes:
    fare_lookup[route["route_no"]] = route["fare"]

# Comprehension version
fare_lookup = {route["route_no"]: route["fare"] for route in routes}

print(fare_lookup)   # {'58': 100, '111': 80, '24': 50}

route_names = {route["route_no"]: route["name"] for route in routes}
print(route_names)   # {'58': 'CBD - Rongai', '111': 'CBD - Kikuyu', '24': 'CBD - Kawangware'}

fare_lookup = {route["route_no"] : route["fare"] for route in routes if route["fare"] >=80}
print(fare_lookup["58"])

# KeyError handling:
fare_lookup = {"58": 100, "111": 80}

# 1. Check first with `in`
if "24" in fare_lookup:
    print(fare_lookup["24"])
else:
    print("Route not found")

# 2. Use .get(), which returns a default instead of crashing
print(fare_lookup.get("24"))             # None
print(fare_lookup.get("24", "Not found"))  # Not found
print(fare_lookup.get("58", "Not found"))  # 100

#Example
route_numbers = ["58", "111", "24", "46"]

for route_no in route_numbers:
    if route_no in fare_lookup: # checks if route_no is a key in fare_lookup
        print(f"{route_no}: {fare_lookup[route_no]}")
    else:
        print(f"{route_no}: no fare data")

for route_no in route_numbers:
    fare = fare_lookup.get(route_no) # returns None if route_no is not in fare_lookup

    if fare is not None:
        print(f"{route_no}: {fare}")
    else:
        print(f"{route_no}: no fare data")

# Looping over key and values together: .items()
fare_lookup = {"58": 100, "111": 80}

for route_no, fare in fare_lookup.items():
    print(f"Route {route_no} costs Ksh {fare}")

fare_lookup = {"58": 100, "111": 80, "24": 50}

# 1. Every route and fare
for route_no, fare in fare_lookup.items():
    print(f"Route {route_no}: Ksh {fare}")

# 2. Average fare: 230 / 3
average_fare = sum(fare_lookup.values()) / len(fare_lookup)
print(average_fare)   # 76.66666666666667

# 3. 10% discount
discounted = {route_no: fare * 0.9 for route_no, fare in fare_lookup.items()}
print(discounted)     # {'58': 90.0, '111': 72.0, '24': 45.0}