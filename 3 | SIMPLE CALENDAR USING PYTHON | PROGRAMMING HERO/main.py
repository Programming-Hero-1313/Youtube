# importing the calendar module
import calendar

#taking input of year from the user
y = int(input("ENTER THE YEAR : "))

#taking input of month from the user
m = int(input("ENTER THE MONTH : "))

# making calendar in the 'cal' variable
cal = calendar.month(y, m)

# print the cal (calendar is stored in the cal variable)
print(cal)
