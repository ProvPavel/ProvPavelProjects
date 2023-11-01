import numpy as np


def gradient_descent(func, start_point, gamma, epsilon, steps):
    hist = np.array([[0.1], [start_point]])
    if steps:
        for i in range(steps):
            x_curr = hist[-1]
            x_next = step(x_curr, gamma, func)
            hist = np.append(hist, x_next)
    else:
        while True:
            x_curr = hist[-1]
            x_next = step(x_curr, gamma, func)
            hist = np.append(hist, [x_next])
            if abs(func(hist[-1]) - func(hist[-2])) < epsilon:
                break
    hist = np.array([[float(format(q, '.3f'))] for q in list(hist[1::])])
    return hist


def grad(x, func):
    return (func(x + 10 ** -9) - func(x)) / (10 ** -9)


def step(x, lr, func):
    return x - lr * grad(x, func)


def f5_x(x: float) -> float:
    return (15 * x ** 8 + 24 * x ** 5 - 75 * x ** 4 + 135 * x ** 2 - 400 * x ** 3 + 10 * x + 30) / 100


func = f5_x
start_point = 4
gamma = 0.1
epsilon = 0.05
steps = 10

print(gradient_descent(func, start_point, gamma, epsilon, steps))