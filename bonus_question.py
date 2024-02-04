def counter(array):
    outputArray = []
    length = len(array)
    iterator = 0
    while(iterator < length):
        arrayItem = str(array[iterator])
        outputArray.append(len(arrayItem))
        iterator = iterator + 1
    return outputArray


def main():
    # Fill in the array with your choice of strings or numbers. You can replace what I have if you choose
    array = ["Goodbye", "Hello From The Other Side", "Hello"]
    output = counter(array)
    print(output)

if __name__ == "__main__":
    main()