# range(): loop a set number of times (stop is excluded)
for i in range(3):            # 0, 1, 2
    print(i)
for i in range(1, 10, 3):     # start, stop, step -> 1, 4, 7
    print(i)

# enumerate(): index + item together (replaces manual counters)
stages = ["CBD", "Westlands", "Kangemi"]
for position, stage in enumerate(stages, start=1):
    print(position, stage)    # 1 CBD, 2 Westlands, 3 Kangemi

# while: repeat until a condition turns False
seats_left = 3
while seats_left > 0:
    print("Boarding...")
    seats_left -= 1

# break: exit the loop now. continue: skip to the next iteration
for fare in [50, 0, 80, 120]:
    if fare == 0:
        continue              # skip bad data
    if fare > 100:
        break                 # stop at the first fare over 100
    print(fare)               #  50, 80

# Use for when you know what you’re looping over, and while when you’re waiting for a condition (like valid user input). Watch for infinite while loops: if nothing inside changes the condition, it never ends.