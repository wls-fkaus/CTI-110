# Jin Pak
# 11/7/2024
# P4LAB2
# Use loops to show only positive time tables

runagain = "yes"
while runagain.lower() != "no":
    
    # ask for number from user
    num = int(input("Enter an integer: "))
    if num >= 0:
        # display multiplication for the number
        for item in range(1, 13):
            print(f"{num} * {item} = {num * item}")
    else:
        print("This program does not handle negative values")

    runagain = input("Would you like to run this program again? Yes or no: ")

# if user says 'no'

print("Program is ending...")
