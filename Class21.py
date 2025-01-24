#Class: 21
#Date: 2025-01-24
#Topic: MODULE - Random

import random
print(random.random()) #between o and 1
print(random.randint(20,90))#from 20 to 90 
print(random.randrange(0,67,2))
name="bar"
vegies=["tamato","cucumber","hfg"]
print(random.choice(vegies))
print(random.choices(vegies,k=2))


template="Hello {} and your age is {} your studying {}"
print(template.format("barathan",10,"fourth standard"))
template="Hello {name} and your age is {age} your studying {std}"
print(template.format(name="barathan",age=10,std="fourth standard"))

#story generator:

templates=["Once upon a time there was a {adjective}{animal} called {name}. he has a friend called grasshopper","Once upon a time there lived a {animal} family.They had gone out for a trip.A girl named {name} came to the house.She was tired so she slept in the {animal} familys house.When the {animal} family returned they chased {name} away.","In a forest,there lived a {animal}.He was so hungry.One day while he was searching for food, a {animal} told him that there is a grape field in a farm.The {animal} also listened to him and went there.he saw the grape tree and tried to take it but he failed.He tried again and again but failed to catch it,so he thought that the grapes were sour and went searching for food again."]
adjectives=["brave","clever","lazy","cunning",]
animals=["tiger","lion","fox","bear","squirrel"]
names=["cordielia","sudha","murty","ilakiya"]
template=random.choice(templates)


story=template.format(
    adjective=random.choice(adjectives),
    animal=random.choice(animals),
    name=random.choice(names)
)
print(story)