import module1.func1 as printStatement
import module2.func2 as bigRandomizer
import module3.func3 as smallRandomizer

def main():
    print("This program will use function 3 to pick whether to run function 1 or function 2 first.")
    num=smallRandomizer.randomNum()
    if(num == 2):
        bigRandomizer.randomizer()
        printStatement.simplePrint()
    else:
        printStatement.simplePrint()
        bigRandomizer.randomizer()

if __name__ == "__main__":
    main()
