class Character:
    level_max = 100

    def __init__(self, level=1, strength=10, hp_max=100):
        self.__level = level
        self.__strength = strength
        self.__hp_max = hp_max
        self.__hp = self.__hp_max
        self.__weapon = Weapon()
    
    def equip_weapon(self, weapon):
        raise NotImplementedError("Class not defined for character!")
    
    def level_up(self):
        self.__level += 1
        self.__strength += 5
        self.__hp_max += 10

    def attack(self, target):
        target.__hp -= (self.__strength + self.__weapon.get_damage())
    
    def is_alive(self):
        return self._hp > 0
    
    def get_variable(self, var):
        switch = {
            "hp": self.__hp,
            "hp_max": self.__hp_max,
            "level": self.__level,
            "strength": self.__strength,
            "weapon_damage": self.__weapon.get_damage()
        }
        
        return switch.get(var, "nothing")
    
    def set_hp(self, hp):
        self.__hp = hp

    def set_strength(self, strength):
        self.__strength = strength

class Mage(Character):
    def __init__(self):
        super().__init__()
        self.__magic = 5
    
    def level_up(self):
        super().level_up()
        self.__magic += 1
    
    def attack(self, target):
        target.set_hp(target.get_variable("hp") - (super().get_variable("strength") + self.__weapon.get_damage() + self.__magic))
    
    def equip_weapon(self, weapon):
        if isinstance(weapon, Wand):
            self.__weapon = weapon

class Warrior(Character):
    def __init__(self):
        super().__init__()
    
    def level_up(self):
        super().level_up()
        self.set_strength(self.get_variable("strength") + 2)
    
    def attack(self, target):
        target.set_hp(target.get_variable("hp") - (super().get_variable("strength") + self.__weapon.get_damage()))
    
    def equip_weapon(self, weapon):
        if isinstance(weapon, Sword):
            self.__weapon = weapon

class Weapon:
    def __init__(self, weapon_damage = 1):
        self.__damage = weapon_damage
    
    def get_damage(self):
        return self.__damage

class Wand(Weapon):
    def __init__(self, weapon_damage = 1, type = "Fire"):
        super().__init__(weapon_damage)
        self.__type = type

class Sword(Weapon):
    def __init__(self, weapon_damage = 1):
        super().__init__(weapon_damage)

class Game:
    def start():
        player = Mage()
        enemy = Warrior()

        wand = Wand(5)
        player.equip_weapon(wand)

        player.attack(enemy)
        print(enemy.get_variable("hp"))

Game.start()