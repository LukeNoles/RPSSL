import user_choice.UserChoice
import computer_choice.ComputerChoice
import play.Play

user_input = user_choice.UserChoice(int(input("Rock, Paper, Scissors, Lizard, Spock")
computer_input = computer_choice.ComputerChoice.computerchoice()
run = play.Play(user_input, computer_input)
final = run.results
print(final)
