import turtle
import pandas

screen = turtle.Screen()
screen.title("Canada Map Game")

map_image = "map.gif"
screen.addshape(map_image)
turtle.shape(map_image)

map_data = pandas.read_csv('map.csv')
all_provinces = map_data.province.to_list()
# def get_mouse_click_cor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_cor)

game_is_on = True
counter = 0

while game_is_on:

    answer = screen.textinput(title=f"{counter} / 13 guessed correctly", prompt="Name the next Province or Territory:")

    if answer.upper() == "EXIT":
        break
    elif answer.upper() in all_provinces:
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        province_row = map_data[answer.upper() == map_data.province]
        t.goto(int(province_row.x), int(province_row.y))
        t.write(answer.upper(), "center")
        counter += 1

