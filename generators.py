# A generator is a special kind of iterator that produces a value only when requested. It is defined like a normal function but uses the yield statement to return values one at a time, pausing its state between each yield. This allows for efficient memory usage, especially when dealing with large datasets or streams of data.

# return vs yield: return sends a value back to the caller and terminates the function, while yield sends a value back but pauses the function, allowing it to resume later from where it left off.


# A generator gives you the same result as that whole class with a single function. Use yield instead of return, and Python handles the position-tracking for you. Values are produced lazily, one at a time, only when asked for.(Lazy evaluation)


def stage_stream(stages):
    for stage in stages:
        print(f"  (generating {stage})")
        yield stage

gen = stage_stream(["CBD", "Westlands", "Kangemi"])
print("Generator created, nothing has run yet")
print(next(gen))
print(next(gen))
# Generator created, nothing has run yet
#   (generating CBD)
# CBD
#   (generating Westlands)
# Westlands

# Practical: filter a stream of fares without building a second list
def fares_over(fares, limit):
    for fare in fares:
        if fare > limit:
            yield fare

print(list(fares_over([50, 120, 80, 150], 100)))   # [120, 150]

# Generator expression: a comprehension with () instead of []
fares = [50, 80, 100, 120]
print(sum(fare for fare in fares if fare > 60))    # 300

# Generators are one-shot: once consumed, they're empty
g = fares_over([50, 120, 80, 150], 100)
print(list(g))   # [120, 150]
print(list(g))   # []