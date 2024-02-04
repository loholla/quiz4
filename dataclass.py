from dataclasses import dataclass

@dataclass
class basicData:
    name:str
    favNum:int
    favColor:str

def main():
    person=basicData("John",25,"Red")
    text = f"This is {person.name}, who has the favorite number {person.favNum} and favorite color of {person.favColor}."
    print(text)

if __name__=="__main__":
    main()