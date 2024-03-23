import turtle
from freegames import square, vector

p1xy = vector(-100, 0)
p1aim = vector(4, 0)
p1body = set()

p2xy = vector(100, 0)
p2aim = vector(-4, 0)
p2body = set()


def inside(head):
    """Return True if head inside screen."""
    return -200 < head.x < 200 and -200 < head.y < 200


def draw():
    """Advance players and draw game."""
    p1xy.move(p1aim)
    p1head = p1xy.copy()

    p2xy.move(p2aim)
    p2head = p2xy.copy()

    if not inside(p1head) or p1head in p2body:
        print('Player blue wins!')
        return

    if not inside(p2head) or p2head in p1body:
        print('Player red wins!')
        return

    p1body.add(p1head)
    p2body.add(p2head)

    square(p1xy.x, p1xy.y, 3, 'red')
    square(p2xy.x, p2xy.y, 3, 'blue')
    turtle.update()
    turtle.ontimer(draw, 50)


turtle.setup(420, 420, 370, 0)
turtle.hideturtle()
turtle.tracer(False)
turtle.listen()
turtle.onkey(lambda: p1aim.rotate(90), 'a')
turtle.onkey(lambda: p1aim.rotate(-90), 'd')
turtle.onkey(lambda: p2aim.rotate(90), 'j')
turtle.onkey(lambda: p2aim.rotate(-90), 'l')
draw()
turtle.done()
