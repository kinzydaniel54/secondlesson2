place = input("choose a place: forest or cave")

if place == "forest":
  action = input("climb a tree or cross a river")
  if action == "climb a tree":
    print ("you found a bird's nest")
  else: 
    print("you found a boat")
elif place == "cave":
    print("you find a hidden treasure")
    action = input("light a torch or proceed in the dark")
    if action == ("light a torch"):
        print("you proceed into the cave with a lit torch")
    else:
        print("you proceeded into the dark without a lit torch") 
else:input("wrong answer") 

pass 