import turtle
import random
score =0
lives=3

wn=turtle.Screen()
wn.title("falling skies by kpd")
wn.bgcolor("green")
wn.bgpic("background.gif")
wn.setup(width=800,height=600)
wn.tracer(0)

wn.register_shape("d.gif")
wn.register_shape("mango.gif")
wn.register_shape("k.gif")


# add the players
player = turtle.Turtle()
player.speed(0)
player.penup()
player.shape("d.gif")
player.color("white")
player.goto(0, -250)

player.direction = "stop"
#create list of good guys
good_guys= []

# add the good-guy
for i in range(10):
    good_guy = turtle.Turtle()
    good_guy.speed(0)
    good_guy.penup()
    good_guy.shape("mango.gif")
    good_guy.color("blue")
    good_guy.goto(-110, 250)
    good_guy.speed=random.randint(1,4)
    good_guys.append(good_guy)
#create a bad guys
bad_guys= []

# add the bad-guy
for i in range(5):
    bad_guy = turtle.Turtle()
    bad_guy.speed(0)
    bad_guy.penup()
    bad_guy.shape("k.gif")
    bad_guy.color("red")
    bad_guy.goto(110, 250)
    bad_guy.speed=random.randint(1,4)
    bad_guys.append(bad_guy)



#make pens
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.penup()
pen.shape("square")
pen.color("white")
pen.goto(0, 260)
font=("courier", 24,"normal")
pen.write("score : {} Lives: {}".format(score,lives),align="center",font=font)

player.direction = "stop"
# Functions 
def go_left():
    player.direction="left"

def go_right():
    player.direction="right"

#keyboard bindings

wn.listen()
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")


#main game loop
while True:
    
    wn.update()
    
     
    #move the players
    if player.direction=="left":
        x = player.xcor()
        x-=0.9
        player.setx(x)
    if player.direction=="right":
        x = player.xcor()
        x+=0.9
        player.setx(x)
        
    #moving good guy
    for good_guy in good_guys:
        y=good_guy.ycor()
        y-=good_guy.speed
        good_guy.sety(y) 
        
        #check for off the screen
        if y<-300:
            x = random.randint(-380,380)
            y = random.randint(300,400)
            good_guy.goto(x,y)
            
        #check for the collisions with playe
        
        if good_guy.distance(player) < 20:
            x = random.randint(-380,380)
            y = random.randint(300,400)
            
            good_guy.goto(x,y)
            score+=20
            pen.clear()
            pen.write("score : {} Lives: {}".format(score,lives),align="center",font=font)

            
            
            #moving bad guy
    for bad_guy in bad_guys:
        y=bad_guy.ycor()
        y-=bad_guy.speed
        bad_guy.sety(y) 
        
        #check for off the screen
        if y<-300:
            x = random.randint(-380,380)
            y = random.randint(300,400)
            bad_guy.goto(x,y)
            
        #check for the collisions with playe
        
        if bad_guy.distance(player) < 20:
            x = random.randint(-380,380)
            y = random.randint(300,400)
            
            bad_guy.goto(x,y)
            score-=20
            lives-= 1
            pen.clear()
            pen.write("score : {} Lives: {}".format(score,lives),align="center",font=font)

        if lives==0:
            font=("courier", 24,"normal")
            pen.write("over")

















wn.mainloop()