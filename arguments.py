import argparse

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(help="String",dest="userString",type=str)
    parser.add_argument(help="Integer",dest="userInteger",type=int)
    parser.add_argument(help="Float",dest="userFloat",type=float)
    args=parser.parse_args()
    text = f"Your string is '{args.userString}', your integer is '{args.userInteger}', and your float is '{args.userFloat}'."
    print(text)

if __name__ == "__main__":
    main()