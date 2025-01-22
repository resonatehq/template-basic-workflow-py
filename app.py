from resonate.context import Context
from resonate.stores.local import LocalStore
from resonate.resonate import Resonate
import random

# Create a Resonate instance with a local store
resonate = Resonate(store=LocalStore())

# Define the register workflow
# Register it with Resonate as a top-level orchestrating generator
@resonate.register
def add(ctx: Context, a: int, b: int):
    print(f"a + b = {a + b}")
    return a + b

def main():
    try:
        # Run the add function asynchronously
        promise = add.run(id=f"add-{random.randint(0, 100)}", a=10, b=20)
        print(f"result: {promise.result()}")
    except Exception as e:
        print({"error": str(e)})

if __name__ == "__main__":
     main()