"""
Author: passa-
Problem: [monster 2] นักรบปะทะมอนสเตอร์ 2
Student Code: 6510503310
Branch: Computer Engineering
"""

import numpy as np
from math import floor
X = np.random.RandomState(1)

class Character:
    def __init__(self,hp,spd):
        self.hp = hp
        self.spd = spd

class Hero(Character):
    def __init__(self,hp,spd,kill=0):
        self.kill = kill
        super(Hero, self).__init__(hp, spd)

    def attack(self,other,streak):
        other.hp -= (10 + streak*2)
        if other.hp < 0:
            other.hp = 0
            self.kill += 1

    def heal(self,n):
        self.hp += 20*n

class Monster(Character):
    def __init__(self,hp,spd,id):
        self.id = id
        super(Monster, self).__init__(hp, spd)

    def attack(self,hero):
        hero.hp -= X.randint(1, 40)
        if hero.hp < 0:
            hero.hp = 0

def r_input():
    s_hp = int(input("Blood Start: "))
    spd = int(input("Your speed: "))
    n = int(input("Number of monsters: "))
    m_spd = []
    for i in range(n):
        m_spd.append(int(input(f"Monster {i+1} speed: ")))
    return s_hp,spd,n,m_spd

def gen_character(s_hp,spd,n,m_spd):
    hero = [Hero(s_hp,spd)]
    monsters = [Monster(floor(s_hp/n), m_spd[i], i+1) for i in range(len(m_spd))]
    characters = hero + monsters
    characters.sort(key=lambda x:x.spd, reverse=True)
    return characters

def hero_action(hero,monster,n,streak):
    print("- Your Turn -")
    action = input("Attack(a) or Heal(h): ")
    if action == "a":
        hero.attack(monster,streak)
        print(f"Monster {monster.id} HP left {monster.hp}")
        return hero,monster,streak+1
    elif action == "h":
        hero.heal(n)
        print(f"Your HP left {hero.hp}")
        return hero,monster,0

def monster_action(hero,monster):
    print(f"- Monster {monster.id} Turn -")
    monster.attack(hero)
    print(f"Your HP left {hero.hp}")
    return hero,monster

def find_char_idx(characters,option):
    if option == "h":
        for character in characters:
            if isinstance(character, Hero):
                return characters.index(character)
    elif option == "m":
        for character in characters:
            if character.hp != 0 and isinstance(character, Monster):
                return characters.index(character)

def play(characters,n):
    turn = 0
    idx = 0
    streak = 0

    while True:
        first_attacker_idx = min(find_char_idx(characters,"h"), find_char_idx(characters,"m"))
        if idx % (n+1) == first_attacker_idx:
            turn += 1
            print("=========================")
            print(f"Turn {turn}")
            print("-------------------------")

        attacker = characters[idx%(n+1)]

        if isinstance(attacker, Hero):
            monster_idx = find_char_idx(characters,"m")
            hero = attacker
            monster = characters[monster_idx]
            characters[idx%(n+1)], characters[monster_idx], streak = hero_action(hero,monster,n,streak)
            if characters[idx%(n+1)].kill == n:
                print("You win.(^_^)")
                break

        elif isinstance(attacker, Monster) and attacker.hp != 0:
            hero_idx = find_char_idx(characters,"h")
            hero = characters[hero_idx]
            monster = attacker
            characters[hero_idx], characters[idx%(n+1)] = monster_action(hero,monster)
            if characters[hero_idx].hp == 0:
                print("You lose and die.(T_T)")
                break

        idx += 1

# main ##

s_hp,spd,n,m_spd = r_input()
characters = gen_character(s_hp,spd,n,m_spd)
play(characters,n)
