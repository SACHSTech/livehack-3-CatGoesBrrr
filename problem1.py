'''
-------------------------------------------------------------------------------
Name:		main.py

Purpose:	determines which group a player is placed in

Author:	Tan.C

Created:	03/03/2021
------------------------------------------------------------------------------
'''
print("****** Tournament Tracker ******")
print("")

# variable start value
w_count = 0

# get number of wins and losses from user
print("Enter the wins and losses for your team: ")
for i in range(6):
  user_results = input("")
  if user_results == "w" or "W":
    w_count = w_count + 1

# output results
if w_count == 5 or 6:
  print("Your team is in Group 1")

elif w_count == 3 or 4:
  print("Your team is in Group 2")

elif w_count == 1 or 2:
  print("Your team is in Group 3")

else:
  print("Your team is eliminated from the tournament")