# value returning functions

import random

# habitat
def getHabitat(animal):
    if animal in ["turtle", "fish", "anenome", "pufferfish", "shark", "whale", "dolphin", "seahorse", "jellyfish"]:
        return "Ocean"
    if animal in ["camal", "scorpian", "spider", "iguana", "kangaroo", "fox", "snake"]:
        return "Desert"
    if animal in ["bear", "lemur", "lion", "monkey", "tiger", "parrot", "panda", "panther"]:
        return "Jungle"
    

def getAnimal(habitat,numanimal):
    friends = []
    
    if habitat == "Ocean":
        oceanlist =["turtle", "fish", "anenome", "pufferfish", "shark", "whale", "dolphin", "seahorse", "jellyfish"]
        # Loop runs numanimal times
        for i in range(numanimal):
            # Adding a random oceanlist item to the friends list
            friends.append(random.choice(oceanlist))
        return friends
    
    if habitat == "Desert":
        desertlist =["camal", "scorpian", "spider", "iguana", "kangaroo", "fox", "snake"]
        # Loop runs numanimal times
        for i in range(numanimals):
            # Adding a random oceanlist item to the friends list
            friends.append(random.choice(desertlist))
        return friends

    if habitat == "Jungle":
        junglelist =["bear", "lemur", "lion", "monkey", "tiger", "parrot", "panda", "panther"]
        # Loop runs numanimal times
        for i in range(numanimals):
            # Adding a random oceanlist item to the friends list
            friends.append(random.choice(junglelist))
        return friends


# main
def main():
    answer = "yes"
    while answer.lower() == "yes":
        print("✨🐠🦑🌊✨")
        animal = input("Enter your favorite animal: ")
        print()
        habitat = getHabitat(animal.lower())
        print(f"This {animal} lives in this {habitat} habitat.")
        print()
        numanimal = int(input(f"How many friends for the {animal}: "))

        friendslist = getAnimal(habitat,numanimal)

        print(f"The {animal} has the following friends: ")
        # loop to display all items in the friendslist
        for i in friendslist:
            print(i)
        
        answer = input("Do you want to run this program again? Yes or no: ")

if __name__=="__main__":
    main()

print("Program has ended...")
