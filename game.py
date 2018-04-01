import random

from consts import *


class Game(object):
    def __init__(self, length=GAME_LENGTH):
        self.length = length
        self.colors = COLORS
        self.initial_state = self.new_game()
        self.turns = 0
        self.is_won = False
        self.is_ended = False

    def new_game(self):
        initial = []
        while len(initial) < self.length:
            r = random.randint(MIN_COLOR, MAX_COLOR)
            if r not in initial:
                initial.append(r)
        initial = [self.colors[i] for i in initial]
        return initial

    def turn(self):
        if self.is_ended:
            print('Game Over')
            return

        guess = input()
        guess = guess.split(",")

        white = 0
        black = 0
        for i in range(self.length):
            if self.initial_state[i] == guess[i]:
                black += 1
            elif guess[i] in self.initial_state:
                white += 1
        print("black {} and white {}".format(black, white))
        self.turns += 1
        self.check_state(black)

    def to_str(self):
        return ' , '.join(self.initial_state)

    def check_state(self, black):
        if self.check_win(black):
            print("Your won!")
            self.end()
        elif self.chek_lose():
            print("شما باختید کلمات مورد نظر {} بودند".format(self.to_str()))

    def check_win(self, black):
        return black == self.length

    def chek_lose(self):
        return (self.turns == MAX_TURNS) and not self.is_won

    def end(self):
        self.is_ended = True

    @staticmethod
    def start():
        for i in range(MAX_COLOR):
            game.turn()


game = Game
game.start()
