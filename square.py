import turtle

# creating canvas
turtle.Screen().bgcolor("orange")

sc=turtle.Screen()
sc.setup(400,300)

turtle.title("welcome to the turtle window")

# turtle object creating
board=turtle.Turtle()

# creating a square
for i in range(4):
        board.forward(100)
        board.left(90)
        i=i+1