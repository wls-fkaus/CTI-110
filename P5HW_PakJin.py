# Jin Pak
# 12/7/24
# P5HW
# Using functions to create a game
import random
import threading
import string

class TimerExpired(Exception):
    pass

def create_Character():
    name = input("Enter character's name: ")
    health = 100
    weapon = ["Miku Beam🎵"]
    strength = 100

    return {
        "Name": name,
        "Health": health,
        "Weapons": weapon,
        "Strength": strength
    }

def create_Villain():
    name = input("Enter villain's name: ")
    health = 100
    weapon = ["Tornado"]
    strength = random.randint(50, 100)

    return {
        "Name": name,
        "Health": health,
        "Weapons": weapon,
        "Strength": strength
    }

def show_stats(character):
    print()
    print(f"{character['Name']}'s Stats")
    print("🌌✨🌠🌌✨🌠🌌✨🌠🌌✨🌠🌌✨🌠")
    print(f"Health: {character['Health']}")
    print(f"Weapons: {character['Weapons']}")
    print(f"Strength: {character['Strength']}")
    print()

def input_with_timeout(prompt, timeout):
    user_input = []

    def get_input():
        user_input.append(input(prompt))

    input_thread = threading.Thread(target=get_input)
    input_thread.start()
    input_thread.join(timeout)

    if input_thread.is_alive():
        raise TimerExpired("Time's up!")
    return user_input[0] if user_input else ""

def game_sequence(villain):
    characters = string.ascii_uppercase + string.digits # random sequence
    sequence = ''.join(random.choices(characters, k=6))
    timeout = 10  # seconds

    print(f"Enter the correct sequence to receive 5 notes🎵 and deal 25 dmg to {villain['Name']}!")
    print(f"You have {timeout} seconds.")
    print(f"Sequence: {sequence}")

    try:
        user_response = input_with_timeout("Your input: ", timeout)
        if user_response == sequence:
            villain["Health"] -= 25 # take away health from villain
            print()
            print("🎵Correct! You earn 5 notes!")
            print(f"✅Villain's health: {villain['Health']}")
            print()
            return 5
        else:
            print()
            print("❌Incorrect sequence. Try again!")
            print()
    except TimerExpired:
        print()
        print("❌Time's up! You ran out of time!")
        print()

    return 0

def main():
    runagain = "yes"
    while runagain.lower() != "no": # To loop it again if wanted
        print("Game is starting...")
        print()
        print("Goal: Collect 20 music notes🎵🎵")
        print("Defeat the villain!")
        print()
        print("Here's your character")
        char1 = create_Character()
        show_stats(char1)
        print()
        villain = create_Villain()
        show_stats(villain)
        print()

        points = 0
        while points < 20 and villain["Health"] > 0:
            print(f"Your current amount of notes🎵: {points}")
            points += game_sequence(villain)
            
        if points >= 25:
                print(f"✨✨Congratulations, {char1['Name']}! You collected 25 music notes🎵 and defeated {villain['Name']}!✨✨")
        elif villain["Health"] <= 0:
                print(f"✨✨Congratulations, {char1['Name']}! You collected 25 music notes🎵 and defeated {villain['Name']}!✨✨")
        runagain = input("Would you like to play this game again🥺? Yes or no: ")



    print("Game is ending...")


if __name__ == "__main__":
    main()
