import turtle
turtle.shape('turtle')
finn = turtle.clone()
finn.shape('square')
finn.pendown()
finn.forward(100)
finn.right(90)
finn.forward(100)
finn.right(90)
finn.forward(100)
finn.right(90)
finn.forward(100)
finn.pendown()


charlie = turtle.Turtle()
charlie.shape('triangle')
charlie.right(45)
charlie.forward(100)
charlie.right(90)
charlie.forward(100)
charlie.right(135)
charlie.forward(150)


turtle.mainloop()
