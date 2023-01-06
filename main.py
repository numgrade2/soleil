"""Super doc."""


def hello(name=None):
    """Super doc func."""
    if name:
        print("Hello {name}.")
    else:
        print("Hello!")


def goodbye():
    """Super doc."""
    print("Goodbye")
    

if __name__ == "__main__":
    hello()
    goodbye()
