import turtle

t = turtle.Turtle()
t.speed(0)

colors = ["red", "blue", "green", "yellow", "purple"]

for i in range(100):
    t.color(colors[i % 5])
    t.forward(i * 3)
    t.right(91)

turtle.done()