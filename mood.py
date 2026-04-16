import random
mood = input("Enter your mood (happy/sad/tired/bored): ").lower()

if mood == "happy":
    h = random.choice(["go for a run", "start a new project", "bake a treat"])
    print(h)
elif mood == "sad":
    s = random.choice(["talk to a friend", "listen to music"])
    print(s)
elif mood == "tired":
    t = random.choice(["get some sleep", "take a nap"])
    print(t)
elif mood == "bored":
    b = random.choice(["play a game", "watch youtube", "try coding challenge"])
    print(b)
else:
    print("mood not recognized, try again")


