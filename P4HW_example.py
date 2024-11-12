# Example similar to P4HW1
# Ask the user how many grades 
# Create a list 
avaliableitems = ["bows", "toy", "litter", "pot", "kitkat", "treat"] 
numitems = int(input("How many items do you want to purchase? "))

# empty list to hold all the values
cart = []

# loop to get the items
for items in range(numitems):
    thisitem = input(f"Enter item #{items + 1}: ")
    while thisitem not in avaliableitems:
        print(f"{thisitem} is not avaliable!")
        thisitem = input(f"Enter item #{items + 1} again: ")
    # add the valid item  to the cart
    cart.append(thisitem)


# loop to print each item in the cart
print()
print("Items we purchased")
for product in cart:
    print(product)