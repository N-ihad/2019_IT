import numpy as np
import matplotlib.pyplot as plt


def calculateAlpha(dimension):
    ar = np.arange(dimension + 1, dtype=int)
    result = ar * 2 * np.pi / dimension
    return result


def draw(dimension, const, pareto_lines, alpha):
    _, axis = plt.subplots(1, 1, subplot_kw=dict(polar=True))
    axis.set_rmax(const)
    axis.set_thetagrids(np.arange(0, 360, 360 / dimension), labels=(np.arange(dimension) + 1))
    axis.grid(True)
    for line in pareto_lines:
        axis.plot(alpha, line)
    plt.show()


def pareto(const, dimension, amountOfDots):
    buff = True
    pareto_dots = []
    dots = np.trunc(np.random.rand(amountOfDots, dimension) * const)

    for ind in range(dots.shape[0]):
        for i, line in enumerate(dots):
            if i != ind and np.all(dots[ind, :] <= line):
                buff = False
                break
        if buff:
            pareto_dots.append(ind)
        buff = True

    dots = np.append(dots, np.reshape(dots[:, 0], (amountOfDots, 1)), axis=1)
    pareto_lines = dots[pareto_dots, :]
    alpha = calculateAlpha(dimension)
    draw(dimension, const, pareto_lines, alpha)


if __name__ == "__main__":
    pareto(10, 3, 10)