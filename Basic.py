"""# Description: This file contains the basic python code for the beginners.
FirstMonth = 23
SecondMonth = 32
ThirdMonth = 64
# Calculating the mean of the three months
mean = (FirstMonth+SecondMonth+ThirdMonth ) /3
print(mean)

"""
"""#Task 1: Write a Python program to take the input of two numbers and print the sum of the two numbers.

Name = input("Enter your name: ")
#print("Hello", Name)
print("Welcome to the Python World,"+  Name  ,"!")"""


"""TilesNeed = 9*7 + 5*7
print("Total Tiles Need: ", TilesNeed)
# Fill this in with an expression that calculates how many tiles will be left over.
TilesBuy = 17*6
leftOver = TilesBuy - TilesNeed
print("Numeber of tiles left over: ", leftOver)"""

"""# The current volume of a water reservoir (in cubic metres)
reservoir_volume = 4.445e8
# The amount of rainfall from a storm (in cubic metres)
rainfall = 5e6
AmountOfRainfall = int(rainfall)
#print("Amount of Rainfall: ", AmountOfRainfall)
# decrease the rainfall variable by 10% to account for runoff
rainfallDecrease = AmountOfRainfall - (AmountOfRainfall * 0.1)
print("Rainfall Decrease: ", rainfallDecrease)
# add the rainfall variable to the reservoir_volume variable
reservoir_volume = reservoir_volume + rainfallDecrease
print("Reservoir Volume: ", reservoir_volume)

# increase reservoir_volume by 5% to account for stormwater that flows  
reservoir_volumeIncrease = reservoir_volume + (reservoir_volume * 0.05)
print("Reservoir Volume Increase: ", reservoir_volumeIncrease)
# into the reservoir in the days following the storm
 
# decrease reservoir_volume by 5% to account for evaporation
reservoir_volumeDecrease = reservoir_volumeIncrease - (reservoir_volumeIncrease * 0.05)
print("Reservoir Volume Decrease: ", reservoir_volumeDecrease)
# subtract 2.5e5 cubic metres from reservoir_volume to account for water
NewAmount = reservoir_volume - int(2.5e5) 
print("New Amount: ", NewAmount)
# that's piped to arid regions.

# print the new value of the reservoir_volume variable"""


# 1. Assign the value 4.445e8 to a variable named reservoir_volume
reservoir_volume = 4.445e8  
print("Initial Reservoir Volume:", reservoir_volume)

# 2. Assign the value 5e6 to a variable named rainfall
rainfall = 5e6  
print("Initial Rainfall:", rainfall)

# 3. Decrease the rainfall variable by 10% to account for runoff
rainfall *= 0.9  # Keep 90% of the original rainfall
print("Rainfall After Runoff:", rainfall)

# 4. Add the adjusted rainfall to the reservoir_volume
reservoir_volume += rainfall  
print("Reservoir Volume After Rain:", reservoir_volume)

# 5. Increase reservoir_volume by 5% to account for stormwater that flows into it
reservoir_volume *= 1.05  
print("Reservoir Volume After Stormwater Flow:", reservoir_volume)

# 6. Decrease reservoir_volume by 5% to account for evaporation
reservoir_volume *= 0.95  
print("Reservoir Volume After Evaporation:", reservoir_volume)

# 7. Subtract 2.5e5 cubic meters from reservoir_volume to account for water piped to arid regions
reservoir_volume -= 2.5e5  
print("Final Reservoir Volume After Water Usage:", reservoir_volume)
