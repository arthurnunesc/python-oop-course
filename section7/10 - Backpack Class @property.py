class Backpack:
    def __init__(self):
        self._items = []

    @property
    def items(self):
        print("Calling the getter...")
        return self._items

    @items.setter
    def items(self, new_items):
        print("Calling the setter...")
        if isinstance(new_items, list):
            self._items = new_items
        else:
            print("Please enter a valid list of items.")


my_backpack = Backpack()
print(my_backpack.items)

my_backpack.items = ["Water Bottle", "Sleeping Bag"]
print(my_backpack.items)

my_backpack.items = "Hello, World!"  # Invalid value.
print(my_backpack.items)
