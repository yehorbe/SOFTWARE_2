class Adventurer:
    def __init__ (self, name):
        self.health_points = 100
        self.stamina = 100
        self.attack_damage = 10
        self.name = name

    def gain_health(self, value):
        self.health_points+=value

    def lose_life(self, value):
        if value<self.health_points:
            self.health_points-=value
        else:
            self.health_points = 0

class Mage(Adventurer):
    def __init__(self, name):
        super().__init__(name)
        self.health_points=50
        self.attack_damage=20

    def party_heal(self, party_obj):
        for member in party_obj.members:
            member.gain_health(50)
        return

class Palladin(Adventurer):
    def __init__(self,name):
        super().__init__(name)
        self.health_points=150
        self.attack_damage=5

class Rogue(Adventurer):
    def __init__(self,name):
        super().__init__(name)
        self.health_points=100
        self.attack_damage=10



class Party:
    def __init__(self):
        self.members=[]

    def add_member(self, adventurer):
        self.members.append(adventurer)

    def retire_member(self, adventurer):
        self.members.remove(adventurer)

    def show_members(self,):
        for i in self.members:
            print(i.name)

    def show_health(self):
        for member in self.members:
            print(f'{member.name} HP:{member.health_points}')

hero1=Palladin('Palladin')
hero2=Mage('Mage')
hero3=Rogue('Rogue')

new_party=Party()
new_party.add_member(hero1)
new_party.add_member(hero2)
new_party.add_member(hero3)
print('='*20)
new_party.show_members()
print('='*20)
new_party.show_health()
print('='*20)
hero1.lose_life(100)
hero2.lose_life(20)
hero3.lose_life(50)
new_party.show_health()
print('='*20)
hero2.party_heal(new_party)
new_party.show_health()
print('='*20)
new_party.retire_member(hero2)
new_party.show_members()




