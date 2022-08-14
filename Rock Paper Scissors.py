
import random


choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)
player_choice = None
player_score = 0
computer_score = 0

class Game:

    def __init__ (self):
        self.player_score = player_score
        self.computer_score = computer_score
        self.computer = computer
    def randomize(self):
        computer = random.choice(choices)
        self.computer = random.choice(choices)

    def play(self):
        computer = self.computer
        player = input("choose rock, paper, or scissors ").lower()

        if player == computer:
            print(f"Tie! Play again? Current scores: {self.player_score} {self.computer_score}")

        if player == "rock" and computer == "paper":
            self.computer_score += 1
            print(f"computer wins! Computer's current score: {self.computer_score}")

        elif player == "rock" and computer == "scissors":
            self.player_score += 1
            print(f"You win! Your current score: {self.player_score}")

        if player == "scissors" and computer == "rock":
            self.computer_score += 1
            print(f"computer wins! Computer's current score: {self.computer_score}")
        elif player == "scissors" and computer == "paper":
            self.player_score += 1
            print(f"You win! Your current score: {self.player_score}")

        if player == "paper" and computer == "scissors":
            self.computer_score += 1
            computer_score = self.computer_score
            print(f"computer wins! Computer's current score: {self.computer_score}")
        elif player == "paper" and computer == "rock":
            self.player_score += 1
            print(f"You win! Your current score: {self.player_score}")

        print(f"Your score: {self.player_score}")

        print(f"Computer_score {self.computer_score}")

        print("play_again?: ")

        player = input("Yes or no ").lower()

        if player == "yes":
            game_start.randomize()
            game_start.play()
        else:
            print("Come again soon!")


game_start = Game()
game_start.randomize()
game_start.play()