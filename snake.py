import turtle
import time
import random



#initilization starts here
delay = 0.1

#set up the screen/background
wn = turtle.Screen()
wn.title("Snake Game Version 1")
wn.bgcolor("green")
wn.setup(width=600, height=800)
wn.tracer(0)
 

#initializing snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()# make sure there is no drawing
head.goto(0,0) #start at centre
head.direction = "stop"

#snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

#snake body
segments = []

score = 0
high_score = 0

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,265)
pen.clear()
pen.write("Score: {} High Score: {}".format(score, high_score), align="center", 
font=("Courier", 24, "normal"))


start_menu = turtle.Turtle()
start_menu.speed(0)
start_menu.shape("square")
start_menu.color("white")
start_menu.penup()
start_menu.hideturtle()
start_menu.goto(0,-100)

#initialization done
#helper functions
def up():
    if head.direction != "down":
        head.direction = "up"
def down():
    if head.direction != "up":
        head.direction = "down"
def left():
    if head.direction != "right":    
        head.direction = "left"
def right():
    if head.direction != "left":
        head.direction = "right"
def move():
    if head.direction == "up":
        y = head.ycor() 
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor() 
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor() 
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor() 
        head.setx(x + 20)
def score_print():
    pen.clear()
    pen.write("Score: {} High Score: {}".format(score, high_score), align="center", 
        font=("Courier", 24, "normal"))
def dead_message():
    pen.clear()
    pen.write("You died!! We will restart", align="center", 
            font=("Courier", 18, "normal"))
def start_message():
    start_menu.goto(0,-100)
    start_menu.write("Welcome to SNAKE!", align="center", font=("Courier", 22, "normal"))
    start_menu.goto(0,-150)
    start_menu.write("use \"W\",\"S\",\"A\",\"D\" to control the snake", align="center", font=("Courier", 15, "normal"))

#function ends here




# keyboard bindings
wn.listen()
wn.onkeypress(up, "w")
wn.onkeypress(down, "s")
wn.onkeypress(left, "a")
wn.onkeypress(right, "d")


# Main game loop
while True:
    wn.update()
    start_menu.clear()
    if head.direction == "stop":
        start_message()
    #check collision with boarder
    if head.xcor() > 295 or head.xcor() < -295 or head.ycor() > 295 or head.ycor() < -295:
        dead_message()
        time.sleep(2)
        head.goto(0,0)
        head.direction = "stop"
        
        
        for i in segments:
            i.goto(1000,1000) #deleting all the body segments
        segments.clear()
        score = 0
        score_print()

    #check collision with body
    for i in segments:
        if i.distance(head) < 20 :
            
            dead_message()
            time.sleep(2)
            head.goto(0,0)
            head.direction = "stop"
            for i in segments:
                i.goto(1000,1000)
            segments.clear()
            score = 0
            
            score_print()

    if head.distance(food) < 20:
        #move food
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)
        score += 10
        if score > high_score:
            high_score = score
        
        score_print()

        #add new body segment
        new_seg = turtle.Turtle()
        new_seg.speed(0)
        new_seg.shape("square")
        new_seg.color("grey")
        new_seg.penup()
        segments.append(new_seg)
    
    #move body with head
    for i in range(len(segments)-1, 0, -1):
        segments[i].goto(segments[i-1].xcor(), segments[i-1].ycor())
    if (len(segments) > 0):
        segments[0].goto(head.xcor(), head.ycor())
    move()

    time.sleep(delay)
wn.mainloop()