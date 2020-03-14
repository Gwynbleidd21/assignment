def main():
    print('Type some string to have it reversed and uppercase.\nType :q to exit.')
    while True:
        # get user input
        txt = input("Your input string: ")

        # program ending condition
        if ':q' == txt:
            break
        # printing result in reversed order and in uppercase
        print("Result", txt[::-1].upper())


if __name__ == "__main__":
    main()
