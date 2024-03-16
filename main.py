import user_choice
import computer_choice
import play

user_input = user_choice.UserChoice()
user_value = user_input.get_value()
computer_input = computer_choice.ComputerChoice()
computer_value = computer_input.get_value()
run = play.Play()
run.computer_value = computer_value
run.user_value = user_value
final = run.run_game()
print(final)
