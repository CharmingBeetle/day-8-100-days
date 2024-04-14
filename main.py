print(" The Affirmation Generator")
print()
name = input("What's your name sweety?: ")
if name == name:
  print("Hi " + name + "! it's nice to meet you!")

feel = input("Are you feeling good today?: ")
if feel == "yes" or feel == "good" or feel == "Good" or feel == "great" or feel == "Great":
  print("That's great to hear!")
elif feel == "no" or feel == "bad" or feel == "Bad" or feel == "sad" or feel == "Sad":
    print("Oh No! Well I think you are a super person", name, "and I hope you feel better!")
else: 
  print("I'm sorry but I'm not sure who you are. Hope everything is alright with you though!")