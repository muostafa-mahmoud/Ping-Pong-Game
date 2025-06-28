from game.tools import ball, paddle_a, paddle_b, pen
import game.tools as tools

#Ball movement

def update_ball():
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        tools.score_a += 1
        pen.clear()
        pen.write(f"Player 1 : {tools.score_a} : Player 2 : {tools.score_b}", align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        tools.score_b += 1
        pen.clear()
        pen.write(f"Player 1 : {tools.score_a} : Player 2 : {tools.score_b}", align="center", font=("Courier", 24, "normal"))

    if 340 < ball.xcor() < 350 and paddle_b.ycor() - 50 < ball.ycor() < paddle_b.ycor() + 50:
        ball.setx(340)
        ball.dx *= -1

    if -350 < ball.xcor() < -340 and paddle_a.ycor() - 50 < ball.ycor() < paddle_a.ycor() + 50:
        ball.setx(-340)
        ball.dx *= -1
