class Play():
    def __init__ (self):
        self.user_value = 0
        self.computer_value = 0
    def run_game(self):
        if self.user_value == self.computer_value:
            return "It's a tie!"
        elif self.user_value == 1 and self.computer_value == 3:
            return "You win!"
        elif self.user_value == 1 and self.computer_value == 4:
            return "You win!"
        elif self.user_value == 2 and self.computer_value == 1:
            return "You win!"
        elif self.user_value == 2 and self.computer_value == 5:
            return "You win!"
        elif self.user_value == 3 and self.computer_value == 2:
            return "You win!"
        elif self.user_value == 3 and self.computer_value == 4:
            return "You win!"
        elif self.user_value == 4 and self.computer_value == 2:
            return "You win!"
        elif self.user_value == 4 and self.computer_value == 5:
            return "You win!"
        elif self.user_value == 5 and self.computer_value == 1:
            return "You win!"
        elif self.user_value == 5 and self.computer_value == 3:
            return "You win!"
        else:
            return "You lose!"
