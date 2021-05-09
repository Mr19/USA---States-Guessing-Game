import turtle
import pandas
import time

screen = turtle.Screen()
screen.title("USA - States Guessing Game")
image_file = "blank_states_img.gif"
screen.setup(width=725, height=491)
screen.addshape(image_file)
turtle.shape(image_file)

states_data = pandas.read_csv("50_states.csv")
states = states_data.state.to_list()
player_correct_guesses = []

while len(player_correct_guesses) <= 50:

    if len(player_correct_guesses) == 50:
        marker = turtle.Turtle()
        marker.hideturtle()
        marker.penup()
        screen.clear()
        marker.goto(-60, 0)
        marker.write("Congrats!!!", font=("Arial", 20, "bold"))
        time.sleep(3)
        break
    else:
        player_guess = screen.textinput(title=f"{len(player_correct_guesses)}/50 States Correct",
                                        prompt="Enter a state's name or Type 'Exit' to end Game").title()

        if player_guess == "Exit":
            for state in player_correct_guesses:
                states.remove(state)
            missing_states_df = pandas.DataFrame(states)
            missing_states_df.to_csv("Missing_States_learn.csv")
            break

        if player_guess in states and player_guess not in player_correct_guesses:
            marker = turtle.Turtle()
            marker.hideturtle()
            marker.penup()
            x_cor = int(states_data[states_data.state == player_guess].x)
            y_cor = int(states_data[states_data.state == player_guess].y)
            marker.goto(x_cor, y_cor)
            marker.write(player_guess)
            player_correct_guesses.append(player_guess)

