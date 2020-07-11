import random


class Game:
    WIN_BIT = "O"
    EMPTY_BIT = " "

    def __init__(self, bits=3):
        self.bits = bits
        self.vars = [self.EMPTY_BIT for _ in range(bits-1)]
        self.vars.append(self.WIN_BIT)

    @property
    def variants_number(self):
        return self.bits

    def start(self):
        random.shuffle(self.vars)

    def is_winner(self, guess):
        return self.vars[guess-1] == self.WIN_BIT


if __name__ == "__main__":
    game = Game(bits=5)
    while True:
        game.start()
        print(f"There are {game.variants_number} bits on table.")
        guess = int(input("And your guess is..?"))
        if 0 < guess <= game.variants_number:
            if game.is_winner(guess):
                print('Congrats!')
                print(game.vars)
                break
            else:
                print(f'Nice shoot, cowboy! But the winning bit is: {game.vars.index(game.WIN_BIT) +1 }')
                print(game.vars)
