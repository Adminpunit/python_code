    import turtle

    # Set up the screen
    screen = turtle.Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0) # Turn off screen updates for smoother animation

    # Create a turtle to represent the reptile
    reptile = turtle.Turtle()
    reptile.shape("circle") # You can use a custom shape or image later
    reptile.color("green")
    reptile.penup()

    def move_reptile(x, y):
        reptile.goto(x, y)
        screen.update() # Update the screen after moving

    screen.onclick(move_reptile) # Move reptile on click
    screen.onmousemove(move_reptile) # Move reptile with mouse movement (requires screen.listen())
    screen.listen()

    turtle.done()