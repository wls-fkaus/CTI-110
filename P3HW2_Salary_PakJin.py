# Jin Pak
# 10/29/24
# P3HW2
# Show the user how much they get payed per hour

# Get info from user
name = input("Enter employee's name: ")
hours = int(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

print("-" * 30)

# calculations
if hours > 40:
    ot = hours - 40
    ot_hours = 1.5 * pay_rate
    ot_pay = ot * ot_hours
    reg_pay = 40 * pay_rate
    gross = ot_pay + reg_pay
else:
    ot = 0
    ot_hours = 0
    ot_pay = 0
    reg_pay = hours * pay_rate
    gross = reg_pay



# Display all the info back to the user
print(f"Employee name: {name}")

print()

print(f"{'Hours worked':<20}{'Pay rate':<20}{'OverTime':<20}{'OverTime Pay':<20}{'RegHour Pay':<20}{'Gross Pay':<20}")
print("-" * 110)
print(f"{hours:<20.1f}${pay_rate:<19.1f}{ot:<20.1f}${ot_pay:<19.2f}${reg_pay:<19.2f}${gross:<19.2f}")

