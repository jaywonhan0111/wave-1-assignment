# Get number of cents required from an user.
changes = int(input("number of cents required for the change: "))

#starting form 2 dollars
num_toonies = changes//200
print("number of toonies: ", num_toonies)

changes = changes % 200 
num_loonies = changes//100
print("number of loonies: ", num_loonies)

changes = changes % 100 
num_quarters = changes//25
print("number of quarters: ", num_quarters)

changes = changes % 25
num_dimes = changes//10
print("number of dimes: ", num_dimes)

changes = changes % 10 
num_nickels = changes//5
print("number of nickels: ", num_nickels)

changes = changes % 5
print("number of pennies: ", changes)









