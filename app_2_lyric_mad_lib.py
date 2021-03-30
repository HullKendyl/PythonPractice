import random

while True:
    
    noun_list = input("Choose a few nouns: ").split()
    verb_list = input("Choose a few verbs: ").split()
    color_list = input("Choose a few colors: ").split()
    shape_list = input("Choose a few shapes: ").split()
    
    noun = random.choice(noun_list)
    verb = random.choice(verb_list)
    color = random.choice(color_list)
    shape = random.choice(shape_list)

    circle_of_life = f"""From the day we arrive on the {noun}
    And, blinking, {verb} into the sun
    There's more to see than can ever be seen
    More to do than can ever be done
    There's far too much to take in here
    More to find than can ever be found
    But the sun rolling high
    Through the {color} sky
    Keeps great and small on the endless {shape}
    It's the circle of life
    And it moves us all"""
    
    print(circle_of_life)
    
    again = input("Would you like to play again?").lower()
    
    if again == "no":
        break