print("Welcome to the MPH to MPS Conversion App")

#Get user input
mph = float(input("\nWhat is your speed in miles per hour (MPH): "))

#Convert to mps
mps = mph*0.4474
mps = round(mps, 2)

print ("\nYour speed in meters per second (MPS) is " + str(mps) + "")

