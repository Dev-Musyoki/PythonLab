# Regular Expressions: A powerful tool for pattern matching and text manipulation in Python.


import re

# 1. Validate a Kenyan number plate like "KDA 123X"
plate_pattern = re.compile(r"K[A-Z]{2} \d{3}[A-Z]")

for plate in ["KDA 123X", "KBZ 456A", "kda 123x", "ABC 123X", "KDA 12X"]:
    print(plate, "->", bool(plate_pattern.fullmatch(plate)))
# KDA 123X -> True
# KBZ 456A -> True
# kda 123x -> False   (lowercase)
# ABC 123X -> False   (must start with K)
# KDA 12X  -> False   (needs 3 digits)

# 2. Validate a route number: 1-3 digits, optional letter ("58", "111", "23B")
route_pattern = re.compile(r"\d{1,3}[A-Z]?")
print(bool(route_pattern.fullmatch("23B")))    # True
print(bool(route_pattern.fullmatch("1234")))   # False

# 3. Extract data from a messy commuter report
report = "Route 58 fare now Ksh 120, Route 111 fare Ksh 90, Route 24 fare Ksh 50"
matches = re.findall(r"Route (\d+) fare (?:now )?Ksh (\d+)", report)
print(matches)   # [('58', '120'), ('111', '90'), ('24', '50')]

fare_updates = {route_no: int(fare) for route_no, fare in matches}   # comprehension again
print(fare_updates)   # {'58': 120, '111': 90, '24': 50}

# 4. Clean up messy whitespace

print(re.sub(r"\s+", " ", "CBD   -   Rongai"))   # CBD - Rongai



#Key Regular Expression Symbols:	    
#1.  \\d / \\w / \\s	- a digit / a word character / whitespace
#2.   [A-Z]	- any one character from the set
#3.  {3} / {1,3}	- exactly 3 / between 1 and 3
#4.  \\+ / \\* / \\?	- one or more / zero or more / optional
#5.  ( )	- capture group (what findall returns)
#6. (?: )	- group that isn’t captured


# Functions: fullmatch (the whole string must match), match (from the start), search (anywhere), findall (every match), sub (replace). Use raw strings (r"...") so backslashes survive.