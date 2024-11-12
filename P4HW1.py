# Jin Pak
# 11/12/2024
# Collect all grades and show the lowest and average

# Ask user for amount of grades
numscores = int(input("How many scores do you want to enter? "))

# make a list for the valid scores
grades = []


for scores in range(numscores):
    thisscore = int(input(f"Enter score #{scores + 1}: "))
    while thisscore < 0 or thisscore > 100:
        print("INVALID Score entered!!!")
        print("Score should between 0 and 100")
        thisscore = int(input(f"Enter score #{scores + 1} again: "))
    # add the valid score to the list
    grades.append(thisscore)

print()


# Display the results
print("------------Results-----------")
print(f"{'Lowest Score  : ':<17}{min(grades):.1f}")
grades.remove(min(grades))
avg = sum(grades)/len(grades)
print(f"{'Modified List : '} {grades}")
print(f"{'Scores Average: ':<17}{avg:.2f}")
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
print(f"{'Grade         : ':<17}{let_grade}")
print("-" * 30)
