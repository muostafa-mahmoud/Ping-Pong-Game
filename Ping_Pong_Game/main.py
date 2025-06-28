from game.screen import wn
from game.tools import paddle_a, paddle_b, ball, pen, score_a, score_b
from game.controls import setup_controls
from game.logic import update_ball

setup_controls()

while True:
    wn.update()
    update_ball()
