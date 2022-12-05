import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S State Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)


# def get_mouse_click_coor(x,y):
#    print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
data = pandas.read_csv("50_states.csv")
all_stetes = data.state.to_list()

guess_state = []
while  len(guess_state) < 50 :
    answer_state = screen.textinput(title=f"{len(guess_state)}/50 of States correct", prompt="What another state name ?").title()
    if answer_state == "Exit" :
        missing_State = [state for state in all_stetes if state not in guess_state]
        new_data = pandas.DataFrame(missing_State)
        new_data.to_csv("States_to_lern.csv")
        break
    if answer_state in all_stetes :
        guess_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)


