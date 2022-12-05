
import turtle
import winsound

wnd = turtle.Screen()   #wnindow
wnd.title("Pong: The Game")
wnd.bgcolor("black")
wnd.setup(width = 800,height= 600)
wnd.tracer(0)           #stops window from updating, prevents lagging, speeds ot up

#score
score_a = 0
score_b = 0






#  paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid= 5, stretch_len= 1)
paddle_a.penup()
paddle_a.goto(-350,0)




#  paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid= 5, stretch_len= 1)
paddle_b.penup()
paddle_b.goto(350,0)



#  ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")

ball.penup()
ball.goto(0,0)
ball.dx = 0.5  #move 2 pixel in x direction
ball.dy = 0.5 #move 2 pixel in y direction

# Pen 
pen = turtle.Turtle()
pen.speed(0)
pen.color('pink')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write('Player A :0  Player B: 0', align = 'center', font = ('Courier', 24,"normal"))

# Function
#move the paddles
# paddle_a
def paddle_a_up():
   y = paddle_a.ycor()  #get the y cordinate
   y+= 20                #add 20 to y cordinate
   paddle_a.sety(y)      #set to new y coordinate

def paddle_a_down():
 y = paddle_a.ycor()  #get the y cordinate
 y-= 20                #sub 20 to y cordinate
 paddle_a.sety(y)      #set to new y coordinate

# paddle_b
def paddle_b_up():
   y = paddle_b.ycor()  #get the y cordinate
   y+= 20                #add 20 to y cordinate
   paddle_b.sety(y)      #set to new y coordinate

def paddle_b_down():
 y = paddle_b.ycor()  #get the y cordinate
 y-= 20                #sub 20 to y cordinate
 paddle_b.sety(y)      #set to new y coordinate

# keyboeard binding
wnd.listen()   #listen for keyboard input
wnd.onkeypress(paddle_a_up,"w")       # window keyboard se input legii, paddle_a_up function chlega aur hr press se 20 pixel upr jayega padel
wnd.onkeypress(paddle_a_down,"s")
wnd.onkeypress(paddle_b_up,"Up")
wnd.onkeypress(paddle_b_down,"Down")



#main game loop
while True:
   wnd.update()    # whatever you did to the window got updated so that you can see final results

   #move the ball
   ball.setx(ball.xcor()+ ball.dx)
   ball.sety(ball.ycor()+ball.dy)

   #border checking
   #top and bottom
   if ball.ycor() > 290:
     ball.sety(290)
     ball.dy *= -1
     winsound.PlaySound("SPRTField_Balloon against wall 1 (ID 1825)_BSB.wav",winsound.SND_ASYNC)
   
   if ball.ycor() < -290:
     ball.sety(-290)
     ball.dy *= -1 
     winsound.PlaySound("SPRTField_Balloon against wall 1 (ID 1825)_BSB.wav",winsound.SND_ASYNC)
     
    #left and right
   if ball.xcor() > 390:
     ball.goto(0,0)
     ball.dx *= -1
     score_a += 1
     pen.clear()
     pen.write('Player A :{}  Player B: {}'.format(score_a,score_b), align = 'center', font = ('Courier', 24,"normal"))

   if ball.xcor() < -390:
     ball.goto(0,0)
     ball.dx *= -1
     score_b += 1
     pen.clear()
     pen.write('Player A :{}  Player B: {}'.format(score_a,score_b), align = 'center', font = ('Courier', 24,"normal"))

    # paddle ball collision
   if (ball.xcor() > 340 and ball.xcor() <350) and (ball.ycor() < paddle_b.ycor() +40 and ball.ycor() > paddle_b.ycor() -40  ):
     ball.setx(340)
     ball.dx *= -1
     
   if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() +40 and ball.ycor() > paddle_a.ycor() -40  ):
     ball.setx(-340)
     ball.dx *= -1 
     
   
   





