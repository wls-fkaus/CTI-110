# Jin Pak
# 10/24/24
# P3HW1
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
avg = sum(grades)/len(grades)

print()

# Results!
print("------------Results------------")

print(f"{'Lowest Grade: ':<20}{min(grades)}")
print(f"{'Highest Grade: ':<20}{max(grades)}")
print(f"{'Sum of Grades: ':<20}{sum(grades)}")
print(f"{'Average: ':<20}{avg:.2f}")
print("-" * 31)

# Determine the letter grade from the avg
if avg >= 90:
    let_grade = "A"
elif avg >= 80:
    let_grade = "B"
elif avg >=70:
    let_grade = "C"
elif avg >= 60:
    let_grade = "D"
elif avg <= 59:
    let_grade = "F"

# Display the letter grade
print(f"Your grade is: {let_grade}")
