from typing import Protocol
import os
import random

class CreatureBase(Protocol):
    def hp(self)->None:
        pass
    
    def ac(self)->None:
        pass

    def printStats(self)->None:
        pass

class PlayerCharacter:
    def __init__(self)->None:
        self.hp()
        self.ac()

    def hp(self)->None:
        self.hp = random.randint(4,24)

    def ac(self)->None:
        self.ac = random.randint(13,18)

    def printStats(self)->None:
        print("Player HP:",self.hp, ",", "Player AC:",self.ac)

class EnemyCharacter:
    def __init__(self)->None:
        self.hp()
        self.ac()

    def hp(self)->None:
        self.hp = random.randint(2,12)
    
    def ac(self)->None:
       self.ac=random.randint(8,14)

    def printStats(self)->None:
        print("Enemy HP:",self.hp, ",", "Enemy AC:",self.ac)

def main():
    player1=PlayerCharacter()
    player1.printStats()

    enemy1=EnemyCharacter()
    enemy1.printStats()

if __name__=="__main__":
    main()