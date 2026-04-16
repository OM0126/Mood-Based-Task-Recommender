# Mood-Based Activity Suggestion App

A simple Python program that suggests an activity based on your current mood.

---

## Features

* Takes user mood as input
* Suggests a random activity
* Handles invalid input gracefully
* Simple and beginner-friendly code

---

##  Technologies Used

* Python 3
* `random` module

---

##  How It Works

1. User enters their mood (happy, sad, tired, bored)
2. Program checks if mood exists
3. Displays a random suggestion from the list

---

##  Code Example

```python
import random

moods = {
    "happy": ["Go for a run", "Start a new project"],
    "sad": ["Talk to a friend", "Listen to music"],
    "tired": ["Get some sleep", "Take a nap"],
    "bored": ["Play a game", "Watch YouTube", "Try a coding challenge"]
}

m = input("Enter your mood (happy/sad/tired/bored): ").lower()

if m in moods:
    suggestion = random.choice(moods[m])
    print("You should:", suggestion)
else:
    print("Mood not recognized, try again")
```

---

##  How to Run

1. Make sure Python is installed
2. Save the file as `mood.py`
3. Run the program:

```bash
python mood.py
```

---

##  Example

```
Enter your mood: happy
You should: Go for a run
```

---

## Notes

* Input is case-insensitive
* Make sure to type mood correctly

---

##  Future Improvements

* Add more moods
* Build GUI using Tkinter
* Convert into web app
* Add voice input

---

## Author

OM
