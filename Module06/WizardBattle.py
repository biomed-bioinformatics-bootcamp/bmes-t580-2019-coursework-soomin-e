import time
import random

from Characters import Wizard, Ranger, monster, smallCreature, largeCreature, Dragon

# Print Header
print('--------------------')
print('   WIZARD BATTLE')
print('____________________')
print()


# Lists the Creatures
creatures = [
    smallCreature('Goat', 1),
    smallCreature('Bat', 3),
    largeCreature('MindFlare', 5),
    Dragon('Dragon', 50, 75, True),
    Wizard('Evil Wizard', 1000)
]

# print(creatures)

hero = Wizard('Geralt', 75)

while True:

    active_creature = random.choice(creatures)
    print('A %s of level %s has appear from a dark and foggy forest...' % (active_creature.name, active_creature.level))
    print()

    cmd = input('Do you [a]ttack, [r]unaway, or [l]ook around? ')
    if cmd == 'a':
        if hero.attack(active_creature):
            creatures.remove(active_creature)
        else:
            print("The wizard runs and hides taking time to recover...")
            time.sleep(5)
            print("The wizard returns revitalized!")
    elif cmd == 'r':
        print('The wizard has become unsure of his power and flees!!!')
    elif cmd == 'l':
        print('The wizard {} takes in the surroundings and sees:'
              .format(hero.name))
        for c in creatures:
            print(' * A {} of level {}'.format(c.name, c.level))
    else:
        print("OK, exiting game... bye!")
        break

    if not creatures:
        print("You've defeated all the creatures, well done!")
        break

    print()
