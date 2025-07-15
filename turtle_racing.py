from PIL import Image
import turtle
import time
import random

WIDTH, HEIGHT = 1000, 1000
FINISH_LINE = HEIGHT // 2 - 20
COLORS = [
    "red", "blue", "green", "yellow", "orange", "purple", "pink", "brown",
    "black", "gray", "cyan", "magenta", "gold", "silver", "navy", "turquoise",
    "lime", "maroon", "violet"
]

def get_number_of_turtles():
    while True:
        user_input = input ("Enter the number of turtles you wish to race(1-10): ")
        if user_input.isdigit():
            total_no_of_turtle = int(user_input)
            if 1 < total_no_of_turtle < 11:
                break
            else:
                print("Please Nigga!Enter between 0 and 11.")
                Image.open("image.jpeg").show()
                continue
            
        else:
            print("Please enter a number! ")

    return total_no_of_turtle
    
def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("🐢 Turtle Racers 🏁")

def create_racers(colors):
    turtles = []
    spacing = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.shapesize(1.4, 1.4)
        racer.penup()
        racer.left(90) 
        x = (spacing * (i + 1)) - (WIDTH // 2)
        racer.goto(x, -HEIGHT // 2 + 20)
        racer.pendown()
        turtles.append(racer)
    return turtles

# def race(colors):
#     racers = create_racers(colors)
#     while True:
#         for i, racer in enumerate(racers):
#             racer.forward(random.randint(5, 30))
#             if racer.ycor() >= FINISH_LINE:
#                 return i  # Return winner index


def race(colors):
    racers = create_racers(colors)
    winner_not_found = True
    distance=[]
    while winner_not_found:
        for i,racer in enumerate(racers):
            racer.forward(random.randrange(5,40))
            if racer.ycor() >= FINISH_LINE:
                winner_not_found = False
                
            if i == len(racers)-1:
                break

    for racer in racers: 
        distance.append(racer.ycor())
    
    print(distance)
    print(colors)

    return distance.index(max(distance))

def main():
    init_turtle()
    num_racers = get_number_of_turtles()
    random.shuffle(COLORS)
    race_colors = COLORS[:num_racers]
    winner_index = race(race_colors)
    print(f"\n🏆 The winner is the {race_colors[winner_index]} turtle!")
    time.sleep(5)

main()
exit()