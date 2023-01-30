class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_left(self, decrement_x=2):
        self.x -= decrement_x

    def move_down(self, decrement_y=5):
        self.y -= decrement_y

    def move_up(self, increment_y=5):
        self.y += increment_y

    def move_right(self, increment_x=2):
        self.x += increment_x


player_instance = Player(0, 0)
print(player_instance.y)

player_instance.move_up()
print(player_instance.y)

player_instance.move_up(8)
print(player_instance.y)

player_instance.move_down()
print(player_instance.y)

player_instance.move_down(3)
print(player_instance.y)
