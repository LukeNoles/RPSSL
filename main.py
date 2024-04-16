import user_choice
import computer_choice
import play

win_count = 0
lose_count = 0
while True:
    print("Choose your fighter.")
    user_input = user_choice.UserChoice()
    user_value = user_input.get_value()
    print("You picked ", user_value)
    computer_input = computer_choice.ComputerChoice()
    computer_value = computer_input.get_value()
    print("CP picked ", computer_value)
    run = play.Play()
    run.computer_value = computer_value
    run.user_value = user_value
    final = run.run_game()
    if "win" in final:
        win_count = win_count + 1
    if "lose" in final:
        lose_count = lose_count + 1
    print("Wins:", win_count)
    print("losses:", lose_count)
    print(final)
    print("Battle once more?")
    print("Yes (y), No (n)")
    play_again = input()
    if play_again.lower() != "y":
        break