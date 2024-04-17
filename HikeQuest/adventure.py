import time
import random

def intro():
    print("Welcome to the Hiking Adventure!")
    time.sleep(2)
    print("You are about to embark on a journey through the wilderness.")
    time.sleep(2)
    print("Your goal is to reach the summit of the mountain.")
    time.sleep(2)
    print("As you hike, you'll encounter different obstacles and make decisions that will affect your journey.")

def hike():
    print("\nYou start hiking up the mountain.")
    time.sleep(2)
    print("The trail is steep and rocky, but the scenery is breathtaking.")
    time.sleep(2)
    print("Suddenly, you hear a rustling in the bushes.")

    encounter = random.choice(["animal", "rockslide", "lost"])

    if encounter == "animal":
        animal_encounter()
    elif encounter == "rockslide":
        rockslide_encounter()
    else:
        lost_encounter()

def animal_encounter():
    print("\nAn animal emerges from the bushes!")
    time.sleep(2)
    animal = random.choice(["bear", "mountain lion"])
    print(f"It's a {animal}!")

    choice = input("Do you try to scare it away or remain calm? (scare/calm): ").lower()
    if choice == "scare":
        print("You make yourself look big and shout loudly. The animal backs away and disappears into the forest.")
    else:
        print("You remain calm and slowly back away. The animal loses interest and wanders off.")

def rockslide_encounter():
    print("\nYou hear a rumbling sound above you.")
    time.sleep(2)
    print("A rockslide is heading straight towards you!")

    choice = input("Do you try to outrun it or take cover? (outrun/cover): ").lower()
    if choice == "outrun":
        print("You sprint ahead and narrowly avoid the falling rocks.")
    else:
        print("You quickly find shelter behind a large boulder. The rocks crash around you, but you emerge unscathed.")

def lost_encounter():
    print("\nYou realize you've lost your way.")
    time.sleep(2)
    print("The dense fog makes it difficult to see the trail.")

    choice = input("Do you try to backtrack or continue forward? (backtrack/forward): ").lower()
    if choice == "backtrack":
        print("You carefully retrace your steps and find the trail again.")
    else:
        print("You push forward through the fog, hoping to find your way. After a while, you stumble upon the trail again.")

def summit():
    print("\nAfter a long and challenging hike, you finally reach the summit of the mountain!")
    time.sleep(2)
    print("The view from up here is spectacular. You feel a sense of accomplishment.")

def play_game():
    intro()
    time.sleep(2)

    while True:
        hike()

        choice = input("\nDo you want to continue hiking? (yes/no): ").lower()
        if choice != "yes":
            break

    summit()
    print("Congratulations on completing the Hiking Adventure!")

if __name__ == "__main__":
    play_game()
