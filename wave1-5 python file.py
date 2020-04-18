Exercise 24
d = int(input("Enter number of days: "));
h = int(input("Enter number of hours: "));
m = int(input("Enter number of minutes: "));
s = int(input("Enter number of seconds: "));
#converting day into hours, hours into minutes
#and then minutes into seconds
res = ((d*24 + h)*60 + m)*60 +s;
print("Total number of seconds:", res)

Exercise 25
##
# covert a number of seconds to days, hours and seconds
#
seconds_per_day = 86400
seconds_per_day = 3600
seconds_per_day =60

# Read input from the user
seconds =int(input("Enter a number of seconds: "))
# Compute the datys, hours, minutes and seconds
days = seconds / seconds_per_day
seconds = seconds % seconds_per_day

hours = seconds / seconds_per_hour
seconds = seconds % seconds_per_hour

minutes = seconds / seconds_per_minute
seconds + seconds % seconds_per_minute

#Display the result with the desired formatting
print("The equivalent duration is", \ "%d:%02d:%02d." % (days, hours, minutes, seconds)




Exercise 26 
#Importing time module 
import time

#using localtime() to convert time in seconds
Time = time.localtime()

#printing current time 
print(time.asctime(Time))
