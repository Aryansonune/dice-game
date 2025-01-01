import random

dice = int(input("Dice: "))

if  (dice <= 0):
    print ("Must have at least one dice!")
    quit()

sides = int(input("Sides: "))

if (sides <= 0):
    print ("Must have at least one side!")
    quit ()

roll = []

for i in range(0, dice):
    face = random.randint(1, sides)
    roll.append(face)

print(roll)