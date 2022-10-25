# IMPORTS
import random


# SOLDIER
# Receive **2 arguments** (1st health & 2nd strength), self doesn't "count"
class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):  # receive **0 arguments** (self doesn't count)
        return self.strength  # return strength` property

    def receiveDamage(self, damage):  # receive **1 argument** (the damage)(self doesn't count)
        self.damage = damage

        # remove the received damage from the `health` property
        self.health = self.health - damage

        return  # returns nothing


# VIKING
# Viking` inherit from `Soldier`
class Viking(Soldier):
    def __init__(self, name, health, strength):  # receive **3 arguments** (1st name, 2nd health & 3rd strength)
        super().__init__(health, strength)  # specifies the inherited properties
        self.name = name

    # def attack(self):
    # This method should be **inherited** from `Soldier`, no need to reimplement it.
    # return self.strength

    def receiveDamage(self, damage):
        # This method needs to be **reimplemented** for `Viking` because the `Viking`
        # version needs to have different return values.
        self.health = self.health - damage

        # if the `Viking` is still alive**, it should return **"NAME has received DAMAGE points of damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"

        else:  # **if the `Viking` dies**, it should return **"NAME has died in act of combat"**
            return f"{self.name} has died in act of combat"

    def battleCry(self):  # should receive **0 arguments** (remember self doesn't count)
        return "Odin Owns You All!"  # return **"Odin Owns You All!"**. Be careful misspelling the battlecry, it will raise an error.


# SAXON
# Saxon inherit from `Soldier`

class Saxon(Soldier):
    def __init__(self, health, strength):  # receive **2 arguments** (1st health & 2nd strength)
        super().__init__(health, strength)

    # def attack(self):
    # This method should be **inherited** from `Soldier`, no need to reimplement it.
    # return self.strength

    def receiveDamage(self, damage):  # receive **1 argument** (the damage)
        self.damage = damage
        self.health = self.health - damage

        # if the Saxon is still alive**, it should return _**"A Saxon has received DAMAGE points of damage"**
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"

        else:  # if the Saxon dies**, it should return _**"A Saxon has died in combat"**_
            return f"A Saxon has died in combat"


# WAR
# receive **0 arguments**

class War:
    def __init__(self):
        self.vikingArmy = []  # assign an empty array to the **`vikingArmy` property** (We'll fill it later)
        self.saxonArmy = []  # assign an empty array to the **`saxonArmy` property**(We'll fill it later)

    def addViking(self, viking):  # receive **1 argument** (a `Viking` object)
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):  # same but with saxon army
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        v = random.choice(self.vikingArmy)  # select random viking
        s = random.choice(self.saxonArmy)  # select random saxon

        # v.attack() => With this I generate a viking attack with the viking previously created
        # s.receiveDamage () => Saxon gets the damage that.

        attack_v = s.receiveDamage(v.attack())  # the Saxon receives Damage equal to the `strength` of a `Viking`

        if s.health <= 0:  # If saxon is dead
            self.saxonArmy.remove(s)  # remove it from the army list
        return attack_v

    def saxonAttack(self):  # same but for saxon attacks
        v = random.choice(self.vikingArmy)
        s = random.choice(self.saxonArmy)

        attack_s = v.receiveDamage(s.attack())

        if v.health <= 0:
            self.vikingArmy.remove(v)
        return attack_s

    def showStatus(self):  # receive **0 arguments**
        # if the `Saxon` array is empty**
        if len(self.saxonArmy) == 0 and len(self.vikingArmy) > 0:
            # return _**"Vikings have won the war of the century!"**_
            return "Vikings have won the war of the century!"

        # **if the `Viking` array is empty**
        elif len(self.vikingArmy) == 0 and len(self.saxonArmy) > 0:
            # return _**"Saxons have fought for their lives and survive another day..."**_
            return "Saxons have fought for their lives and survive another day..."

        # **if there are at least 1 `Viking` and 1 `Saxon`**
        else:
            # return _**"Vikings and Saxons are still in the thick of battle."**_
            return "Vikings and Saxons are still in the thick of battle."