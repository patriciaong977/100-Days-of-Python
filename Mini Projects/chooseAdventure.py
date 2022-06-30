print('''
0=========================================================0
|'.                   All About Animals                 .'|
|  '. _______________________________________________ .'  |
|    |             /\ /\.-. .                       .|    |
|    | '. ________|  `  `.' .`. | /______________ .' |    |
|    |   |         \  `/ >>-' -`* -              |   |    |
|    |   |         /  ,\ '    / | \        ____  |   |    |
|    |   |         `-'`.:`.               |    | |   |    |
|    |   |             > ,`.              |    | |   |    |
|    |   |      /-.   /.' `.              |____| |   |    |
|    |   |     /  _>  `-    : |\_/|              |   |    |
|    |   |   /` /    /-.      |q p|   /�         |   |    |
|    |  ,|  /  ((___/ __>     ( 0 )"""\    __    |   |    |
|    |   \/`  /      }        |"^"`    | ;`'()__)|   |    |
|    |   |\ /'\ .--.(         || /=\\ |  `\:'.`,\|   |    |
|    | .' -\\--\\-- \\--------"'" -'"""'---//--"//'. |    |
|    |'  DS &  jgs                                  '|    |
|  .'------------------------------------------------ '.  |
|.'                      PetShop                        '.|
0=========================================================0
''')
print("Welcome to All About Animals.")
print("Your mission is to find the best pet for you at the PetShop.")

# Write your code below this line 👇

# Scenario
print("\nYou are at the PetShop. You see a cat, a dog, and a bird. \n You're unsure which one to choose.\n")
print ('The shopkeeper grabs your attention and says, "I have a few questions to help you decide."')

# Ask the user if they want a pet that can fly. Make sure all answers are in lowercase.
choice = input("\nDo you want a pet that can fly or that walks on the ground? (fly/ground) ").lower()

# If the user answers yes, choose a bird.
if choice == "fly":
  print("\nYou have chosen a bird as your pet.\n Congratulations on your new pet bird!\n")
else: # If the user answers ground.
  choice2 = input("Do you want a pet that loves the outdoors, or indoors? (outdoors/indoors)")
  if choice2 == "indoors": # If the user answers indoors.
    choice3 = input("Do you want a playful pet or a relaxing pet? (playful/relaxing)").lower()
    if choice3 == "playful": # If the user answers playful.
      print("\nYou have chosen a dog as your pet.\n Congratulations on your new pet dog!\n")
    else: # If the user answers relaxing.
      print("\nYou have chosen a cat as your pet.\n Congratulations on your new pet cat!\n")
  else: # If the user answers outdoors.
    choice4 = input("Are you sure you want a pet that can't fly? (yes/no/not sure)").lower()
    if choice4 == "yes":
      print("\n You have chosen a dog as your pet.\n Congratulations on your new pet dog!\n")
    elif choice4 == "no":
      choice5 = input("\n Would you like to consider a bird as your pet? (yes/no)?").lower()
      if choice5 == "yes":
        print("\n You have chosen a bird as your pet.\n Congratulations on your new pet bird!\n")
      else:
        print("\n You have chosen a dog as your pet.\n Congratulations on your new pet dog!\n")
    else:
      print("\n Maybe you should think more about what pet you want and come back next time.\n")
