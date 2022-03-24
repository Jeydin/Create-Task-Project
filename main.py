import os
import random
from misc import *
import time

os.system("cls")

def start():
  write("yourhealth", 100)
  write("enemyhp", 100)
  print("====== The Great McDonalds Battle ======")
  time.sleep(1)
  print("You are an underage McDonalds worker, who flips burger patties for a living while hoping to get a promotion so you can make a little bit more money.")
  time.sleep(2)
  print("One day, a woman walks into the store and complains about her burger, which turned out to be a little undercooked on the inside.")
  time.sleep(2)
  print("Since no one takes her seriously, she starts throwing things around the restaurant and attacking people.")
  time.sleep(2)
  print("She announces that her name is Karen and that she vows to sue everyone in the restaurant for not caring about her.")
  time.sleep(2)
  print("You walk out of the kitchen with your trusty frying pan to engage in combat with Karen and take care of the problem.")
  time.sleep(2)
  print("Maybe this will get you the promotion you've always wanted.")
  time.sleep(2)
  print()
  print("Press Enter to continue.")
  input("> ")
  os.system("cls")
  battle()

def attack():
  print("====== YOU ATTACKED ======")
  chance = random.randrange(11)
  attack = random.randint(10, 20)
  if chance >= 0 and chance <= 3:
    slowprint(choosestatement("enemydodge"))
    print()
    slowprint("You did not deal any damage to Karen.")
    print()
    print("Your HP:", read("yourhealth"))
    print("Karen's HP:", read("enemyhp"))
    print()
  elif chance >= 4 and chance <= 8:
    slowprint(choosestatement("youattack"))
    health = int(read("enemyhp")) - attack
    print()
    slowprint("You dealt " + str(attack) + " damage to Karen!")
    print()
    print("Your HP:", read("yourhealth"))
    print("Karen's HP: " + str(read("enemyhp")) + "- " + str(attack) + " = " + str(health))
    write("enemyhp", health)
    print()
  else:
    slowprint(choosestatement("youcrit"))
    health = int(read("enemyhp")) - (attack * 2)
    print()
    print("You dealt " + str(attack * 2) + " damage to Karen (" + str(attack) + " x 2)!")
    print()
    print("Your HP:", read("yourhealth"))
    print("Karen's HP: " + str(read("enemyhp")) + "- " + str(attack * 2) + " = " + str(health))
    write("enemyhp", health)
    print()
  print()
  print("Press Enter to continue.")
  input("> ")
  os.system("cls")
  if int(read("enemyhp")) <= 0:
    shedied()
  enemystrike()

def enemystrike():
  print("====== YOU GOT ATTACKED ======")
  chance = random.randrange(11)
  attack = random.randint(10, 20)
  if chance >= 0 and chance <= 3:
    slowprint(choosestatement("youdodge"))
    print()
    slowprint("Karen did not deal any damage to you.")
    print()
    print("Your HP:", read("yourhealth"))
    print("Karen's HP:", read("enemyhp"))
    print()
  elif chance >= 4 and chance <= 8:
    slowprint(choosestatement("enemyattack"))
    health = int(read("yourhealth")) - attack
    print()
    slowprint("You took " + str(attack) + " damage!")
    print()
    print("Your HP: " + str(read("yourhealth")) + "- " + str(attack) + " = " + str(health))
    print("Karen's HP:", read("enemyhp"))
    write("yourhealth", health)
    print()
  else:
    slowprint(choosestatement("enemycrit"))
    health = int(read("yourhealth")) - (attack * 2)
    print()
    print("She dealt " + str(attack * 2) + " damage to you (" + str(attack) + " x 2)!")
    print()
    print("Your HP: " + str(read("yourhealth")) + "- " + str(attack * 2) + " = " + str(health))
    print("Karen's HP:", read("enemyhp"))
    write("yourhealth", health)
    print()
  print()
  print("Press Enter to continue.")
  input("> ")
  os.system("cls")
  if int(read("yourhealth")) <= 0:
    youdied()
  battle()

def youdied():
  os.system("cls")
  print("====== YOU DIED ======")
  slowprint("You died! Karen hit you with her purse too many times and you lost too much HP.")
  slowprint("You feel sad in your last moments, regretting that you even decided to defend a restaurant that barely even payed anything.")
  slowprint("At least, you won't have to worry about getting that promotion anymore.")
  print()
  print("Press Enter to continue.")
  input("> ")
  write("yourhealth", 100)
  write("enemyhp", 100)
  os.system("cls")
  restart()

def shedied():
  os.system("cls")
  print("====== KAREN DIED ======")
  slowprint("You killed Karen! You hit her with your frying pan too many times and she lost too much HP.")
  slowprint("Good job! You successfully defended your restaurant against Karen!")
  slowprint("Your boss was so proud of you that he gave you a promotion!")
  print()
  print("Press Enter to continue.")
  input("> ")
  write("yourhealth", 100)
  write("enemyhp", 100)
  os.system("cls")
  restart()

def runaway():
  print("====== YOU RAN AWAY ======")
  slowprint("You ran away from Karen!")
  slowprint("This proved to be a fatal mistake.")
  slowprint("Karen reaches down and takes her shoe off of her foot.")
  slowprint("Summoning the power of the gods, she hurls her shoe at you with inhuman power.")
  slowprint("The shoe hits you, and you die.")
  print()
  print("Press Enter to continue.")
  input("> ")
  write("yourhealth", 100)
  write("enemyhp", 100)
  os.system("cls")
  restart()

def restart():
  print("====== THANK YOU FOR PLAYING ======")
  slowprint("Thank you for playing my text based game!")
  slowprint("Would you like to play again?")
  print()
  print("Send 1 to restart the game")
  print("Send 2 to terminate the process")
  choice = input("> ")
  if choice == "1":
    os.system("cls")
    start()
  elif choice == "2":
    os.system("cls")
    exit()
  else:
    restart()


def battle():
  print("====== BATTLE ======")
  slowprint("You must defend your restaurant against Karen! Send a number to select an option:")
  print()
  print("Your HP:", read("yourhealth"))
  print("Karen's HP:", read("enemyhp"))
  print()
  print("Send 1 to engage with Karen")
  print("Send 2 to run away from Karen")
  choice = input("> ")
  if choice == "1":
    os.system("cls")
    attack()
  elif choice == "2":
    os.system("cls")
    runaway()
  else:
    os.system("cls")
    battle()

start()