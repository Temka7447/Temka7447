
import turtle
import time
import random
import pygame
from snakemod import head, segment

heart = 4
hearts = []
# sctxt=turtle.Turtle()
# sctxt.speed(0)
# sctxt.color("black")
# sctxt.up()
# sctxt.goto(-100, 255)
# sctxt.hideturtle()
pygame.mixer.init()

hit_sound = pygame.mixer.Sound(r"C:\Users\dell\Music\Score - Sound Effect for editing VDownloader.mp3")
game_over_sound = pygame.mixer.Sound(r"C:\Users\dell\Music\game over.mp3")
eat_sound = pygame.mixer.Sound(r"C:\Users\dell\Music\eat.mp3")
background_music = pygame.mixer.Sound(r"C:\Users\dell\Music\Relax With Pusheen - calming music 10 minute break VDownloader.mp3")
losingHe = pygame.mixer.Sound(r"C:\Users\dell\Music\Losing sound effect VDownloader.mp3")

heart_tur1 = turtle.Turtle()
heart_tur1.speed(0)
heart_tur1.color("red")
heart_tur1.shape("circle")
heart_tur1.width(20)
heart_tur1.up()
heart_tur1.goto(-40, -270)

heart_tur2 = turtle.Turtle()
heart_tur2.speed(0)
heart_tur2.color("red")
heart_tur2.shape("circle")
heart_tur2.width(20)
heart_tur2.up()
heart_tur2.goto(0, -270)

heart_tur3 = turtle.Turtle()
heart_tur3.speed(0)
heart_tur3.color("red")
heart_tur3.shape("circle")
heart_tur3.width(20)
heart_tur3.up()
heart_tur3.goto(40, -270)


def set_background(image):
    turtle.bgpic(image)

set_background(r"C:\Users\dell\OneDrive\Documents\Python codes\Suhee snake\snwallpapers.png")

def highscore():
    with open("high1.txt", "r") as f:
        scores = f.readlines()
        high = 0
        for score in scores:
            current_score = int(score)
            if current_score > high:
                high = current_score
    return high

levels = 1
score = 0
high_score = highscore()
segments = []
roughs = []
delay = 0.1

level = turtle.Turtle()
level.speed(0)
level.color("black")
level.up()
level.goto(-100, 255)
level.down()
level.write(f"level{levels}", font=("bold", 30))
level.hideturtle()

win = turtle.Screen()
win.title('Snake Game')
win.bgcolor('black')
win.setup(width=600, height=600)
win.colormode(255)
win.tracer(0)

draw = turtle.Turtle()
draw.color("black")
draw.speed(0)
draw.up()
draw.goto(-250, 250)
draw.setheading(0)
draw.down()

for x in range(4):
    draw.width(3)
    draw.forward(500)
    draw.right(90)
draw.hideturtle()

draw1 = turtle.Turtle()
draw1.color("black")
draw1.speed(0)
draw1.up()
draw1.goto(-280, 255)
draw1.down()
draw1.write("Score: 0", font=("bold", 30))
draw1.hideturtle()

txt = turtle.Turtle()
txt.speed(0)
txt.color("black")
txt.up()
txt.goto(30, 255)
txt.down()
txt.write(f"High Score: {high_score}", font=("bold", 30))
txt.hideturtle()

txthea = turtle.Turtle()
txthea.speed(0)
txthea.color("black")
txthea.up()
txthea.goto(-160, -280)
txthea.down()
txthea.write(f"Your hearts: ", font=("bold", 15))
txthea.hideturtle()

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def go_left():
    if head.direction != "right":
        head.direction = "left"

rough = turtle.Turtle()
rough.speed(0)
rough.shape("square")
rough.color("red")
rough.penup()
rough.hideturtle()

def make_rough(food_x, food_y):
    global roughs

    rough_count = 1
    for _ in range(rough_count):
        rough = turtle.Turtle()
        rough.speed(0)
        rough.shape("square")
        rough.color("red")
        rough.penup()
        
        rough.goto(random.randrange(food_x - 40, food_x + 40, 20), 
                   random.randrange(food_y - 40, food_y + 40, 20))
        if rough.xcor() != 0 and rough.ycor() != 0:
            roughs.append(rough)

make_rough(0, 0)

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
        if y > 220:
            head.sety(-240)
    elif head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
        if y < -220:
            head.sety(240)
    elif head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
        if x > 220:
            head.setx(-240)
    elif head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
        if x < -220:
            head.setx(240)

def food_time():
    segment.color("yellow")
    segment.shape("turtle")
    segment.hideturtle()
    x = random.randrange(-240, 240, 20)
    y = random.randrange(-240, 240, 20)
    segment.goto(x, y)
    segment.showturtle()
    win.ontimer(food_time, 4500)

win.onkeypress(go_up, "Up")
win.onkeypress(go_down, "Down")
win.onkeypress(go_right, "Right")
win.onkeypress(go_left, "Left")
win.listen()

def update_score():
    draw1.clear()
    draw1.write(f"Score: {score}", font=("bold", 30))
    txt.clear()
    txt.write(f"High Score: {high_score}", font=("bold", 30))
    # sctxt.clear() 
    # sctxt.up()
    # sctxt.down()
    # sctxt.goto(head.xcor() - 10, head.ycor() + 15)  
    # sctxt.write(str(score), font=("bold", 20)) 

food_time()

def check_collision():
    global heart
    for segment in segments:
        if head.distance(segment) < 20:
            hit_sound.play()
            heart = heart - 1
            if heart == 0:
                losingHe.play()
                return True
            elif heart == 3:
                heart_tur3.color("grey")
                losingHe.play()
            elif heart == 2:
                heart_tur2.color("grey")
                losingHe.play()
            elif heart == 1:
                heart_tur1.color("grey")
                losingHe.play()
    return False

def check_collisionRough():
    global heart
    for rou in roughs:
        if head.distance(rou) < 20:
            hit_sound.play()
            heart = heart - 1
            if heart == 0:
                losingHe.play()
                return True
            elif heart == 3:
                heart_tur3.color("grey")
                losingHe.play()
            elif heart == 2:
                heart_tur2.color("grey")
                losingHe.play()
            elif heart == 1:
                heart_tur1.color("grey")
                losingHe.play()
    return False

def update_roughs():
    global roughs
    for rough in roughs:
        rough.goto(random.randrange(-240, 240, 20), random.randrange(-240, 240, 20))

def game_loop():
    global delay, score, high_score, levels

    while True:
        win.update()

        if head.xcor() > 240:
            head.goto(-240, head.ycor())
        elif head.xcor() < -240:
            head.goto(240, head.ycor())
        elif head.ycor() > 240:
            head.goto(head.xcor(), -240)
        elif head.ycor() < -240:
            head.goto(head.xcor(), 240)
            continue

        if head.distance(segment) < 20:
            eat_sound.play()
            segment.hideturtle()
            x = random.randint(-220, 220)
            y = random.randint(-220, 220)
            segment.goto(x, y)
            make_rough(x, y)

            if len(segments) % 2 == 0:
                new_body = turtle.Turtle()
                new_body.speed(0)
                new_body.shape("square")
                new_body.color("#42c8f5")
                new_body.penup()
                segments.append(new_body)
            else:
                new_body = turtle.Turtle()
                new_body.speed(0)
                new_body.shape("square")
                new_body.color("#4275f5")
                new_body.penup()
                segments.append(new_body)

            score += 1
            if score > high_score:
                high_score = score
                update_score()
                draw1.clear()
                draw1.write(f"Score: {score}", font=("bold", 30))
                txt.clear()
                txt.write(f"High Score: {high_score}", font=("bold", 30))
                level.clear()
                level.write(f"level{levels}", font=("bold", 30))
            else:
                update_score()
                draw1.clear()
                draw1.write(f"Score: {score}", font=("bold", 30))
                level.clear()
                level.write(f"level{levels}", font=("bold", 30))

            if score % 5 == 0:
                delay -= 0.01
                levels += 1
                update_roughs()

            if score % 1 == 0:
                update_roughs()

        for i in range(len(segments) - 1, 0, -1):
            x = segments[i - 1].xcor()
            y = segments[i - 1].ycor()
            segments[i].goto(x, y)

        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x, y)

        move()

        if check_collision() or check_collisionRough():
            game_over_sound.play()
            background_music.stop()
            break

        time.sleep(delay)
    game_over = turtle.Turtle()
    game_over.speed(0)
    game_over.color("black")
    game_over.up()
    game_over.hideturtle()
    game_over.write("GAME OVER!!!", align="center", font=("Arial", 40, "normal"))

    with open("high1.txt", "a") as f:
        f.write(f"{str(high_score)}\n")

    f.close()

    turtle.mainloop()

background_music.play(-1)  

game_loop()