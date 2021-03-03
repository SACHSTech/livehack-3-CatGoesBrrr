'''
-------------------------------------------------------------------------------
Name:		main.py

Purpose:	allows user to enter the distance driven for each day until the total distance driven surpasses 100km

Author:	Tan.C

Created:	03/03/2021
------------------------------------------------------------------------------
'''
print("***** Welcome to the DoorDash Distance Tracker ******")
print("")

# variable start values
total = 0
days = 0
distance = 0

# get distances from user
print("** Travel Log **")
while total <= 100:
  distance = int(input("Enter the distance travelled for the day: "))
  total = total + distance
  days += 1

# output number of days and average distance
print("")
print("** Summary **")
average = total/days
print("It took " + str(days) + " days to surpass 100km driven.")
print("The average distance driven per day is " + str(average) + " km")