
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--first", help="First number")
    parser.add_argument("--second", help="Second number")
    parser.add_argument("--operator", help="Operator (+, -, *, /)")
    return parser.parse_args()

def main():
    args = parse_args()

    first = int(args.first)
    second = int(args.second)
    operator = args.operator

    if operator == '+':
        print(f"Result: {first + second}")

    elif operator == '-':
        print(f"Result: {first - second}")
    
    elif operator == '*':
        print(f"Result: {first * second}")
    
    elif operator == "/":
        print(f"Result: {first / second}")


if __name__ == "__main__":
    main()