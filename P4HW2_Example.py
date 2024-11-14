# example similar to P4HW2 using loops

# while loop to control the program

# make a variable to control the loop

product = input("Enter product name or 'exit' to terminate: ")

# accumulator
numitems = 0
totalcost = 0

# while loop
while product.lower() != "exit":
    # increment numitems by 1
    numitems += 1
    cost = float(input(f"Enter the cost for {product}: "))
    totalcost += cost
    print()
    product = input("Enter product name or 'exit' to terminate: ")
print(f"The total number of items purchased is {numitems}")
print(f"The total cost of the items is ${totalcost:.2f}")
