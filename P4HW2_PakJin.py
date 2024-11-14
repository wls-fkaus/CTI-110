# Jin Pak
# 11/14/24
# P4HW2
# Show the user how much they get payed per hour

# accumulator
numemployees = 0
total_ot = 0
total_reg_hours = 0
total_gross = 0

# Get info from user
name = input("Enter employee's name or 'exit' to terminate: ")

# start loop
while name.lower() != "exit":

    numemployees += 1
    
    hours = int(input(f"Enter number of hours {name} worked: "))
    pay_rate = float(input(f"Enter {name}'s pay rate: "))

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

    total_ot += ot_pay
    total_reg_hours += reg_pay
    total_gross += gross

# Display all the info back to the user
    print(f"Employee name: {name}")

    print()

    print(f"{'Hours worked':<20}{'Pay rate':<20}{'OverTime':<20}{'OverTime Pay':<20}{'RegHour Pay':<20}{'Gross Pay':<20}")
    print("-" * 110)
    print(f"{hours:<20.1f}${pay_rate:<19.1f}{ot:<20.1f}${ot_pay:<19.2f}${reg_pay:<19.2f}${gross:<19.2f}")

    print()
    print()
    name = input("Enter employee's name or 'exit' to terminate: ")
# Loop breaks
print()
print(f"Total number of employees entered: {numemployees}")
print(f"Total amount paid for overtime: ${total_ot:.2f}")
print(f"Total amount paid for regular hours: ${total_reg_hours:.2f}")
print(f"Total amount paid in gross: ${total_gross:.2f}")


