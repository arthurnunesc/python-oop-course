class Backpack:
    max_num_items = 10

    def __init__(self):
        self.items = []


print(Backpack.max_num_items)

my_backpack = Backpack()
print(my_backpack.max_num_items)

Backpack.max_num_items = 15

print(Backpack.max_num_items)
print(my_backpack.max_num_items)
