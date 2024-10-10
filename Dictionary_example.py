# In-class example for dictionary

# Create a dictionary

rose = {"color":"red", "price":1, "height":3.5, "is_perennial":False}

# Get a value, given the key

print(f"${rose['price']:.2f}")

# Get anohter value, get another key

print(f"Is the the rose a pernnial? {rose['is_perennial']}")

print(rose['color'])

# add a key value pair
rose["water need"] = "Place in vase half filled"

# print the entire dictionary
print(rose)

# add a key value pair
rose.update({"leaf color":"green", "sun_needed":5})
print("\n\n")
print(rose)

# delete item from dictionary
del rose['height']

# print the entire dictionary
print(rose)
print()

# print all keys in the dictionary
print(rose.keys())

# ask the user to give a key in the dictionary

answer = input("Enter a key from the dictionary: ")

# Give the value associated with the users answer
print(f"The value for {answer} is {rose[answer]}")












