# A function that calls itself. It needs a base case (Condition under which the function stops calling itself ) and a recursive case (Where the function calls itself with modified arguments).

def countdown(n):
    if n == 0:                  # base case
        print("Departing!")
        return
    print(n)
    countdown(n - 1)            # recursive case

countdown(3)                    # 3
                                # 2
                                # 1
                                # Departing!

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))             # 120

def sum_nested(items):          # where recursion shines: nested data
    total = 0
    for item in items:
        if isinstance(item, list):
            total += sum_nested(item)
        else:
            total += item
    return total

print(sum_nested([50, [80, 100], [[20], 30]]))   # 280