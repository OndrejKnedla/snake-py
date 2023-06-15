import turtle
import texts
from random import randrange
from time import sleep
from sys import exit


# FUNKCE OTÁČENÍ:
"""
FUNKCE OTÁČENÍ zajistí, aby se hlava hada otočila 
požadovaným směrem. Vrací aktualizovanou proměnnou 
snake.direction, ve které je uložen aktuání směř hada.
"""
def move_up():
    if snake.direction == "right":
        snake.left(90)
        snake.direction = "up"
        return snake.direction
    
    elif snake.direction == "left":
        snake.right(90)
        snake.direction = "up"
        return snake.direction

def move_down():
    if snake.direction == "right":
        snake.right(90)
        snake.direction = "down"
        return snake.direction   
      
    elif snake.direction == "left":
        snake.left(90)
        snake.direction = "down"
        return snake.direction
    
def move_left():
    if snake.direction == "up":
        snake.left(90)
        snake.direction = "left"      
        return snake.direction
    
    elif snake.direction == "down":
        snake.right(90)
        snake.direction = "left"      
        return snake.direction

def move_right():
    if snake.direction == "up":
        snake.right(90)
        snake.direction = "right"      
        return snake.direction
    
    elif snake.direction == "down":
        snake.left(90)
        snake.direction = "right"      
        return snake.direction

# DALŠÍ FUNKCE
def random_position():
    """
    Funkce zvolí náhodné souřadnice pro zobrazení
    potravy pro hada.
    """
    x = randrange(-320, 321, 20)
    y = randrange(-220, 161, 20)
    return x, y

def new_body_part():
    """
    Funkce přidá další díl těla hada. Spustí se, 
    pokud had sní jídlo.
    """
    snake_body = turtle.Turtle("square")
    snake_body.speed(0)
    snake_body.penup()
    return snake_body

def level_speed(snake_body_list):
    """
    Funkce vrací označení levlu a rychlost pohybu hada
    podle počtu snědené potravy. Případně spustí funkci 
    "win" pokud hrác vyhrál.
    """
    if snake_body_list == 40:
        win()
    elif snake_body_list > 30:
        return "FINÁLE", 0.05
    elif snake_body_list > 20:
        return "3", 0.1
    elif snake_body_list > 10:
        return "2", 0.2
    elif snake_body_list <= 10:
        return "1", 0.3
    
def game_over():
    """
    Funkce oznámí prohru a ukončí hru. Je spuštěna pokud
    had narazí do hrany pole nebo do svého těla.
    """
    sleep(2)
    text_area.goto(0, -60)
    text_area.color("red")
    text_area.write(texts.loss, move=False, align="center",
                    font=("Geneva", 50, "bold"))
    sleep(5)
    exit()

def win():
    """"
    Funkce oznámí vítězství a ukončí hru. Je spuštěna pokud
    had sní 40 kusů potravy.
    """
    sleep(2)
    text_area.goto(0, -60)
    text_area.color("green")
    text_area.write(texts.win, move=False, align="center",
                    font=("Geneva", 50, "bold"))
    sleep(5)
    exit()

def play():
    """
    Hlavní kód hry.
    """
    # vyčištění hracího pole
    text_area.clear()

    # cyklus pohybu hada
    while True:
        # označení levelu a nastavení rychlosti
        level_text.clear()
        level_and_spead = level_speed(len(snake_body_list))
        level_text.write(f"LEVEL: {level_and_spead[0]}", move=False,
                         align="center", font=("Courier New", 20))
        sleep(level_and_spead[1])

        # pohyb hada
        snake.forward(20)
        display.update()   
        
        # snědení jablka
        if snake.distance(food) < 10:
            food.goto(random_position())
            snake_body_list.append(new_body_part())

        # vykreslení ocásku
        if len(snake_body_list) > 1:
            for index in range(len(snake_body_list)-1, 0, -1):
                snake_body_list[index].goto(snake_body_list[index-1].position())

        if len(snake_body_list) > 0:
            snake_body_list[0].goto(snake.position())
            
        # kontrola kolize z hranou pole
        x = (snake.xcor())
        y = (snake.ycor())
        if (x <= -360 or
            x >= 360 or
            y <= -250 or
            y >= 200):
            game_over()
        
        # kontrola kolize s tělem hada
        for part in snake_body_list[2:]:
            if part.distance(snake) < 20:
                game_over()

# PROMĚNNÉ
snake_body_list = []

# OBRAZOVKA     
display = turtle.Screen()
display.setup(width=800, height=600)
display.title("SNAKE GAME")

# HRACÍ POLE (souřadnice: x = -360 až 360, y = -260 až 200)
playing_area = turtle.Turtle("square")
playing_area.hideturtle()
playing_area.penup()
playing_area.goto(360, 200)
playing_area.left(180)
playing_area.pendown()
playing_area.pensize(2)
playing_area.pencolor("black")
for _ in range(2):
    playing_area.forward(720)
    playing_area.left(90)
    playing_area.forward(460)
    playing_area.left(90)

# dodání funkcí obrazovky
display.listen()
display.onkeypress(move_up, "w")
display.onkeypress(move_down, "s")
display.onkeypress(move_left, "a")
display.onkeypress(move_right, "d")
display.onkeypress(play, "p")
display.tracer(False) 

# UVÍTÁNÍ
text_area = turtle.Turtle()
text_area.penup()
text_area.hideturtle()
text_area.goto(0, -100)
text_area.write(f"{texts.welcome_text}", move=False, align="center",
              font=("Goudy Old Style", 16))

# LEVEL
level_text = turtle.Turtle() 
level_text.penup()
level_text.hideturtle()
level_text.goto(0, 235)

# HAD
snake = turtle.Turtle("triangle")
snake.speed(0)
snake.penup()
snake.direction = "right"

# POTRAVA PRO HADA
food = turtle.Turtle("circle")
food.penup()
food.color("green4")
food.goto(random_position())


display.exitonclick()
