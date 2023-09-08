

def hello():
    print("hello, what's your name?")

    name = input()

    print(f"Hello, {name}")

print(__name__)
if __name__ == "__main__":
    hello()