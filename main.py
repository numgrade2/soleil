"""Super doc."""


def ask_name():
    """Super doc for ask name."""
    name = input("What's your name? ")
    return name


def hello(name=None):
    """Super doc func."""
    if name:
        print(f"Hello {name}.")
    else:
        print("Hello!")

        
def goodnight():
    """Doc."""
    print("Good night!")
       

def goodbye():
    """Super doc."""
    print("Goodbye")
    

if __name__ == "__main__":
    name = ask_name()
    hello(name)
    goodbye()
