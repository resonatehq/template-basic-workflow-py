import random

from resonate import Resonate, Context
from resonate.stores import LocalStore


# Create a Resonate instance with a local store
resonate = Resonate(store=LocalStore())

# Register a function with Resonate
@resonate.register
def add(ctx: Context, a: int, b: int):
    print(f"{a}+{b} = {a + b}")
    return a + b

def main():
    try:
        # Run the add function
        a = random.randint(0, 100)
        b = random.randint(0, 100)
        handle = add.run(f"add({a}, {b})", a, b)
        print(f"result: {handle.result()}")
    except Exception as e:
        print({"error": str(e)})

if __name__ == "__main__":
    main()
