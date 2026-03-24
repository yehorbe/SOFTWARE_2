class Character:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"I am {self.name}")

class MarioCharacter(Character):
    def __init__(self, name, lives):
        super().__init__(name)
        self.lives = lives

    def jump(self):
        print(f"{self.name} jumps!")

class FireMario(MarioCharacter):
    def __init__(self, name, lives):
        super().__init__(name, lives)

    def throw_a_fireball(self):
        print(f"{self.name} throws a fireball!")

normal_mario = MarioCharacter("Mario", 3)
fire_mario = FireMario("Fire Mario", 5)

normal_mario.jump()
fire_mario.throw_a_fireball()