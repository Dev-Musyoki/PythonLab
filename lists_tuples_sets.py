#1. Lists: Ordered, mutable collections
fares = [50, 80, 100, 120]
print(fares[0])          # 50
print(fares[-1])         # 120 (last item)
print(fares[1:3])        # [80, 100] (slice: start included, stop excluded)
fares.append(150)
fares.remove(80)  # removes the first matching value
fares.pop()       # removes and returns the last item
fares.sort()
len(fares), max(fares), min(fares), sum(fares)


#2. Tuples: Ordered, immutable collections
stage_location = (-1.2864, 36.8172)
lat, lng = stage_location     # unpacking

print(stage_location[0])

#3. Sets: Unordered, mutable collections of unique items
stages_a = {"CBD", "Westlands", "Kangemi"}
stages_b = {"CBD", "Kawangware"}
stages_a & stages_b   # {'CBD'}: shared stages
stages_a | stages_b   # all stages, no duplicates


# Rule of thumb: list for an ordered collection that changes, tuple for a fixed record, set for uniqueness and fast “is it in here?” checks, dict for lookups by key.