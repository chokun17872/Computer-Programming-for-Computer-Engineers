"""
Author: passa-
Problem: [monster] นักรบปะทะมอนสเตอร์
Student Code: 6510503310
Branch: Computer Engineering
"""

import numpy as np

class Character:
  def __init__(self,hp):
    self.hp = hp

  def damage(self,dmg):
    self.hp -= dmg
    if self.hp < 0: self.hp = 0
    
class Hero(Character):
  def heal(self):
    self.hp += 20

## main ##
    
X = np.random.RandomState(1)

start_hp = int(input("Blood Start: "))
hero = Hero(start_hp)
monster = Character(start_hp)
dmg = 10
streak = 0

while True:
  ## hero turn ##
  action = input("Attack(a) or Heal(h): ")
  if action == "a":
    val = dmg+(streak*2)
    monster.damage(val)
    streak += 1
    print(f"Monster's HP left {monster.hp}")
  elif action == "h":
    hero.heal()
    print(f"Your HP left {hero.hp}")
    dmg = 10
    streak = 0
    
  if monster.hp == 0:
    print("You win.(^_^)")
    break
    
  ## monster turn ##
  val = X.randint(1, 40)
  hero.damage(val)
  print(f"Monster's turn : Your HP left {hero.hp}")
  
  if hero.hp == 0:
    print("You lose and die.(T_T)")
    break

