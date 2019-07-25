import random

class monster(object):
    def __init__(self, name, level):  # Initializes the Object
        self.name = name        # Attaches Name to Object
        self.level = level      # Attaches Level to Object

    def print(self):
        print('Name:'. self.name, 'Level:', self.level)

    def get_attack_roll(self):
        die = random.randint(1, 20)
        return die * self.level

    def get_defensive_roll(self):
        die = random.randint(1,20)
        return die * self.level

class Wizard(monster):
    def attack(self, creature):
        print("The wizard %s attacks %s" % (self.name, creature.name))
        print()

        my_roll = self.get_attack_roll()
        creature_roll = creature.get_defensive_roll()

        print("You roll %i" % my_roll)
        print("%s rolls %i" % (creature.name, creature_roll))

        if my_roll >= creature_roll:
            print("The wizard has handily triumphed over %s " % creature.name)
            print()
            return True
        else:
            print("The wizard has been DEFEATED!!!")
            print()
            return False

class Ranger(monster):
    def attack(self, creature):
        print("The ranger %s attacks %s" % (self.name, creature.name))

        my_roll = self.get_attack_roll()
        creature_roll = creature.get_defensive_roll()

        print("You roll %i" % my_roll)
        print("%s rolls %i" % (creature.name, creature_roll))

        if my_roll >= creature_roll:
            print("The ranger has vanquished %s " % creature.name)
            return True
        else:
            print("The ranger is dead!!!")
            return False

class smallCreature(monster):
    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        return base_roll / 2

class largeCreature(monster):
    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        return base_roll / 2

class Dragon(monster):
    def __init__(self, name, level, scaliness, breaths_fire):
        super().__init__(name, level)
        self.breaths_fire = breaths_fire
        self.scaliness = scaliness

    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        # fire_modifier = None
        # if self.breaths_fire:
        #     fire_modifier = 5
        # else:
        #     fire_modifier = 1
        # fire_modifier = VALUE_IF_TRUE if SOME TEST else VALUE IF FALSE
        fire_modifier = 5 if self.breaths_fire else 1
        scale_modifier = self.scaliness / 10

        return base_roll * fire_modifier * scale_modifier