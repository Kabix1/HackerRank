from skopt.space import Real
from skopt.utils import use_named_args
from skopt import gp_minimize
from Strategies import closest_prio4
from test import generate_board, try_strategy

space = [
    Real(0, 1, name="A"),
    Real(0, 1, name="B"),
    Real(0, 10, name="C"),
    Real(0, 10, name="D")
]


@use_named_args(space)
def objective(**params):
    closest_prio4.A = params["A"]
    closest_prio4.B = params["B"]
    closest_prio4.C = params["C"]
    closest_prio4.D = params["D"]
    num_tries = 200
    steps = 0
    for _ in range(num_tries):
        pos, board = generate_board()
        steps += try_strategy(closest_prio4, pos, board)
    return steps / num_tries


res_gp = gp_minimize(objective,
                     space,
                     n_calls=100,
                     random_state=0,
                     verbose=True,
                     n_jobs=6,
                     acq_optimizer="lbfgs")
print(res_gp.x)
