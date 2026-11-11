# A one-line anonymous function. Use it for short throwaway logic, usually as an argument to another function.

discount = lambda fare: fare - 10
print(discount(100))            # 90

routes = [
    {"route_no": "58",  "fare": 100},
    {"route_no": "111", "fare": 80},
    {"route_no": "24",  "fare": 50},
]

cheapest_first = sorted(routes, key=lambda r: r["fare"])   # sort by fare
print([r["route_no"] for r in cheapest_first])             # ['24', '111', '58']

pricey = list(filter(lambda r: r["fare"] > 60, routes))    # keep matching items
print([r["route_no"] for r in pricey])                     # ['58', '111']

# If the logic needs more than one expression, use a normal def

