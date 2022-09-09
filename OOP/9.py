"""
Author: passa-
Problem: [monster 2] นักรบปะทะมอนสเตอร์ 2
Student Code: 6510503310
Branch: Computer Engineering
"""

## not finished yet ## 

import numpy as np
from math import floor
X = np.random.RandomState(1)

class Character:
    def __init__(self,hp,spd):
        self.hp = hp
        self.spd = spd

class Hero(Character):
    def heal(self,n):
        self.hp += 20*n
    
    def attack(self,monster,streak):
        if monster.hp < 10+(streak*2):
            monster.hp = 0
        else:
            monster.hp -= 10+(streak*2)

class Monster(Character):
    def __init__(self,id):
        self.id = id

    def attack(self,hero):
        damage = X.randint(1, 40)
        if hero.hp < damage:
            hero.hp = 0
        else:
            hero.hp -= damage

def r_input():
    start_hp = int(input("Blood Start: "))
    speed = int(input("Your speed: "))
    hero = Hero(start_hp,speed)
    n = int(input("Number of monsters: "))
    monsters = []
    for i in range(n):
        speed = int(input(f"Monster {i+1} speed: "))
        monster = Monster(floor(start_hp/n), speed, i+1)
        monsters.append(monster)
    return hero,monsters,n

def gen_characters_turn(hero,monsters):
    characters = [[monster.speed,monster] for monster in monsters] + [hero.speed,hero]
    characters.sort(key=lambda x:x[0])
    return characters

def dead(monsters,monsters_speed,idx):
    monsters.pop(idx)
    monsters_speed.pop(idx)
    return monsters,monsters_speed

def hero_action(hero,characters,streak,n):
    print("- Your Turn -")
    action = input("Attack(a) or Heal(h): ")
    monsters = [character[0] for character in characters if issubclass(character, Monster)]
    if action == "a":
        hero.attack(monsters[0],streak)
        streak += 1
        print(f"Monster {monsters[0].id} HP left {monsters[0].hp}")
    if monsters[0].hp == 0:   # hero kills monster
        characters.pop(0)
    elif action == "h":
        hero.heal(n)
        print(f"Your HP left {hero.hp}")
        streak = 0

# def monster_action():
#     for monster in monsters:
#         print(f"- Monster {1} Turn -")


def play(hero,monsters,n):
    characters = gen_characters_turn(hero,monsters)
    streak = 1
    while True:
        for i in range(len(characters)):
            if issubclass(characters[i], Hero):
                hero,characters = hero_action(hero,characters,streak,n)
            elif issubclass(characters[i], Monster):
                # monster_action()
            if len(characters) == 1:
                print("You win.(^_^)")
                break
            elif hero.hp == 0
                print("You lose and die.(T_T)")
                break
        
## main ##

hero,monsters,n = r_input()
turn = 1
print("=========================")
print(f"Turn {turn}")
print("-------------------------")
play(hero,monsters,n)
