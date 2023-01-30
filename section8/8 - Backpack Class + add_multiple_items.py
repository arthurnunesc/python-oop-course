class Backpack:
    def __init__(self):
        self._items = []

    @property
    def items(self):
        return self._items

    def add_multiple_items(self, items):
        for item in items:
            self.add_item(item)

    def add_item(self, item):
        if isinstance(item, str):
            self._items.append(item)
        else:
            print("Please provide a valid item.")

    def remove_item(self, item):
        if item in self._items:
            self._items.remove(item)
            return 1
        else:
            print("The backpack does not contain that item.")
            return 0

    def has_item(self, item):
        return item in self._items

    def show_items(self, sorted_list=False):
        if sorted_list:
            print(sorted(self._items))
        else:
            print(self._items)


backpack_instance = Backpack()
print(backpack_instance.items)

backpack_instance.add_multiple_items(
    ["Saco de dormir", "Barrinhas de chocolate", "Garrafa d'água"]
)

backpack_instance.show_items()

backpack_instance.show_items(True)
