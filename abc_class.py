from abc import ABC , abstractmethod
import os
import random

class CreatureBase(ABC):
    @abstractmethod
    def hp(self):
        pass
    
    @abstractmethod
    def ac(self):
        pass

    @abstractmethod
    def printStats(self):
        pass

class PlayerCharacter(CreatureBase):
    def __init__(self):
        pass

    def hp(self):
        self.hp = random.randint(4,24)

    def ac(self):
        self.ac = random.randint(13,18)

    def printStats(self):
        print("Player HP:",self.hp, ",", "Player AC:",self.ac)

class EnemyCharacter(CreatureBase):
    def __init__(self):
        pass

    def hp(self):
        self.hp = random.randint(2,12)
    
    def ac(self):
       self.ac=random.randint(8,14)

    def printStats(self):
        print("Enemy HP:",self.hp, ",", "Enemy AC:",self.ac)

def main():
    player1=PlayerCharacter()
    player1.ac()
    player1.hp()
    player1.printStats()

    enemy1=EnemyCharacter()
    enemy1.ac()
    enemy1.hp()
    enemy1.printStats()

if __name__=="__main__":
    main()