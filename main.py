import argparse


def main():
    parser = argparse.ArgumentParser(description='Reverse and uppercase a text string using command line arguments.')
    parser.add_argument('input_string', type=str, help='Input string to be processed.')
    args = parser.parse_args()
    print("Result:", args.input_string[::-1].upper())


if __name__ == "__main__":
    main()
