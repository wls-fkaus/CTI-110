# Reveiw of functions
import random

def death_cal(name, age):
    avg_lifespan = 80
    year_left = avg_lifespan - age
    print(f"Using an average life span of {avg_lifespan}, {name} has {year_left} years life to live.")
    possible_death = ["Choked on grapefruit", "Attacked by rabid owl", "Sneezed too hard", "Fell down the stairs"]
    cause = random.choice (possible_death)
    return cause

def main():
    cause = death_cal(input("Enter your name: "), int(input("Enter your age: ")))

    print("⚰🕸🦴☠")
    print(f"Cause of death: {cause}")
    print()
    print("\n GAME OVER")

if __name__ == "__main__":
    main()
