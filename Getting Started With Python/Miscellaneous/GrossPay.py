#Prompt a User for hours and rate per hour, calculate the gross pay based on inputs
hours=float(input("Enter Hours: "))
rate=float(input("Enter rate per hour: "))

Pay=hours*rate
print("Pay:", Pay)