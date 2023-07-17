import turtle

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#pontos
pontos_a = 0
pontos_b = 0

# taco A
taco_a = turtle.Turtle()
taco_a.speed(0)
taco_a.shape("square")
taco_a.color("white")
taco_a.shapesize(stretch_wid=5, stretch_len=1)
taco_a.penup()
taco_a.goto(-350, 0)


# taco B
taco_b = turtle.Turtle()
taco_b.speed(0)
taco_b.shape("square")
taco_b.color("white")
taco_b.shapesize(stretch_wid=5, stretch_len=1)
taco_b.penup()
taco_b.goto(350, 0)

#bola

bola = turtle.Turtle()
bola.speed(0)
bola.shape("square")
bola.color("white")
bola.penup()
bola.goto(0, 0)
bola.dx = 0.2
bola.dy = 0.2

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Jogador A: 0   Jogador B: 0", align="center", font=("Courier", 24, "normal"))

#funções taco A

def mov_a_cima():
    y = taco_a.ycor()
    y += 20
    taco_a.sety(y)

def mov_a_baixo():
    y = taco_a.ycor()
    y -= 20
    taco_a.sety(y)

#função taco B
def mov_b_cima():
    y = taco_b.ycor()
    y += 20
    taco_b.sety(y)

def mov_b_baixo():
    y = taco_b.ycor()
    y -= 20
    taco_b.sety(y)
#função teclado

wn.listen()
wn.onkeypress(mov_a_cima, "w")
wn.onkeypress(mov_a_baixo, "s")

wn.onkeypress(mov_b_cima, "Up")
wn.onkeypress(mov_b_baixo, "Down")


# loop do jogo principal
while True:
    wn.update()

#funções bola
    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)

#checagem de borda
    if bola.ycor() > 290:
        bola.sety(290)
        bola.dy *= -1
    if bola.ycor() < -290:
        bola.sety(-290)
        bola.dy *= -1

    if bola.xcor() > 390:
        bola.goto(0, 0)
        bola.dx *= -1
        pontos_a += 1

    if bola.xcor() < -390:
        bola.goto(0, 0)
        bola.dx *= -1
        pontos_b += 1
    #colisões bola:
    if (bola.xcor() > 340 and bola.xcor() < 350) and (bola.ycor() < taco_b.ycor() + 40 and bola.ycor() > taco_b.ycor() - 50):
        bola.setx(340)
        bola.dx *= -1
        pen.clear()
        pen.write("Jogador A: {}   Jogador B: {}".format(pontos_a, pontos_b), align="center", font=("Courier", 24, "normal"))

    if (bola.xcor() < -340 and bola.xcor() > -350) and  (bola.ycor() < taco_a.ycor() + 40 and bola.ycor() > taco_a.ycor() -50):
        bola.setx(-340)
        bola.dx *= -1
        pen.clear()
        pen.write("Jogador A: {}   Jogador B: {}".format(pontos_a, pontos_b), align="center", font=("Courier", 24, "normal"))
