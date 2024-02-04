from dataclasses import dataclass

@dataclass
class basicData:
    name:str
    favNum:int
    favColor:str

    def outputData(self)->None:
        text=f"I am {self.name}, and my favorite number is {self.favNum}. My favorite color is {self.favColor} too."
        print(text)

def main():
    person=basicData("Kaya",15,"Purple")
    person.outputData()

if __name__=="__main__":
    main()