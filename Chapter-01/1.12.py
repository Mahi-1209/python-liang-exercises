import turtle as t

# Draw outer square
t.penup()
t.goto(-50, 50)
t.pendown()

for _ in range(4):
    t.forward(100)
    t.right(90)

# Draw vertical line
t.penup()
t.goto(0, 50)
t.pendown()
t.goto(0, -50)

# Draw horizontal line
t.penup()
t.goto(-50, 0)
t.pendown()
t.goto(50, 0)

t.done()