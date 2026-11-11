# Variables and Printing:
route_name = "CBD - Rongai"
route_number = "58"
fare = 100

print(F"Route Name: {route_name} Route Number: {route_number}, Fare: {fare}")

# Taking input from user:
fare = int(input("Enter your fare: ")) #input() always returns a string no matter what the user types.
print(F"Fare: {fare + 60}")


# Basic Math Operators and Comparisons:
fare = 200
discount = 50
final_fare = fare - discount
print(F"Final fare: {final_fare}")
print(final_fare > 100) 

fare_a = 100
fare_b = 50

print(fare_a > fare_b)
print(fare_a - fare_b)
