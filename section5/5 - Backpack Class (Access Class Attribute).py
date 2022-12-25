class Backpack:
    max_num_items = 10

    def __init__(self):
        self.items = []


my_backpack = Backpack()
your_backpack = Backpack()

print(Backpack.max_num_items)

print(my_backpack.max_num_items)
print(your_backpack.max_num_items)
