name = "REPLACE ME"

def introduce_self(name=name):
    print(f"Hello, my name is {name}")

def announce_celebrity_crush():
    try:
        with open('celebrity_crush.txt') as file:
            crush = file.readline()
            print(f"My celebrity crush is {crush}")
    except FileNotFoundError:
        print("I... don't know what to say. Please help.")

if __name__ == "__main__":
    introduce_self()
    announce_celebrity_crush()

