import turtle

# creating canvas
turtle.Screen().bgcolor("Orange")

sc=turtle.Screen()
sc.setup(400,300)

turtle.title("welcome to the turtle window")

# turtle object creating
board=turtle.Turtle()

# creating a square
for i in range(5):
        board.forward(100)
        board.left(144)
        i=i+1