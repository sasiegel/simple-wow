import abilities

class Hero(object):
    def __init__(self, name, lvl):
        self.name = name
        self.lvl = lvl
        self.hp = 100
        self.mana = 60
        self.basic_dmg = 5
    def basic_attack(self, target):
        target.hp -= self.basic_dmg

class Mage(Hero):
    def __init__(self, name, lvl):
        super().__init__(name, lvl)
        self.hp -= 20
        self.mana += 20
        self.basic_dmg -= 1
        self.abilities = (self.basic_attack, self.fireblast)
    def fireblast(self, target: Hero):
        if self.mana >= 15:
            print('kaboom!')
            self.mana -= 15
            target.hp -= 30
        else:
            print('oom')

class Paladin(Hero):
    def __init__(self, name, lvl):
        super().__init__(name, lvl)
        self.hp += 10
        self.mana -= 30
        self.basic_dmg += 7
        self.abilities = (self.basic_attack, self.crusader_strike)
    def crusader_strike(self, target: Hero):
        if self.mana >= 20:
            print('kapow!')
            self.mana -= 20
            target.hp -= 25
        else:
            print('oom')
