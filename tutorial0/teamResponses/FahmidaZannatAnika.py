import turtle

print("Hello World!")

turtle.setup(1.0,1.0)
pen = turtle.Turtle()

def eye(color, radian):
	pen.down()
	pen.fillcolor(color)
	pen.begin_fill()
	pen.circle(radian)
	pen.end_fill()
	pen.up()

pen.fillcolor('yellow')
pen.begin_fill()
pen.circle(60)
pen.end_fill()
pen.up()

pen.goto(-25, 60)
eye('black', 3)
pen.goto(25, 60)
eye('black', 3)

pen.goto(-35, 40)
pen.down()
pen.right(80)
pen.circle(35, 160)
pen.up()
pen.hideturtle()

pen.goto(0, -50)
pen.write("Hello, Insight Team!", font=("Callibri", 12 ),align="center")
pen.goto(0, -80)
pen.write("From, Assassination Classroom", font=("Callibri", 10 ),align="left")
pen.up()
pen.hideturtle()
