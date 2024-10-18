# Jin Pak
# 10/17/24
# P2HW2
# Calculate the average of all the grades from input

# Get info from user
mod1 = float(input("Enter grade for Module 1: "))
mod2 = float(input("Enter grade for Module 2: "))
mod3 = float(input("Enter grade for Module 3: "))
mod4 = float(input("Enter grade for Module 4: "))
mod5 = float(input("Enter grade for Module 5: "))
mod6 = float(input("Enter grade for Module 6: "))

# create a list with grades
grades = [mod1, mod2, mod3, mod4, mod5, mod6]

# calculate the average
average = sum(grades)/len(grades)

print()

# Results!
print("------------Results------------")

print(f"{'Lowest Grade: ':<20}{min(grades)}")
print(f"{'Highest Grade: ':<20}{max(grades)}")
print(f"{'Sum of Grades: ':<20}{sum(grades)}")
print(f"{'Average: ':<20}{average:.2f}")
print("-" * 31)
