import random


class Die:
    def __init__(self):
        self._value = None

    @property
    def value(self):
        return self._value

    def roll(self):
        self._value = random.randint(1, 6)
        return self._value


class Player:
    def __init__(self, die, is_computer=False):
        self._die = die
        self._is_computer = is_computer
        self._counter = 10

    @property
    def die(self):
        return self._die

    @property
    def is_computer(self):
        return self._is_computer

    @property
    def counter(self):
        return self._counter

    def increment_counter(self):
        self._counter += 1

    def decrement_counter(self):
        self._counter -= 1

    def roll_die(self):
        self._die.roll()


class DiceGame:
    def __init__(self, player, computer):
        self._player = player
        self._computer = computer

    def play(self):
        print("====================================")
        print("Welcome! The game is starting now...")
        print("====================================")

        while True:
            self.play_round()
            if self.check_game_over():
                break

    def play_round(self):
        self._print_welcome_round()

        self._roll_dice()

        self._show_dice(self._player.die.value, self._computer.die.value)

        self._check_round_winner(self._player.die.value, self._computer.die.value)

        self._show_counters()

    def _print_welcome_round(self):
        print("\n---------- New Round ----------")
        input("Press any key to roll the dice.")

    def _roll_dice(self):
        self._player.roll_die()
        self._computer.roll_die()

    def _show_dice(self, player_value, computer_value):
        print(f"\nHuman die: {player_value}")
        print(f"Computer die: {computer_value}")

    def _update_counters(self, winner, loser):
        winner.decrement_counter()
        loser.increment_counter()

    def _check_round_winner(self, player_value, computer_value):
        if player_value > computer_value:
            print("\nThe HUMAN won this round!")
            self._update_counters(self._player, self._computer)
            return player_value
        elif computer_value > player_value:
            print("\nThe COMPUTER won this round!")
            self._update_counters(self._computer, self._player)
            return computer_value
        else:
            print("The round tied.")
            return None

    def _show_counters(self):
        print(f"\nHuman counter: {self._player.counter}")
        print(f"Computer counter: {self._computer.counter}")

    def check_game_over(self):
        if self._player.counter == 0:
            self.show_game_over(self._player)
            return True
        elif self._computer.counter == 0:
            self.show_game_over(self._computer)
            return True
        else:
            return False

    def show_game_over(self, winner):
        print("\n---------------------------------")
        print("- MODAFOKIN GAME OVER MODAFOKAR -")
        if winner.is_computer:
            print("- THE MODAFOKIN *COMPUTER* WON! -")
            print("---------------------------------")
        else:
            print("-- THE MADAFOKIN *HUMAN* WON!! --")
            print("---------------------------------")


player_die = Die()
computer_die = Die()

my_player = Player(player_die)
computer_player = Player(computer_die, is_computer=True)

game = DiceGame(my_player, computer_player)

game.play()
