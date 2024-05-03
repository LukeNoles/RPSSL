class Play():
    def __init__ (self):
        self.user_value = 0
        self.computer_value = 0
    def run_game(self):
        if self.user_value == self.computer_value:
            return "It's a tie!"
        elif self.user_value == 1 and self.computer_value == 3:
            return "Rock smashes scissors! You win!"
        elif self.user_value == 1 and self.computer_value == 4:
            return "Rock crushes lizard! You win!"
        elif self.user_value == 2 and self.computer_value == 1:
            return "Paper covers rock! You win!"
        elif self.user_value == 2 and self.computer_value == 5:
            return "Paper disproves Spock! You win!"
        elif self.user_value == 3 and self.computer_value == 2:
            return "Scissors cuts paper! You win!"
        elif self.user_value == 3 and self.computer_value == 4:
            return "Scissors chops lizard! You win!"
        elif self.user_value == 4 and self.computer_value == 2:
            return "Lizard eats paper! You win!"
        elif self.user_value == 4 and self.computer_value == 5:
            return "Lizard poisons Spock! You win!"
        elif self.user_value == 5 and self.computer_value == 1:
            return "Spock blasts rock! You win!"
        elif self.user_value == 5 and self.computer_value == 3:
            return "Spock vaporizes scissors! You win!"
        elif self.user_value == 1 and self.computer_value == 3:
            return "Rock smashes scissors! You lose!"
        elif self.user_value == 4 and self.computer_value == 1:
            return "Rock crushes lizard! You lose!"
        elif self.user_value == 1 and self.computer_value == 2:
            return "Paper covers rock! You lose!"
        elif self.user_value == 5 and self.computer_value == 2:
            return "Paper disproves Spock! You lose!"
        elif self.user_value == 2 and self.computer_value == 3:
            return "Scissors cuts paper! You lose!"
        elif self.user_value == 4 and self.computer_value == 3:
            return "Scissors chops lizard! You lose!"
        elif self.user_value == 2 and self.computer_value == 4:
            return "Lizard eats paper! You lose!"
        elif self.user_value == 5 and self.computer_value == 4:
            return "Lizard poisons Spock! You lose!"
        elif self.user_value == 1 and self.computer_value == 5:
            return "Spock blasts rock! You lose!"
        elif self.user_value == 3 and self.computer_value == 5:
            return "Spock vaporizes scissors! You lose!"
        elif self.user_value == 3 and self.computer_value == 1:
            return "Rock smashes scissors! You lose!"
