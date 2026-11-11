# if / elif / else:
fare = 120
if fare > 100:
  print("Expensive route!")
elif fare > 50:
  print("Moderate route!")
else:
  print("Cheap fare!")


matatu_fare = int(input("Enter the matatu fare: "))
if matatu_fare > 100:
  print("Peak fare!")
elif  50 <= matatu_fare <= 100: # Read as: "50 is less than or equal to matatu_fare, which is less than or equal to 100"
  print("Standard fare!")
else:
  print("Low fare!")
