import random
moods = {
    "happy" : ["GO FOR A RUN", "START A NEW PROJECT"],
    "sad" : ["TALK TO A FRIEND", "LISTEN TO MUSIC"],
    "tired" : ["GET SOME SLEEP", "TAKE A NAP"],
    "bored" : ["PLAY A GAME", "WATCH YOUTUBE", "TRY CODING CHALLENGE"]
}

m = input("ENTER UR MOOD (HAPPY/SAD/TIRED/BORAD):").lower()

if m in moods:
    suggestion = random.choice(moods[m])
    print("u should:", suggestion)
else:
    print("MOOD NOT RECOGNIZED, TRY AGAIN")


