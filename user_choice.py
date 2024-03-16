class UserChoice():
    def __init__ (self):
        self.name = "Unknown"
        self.value = 0
    def get_value(self):
        print ("Rock (1), Paper (2), Scissors (3), Lizard (4), Spock (5)")
        self.value = int(input())
        return self.value
    def get_name(self):
        if self.value == 1:
          self.name = "rock"
          return self.name
        if self.value == 2:
          self.name = "paper"
          return self.name
        if self.value == 3:
          self.name = "scissors"
          return self.name
        if self.value == 4:
          self.name = "lizard"
          return self.name
        if self.value == 5:
          self.name = "spock"
          return self.name
