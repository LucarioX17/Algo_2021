from logging import critical
import sys, random, time

class Character():
    max_level = 100

    def __init__(self, level=1, power=25, dexterity=0.4, hp_max=100, critical_chance=0.1, critical_bonus=1.5, type="none"):
        self.level = level
        self.power = power
        self.critical_chance = critical_chance
        self.critical_bonus = critical_bonus
        self.dexterity = dexterity
        self.type = type
        self.hp_max = hp_max
        self.hp = self.hp_max
    
    def level_up(self):
        if (self.level < self.max_level):
            self.level += 1
            self.hp_max += 5
            self.hp = self.hp_max
    
    def level_down(self):
        self.level -= 1
        self.hp_max -= 5
        self.hp = self.hp_max
    
    def attack(self, target):
        rand = random.uniform(0, 1)

        if (rand <= self.critical_chance):
            target.hp -= self.power * self.critical_bonus
            print("\n" + "CRITICAL STRIKE - " + str(self.power*self.critical_bonus) + " damage!")
        else:
            target.hp -= self.power
            print("\n" + str(self.power) + " damage!")
    
    def dodge(self):
        rand = random.uniform(0, 1)
        return rand <= self.dexterity

class Air(Character):
    def __init__(self):
        super().__init__()
        self.type = "Air"
    
    def level_up(self):
        super().level_up()
        self.power += 1
        self.dexterity += 0.1
    
    def level_down(self):
        super().level_down()
        self.power -= 1
        self.dexterity -= 0.1
    
    def attack(self, target):
        super().attack(target)

    def dodge(self):
        return super().dodge()

class Fire(Character):
    def __init__(self):
        super().__init__()
        self.type = "Fire"
    
    def level_up(self):
        super().level_up()
        self.power += 5
        self.dexterity += 0.01
    
    def level_down(self):
        super().level_down()
        self.power -= 5
        self.dexterity -= 0.01
    
    def attack(self, target):
        super().attack(target)
    
    def dodge(self):
        return super().dodge()

class Water(Character):
    def __init__(self):
        super().__init__()
        self.type = "Water"
    
    def level_up(self):
        super().level_up()
        self.power += 2
        self.dexterity += 0.025
    
    def level_down(self):
        super().level_down()
        self.power -= 2
        self.dexterity -= 0.025
    
    def attack(self, target):
        super().attack(target)
    
    def dodge(self):
        return super().dodge()

class Rock(Character):
    def __init__(self):
        super().__init__()
        self.type = "Rock"
    
    def level_up(self):
        super().level_up()
        self.power += 1
        self.hp_max += 5
        self.hp = self.hp_max
        self.dexterity += 0.01
    
    def level_down(self):
        super().level_down()
        self.power -= 1
        self.hp_max -= 5
        self.hp = self.hp_max
        self.dexterity -= 0.01
    
    def attack(self, target):
        super().attack(target)
    
    def dodge(self):
        return super().dodge()

def set_starting_class():
    class_type = input("Choose a starting class - Air | Water | Fire | Rock | None: ")
    
    if (class_type == "Air" or class_type == "air"):
        player = Air()
    elif (class_type == "Water" or class_type == "water"):
        player = Water()
    elif (class_type == "Fire" or class_type == "fire"):
        player = Fire()
    elif (class_type == "Rock" or class_type == "rock"):
        player = Rock()
    elif (class_type == "None" or class_type == "none"):
        player = Character()
    else:
        player = set_starting_class()
    
    return player

def menu_system(wave, player, enemy, turn, extra_turn):
    print("\n" + "Mission - Completed " + str(wave) + "/5 battles")

    menu_option = input("\n" + "Options - Battle | View Stats | Quit: ")

    if (menu_option == "Battle" or menu_option == "battle"):
        battle_system(wave, player, enemy, turn, extra_turn)
    elif (menu_option == "View Stats" or menu_option == "view stats"):
        view_stats(wave, player, enemy, turn, extra_turn)
    elif (menu_option == "Quit" or menu_option == "quit"):
        sys.exit()
    else:
        menu_system(wave, player, enemy, turn, extra_turn)

def view_stats(wave, player, enemy, turn, extra_turn):
    print("\n" + "Stats: ")
    print("Class: " + player.type)
    print("Level: " + str(player.level))
    print("Max HP: " + str(player.hp_max))
    print("HP: " + str(player.hp))
    print("Power: " + str(player.power))
    print("Dexterity: " + str(player.dexterity))

    input("\n" + "Press ENTER to continue...")
    menu_system(wave, player, enemy, turn, extra_turn)

def battle_system(wave, player, enemy, turn, extra_turn):
    if (extra_turn != "player"):
        print("\n" + "Player Type: " + player.type + " | HP: " + str(player.hp))
        print("Enemy Type: " + enemy.type + " | HP: " + str(enemy.hp))
    
    if (turn == "player"):
        print("\n" + "Your Turn: ")
        battle_option = input("Options - Attack | Dodge | Surrender: ")

        if (battle_option == "Attack" or battle_option == "attack"):
            player.attack(enemy)
            turn = "enemy"
        elif (battle_option == "Dodge" or battle_option == "dodge"):
            dodged = player.dodge()
            if (dodged):
                print("\n" + "You successfully dodged the enemy's attack, you now have one extra turn!")
                turn = "player"
                extra_turn = "player"
            else:
                print("\n" + "You failed in dodging the enemy's attack!")
                turn = "enemy"
        elif (battle_option == "Surrender" or battle_option == "surrender"):
            menu_system(wave, player, enemy, turn, extra_turn)
    else:
        if (extra_turn != "player"):
            print("\n" + "Enemy Turn: ")
            time.sleep(1)

            rand = random.uniform(0, 1)

            if (rand <= 0.8):
                enemy.attack(player)
                turn = "player"
            else:
                enemyDodge = enemy.dodge()
                if (enemyDodge):
                    print("\n" + "Enemy successfully dodged your attack and recieves one extra turn!")
                    turn = "enemy"
                    extra_turn = "enemy"
                else:
                    print("\n" + "Enemy attempted to dodge your attack and failed!")
                    turn = "player"
        else:
            turn = "player"
            extra_turn = ""
    
    if (enemy.hp > 0 and player.hp > 0):
        battle_system(wave, player, enemy, turn, extra_turn)
    elif (player.hp <= 0):
        print("\n" + "Defeat!")
        if (player.level > 1):
            print("Lost 1 level.")
            player.level_down()
        menu_system(wave, player, enemy, turn, extra_turn)
    else:
        wave += 1

        if (wave < 5):
            print("\n" + "Congratulations you leved up!")
            player.level_up()
            enemy.level_up()
            menu_system(wave, player, enemy, turn, extra_turn)
        else:
            print("\n" + "Congratulations you completed the mission!")

class Game:
    def start():
        wave = 0
        enemy = Fire()
        turn = "player"
        extra_turn = ""

        print("\n" + "TEXT_RPG.PY" + "\n")

        player = set_starting_class()
        menu_system(wave, player, enemy, turn, extra_turn)
        
Game.start()