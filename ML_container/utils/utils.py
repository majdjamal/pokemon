
import matplotlib.pyplot as plt
import numpy as np

def plotter(DATA_MTX:  np.ndarray, reduced_mtx: np.ndarray, names: dict = None) -> None:
    """
    :param DATA_MTX: Dataset of pokemons, in shape (Npts, Nattributes)
    :param reduced_mtx: Dimensionality reduced Pokemon Dataset stored in shape (Npts, 2)
    :param names: Names of each pokemon given the row index in DATA_MTX. Example, row 1 in DATA_MTX corresponds to alias names[0]. If nothing is passed, the plotter will not annotate data points.
    """

    for i, X in enumerate(reduced_mtx.T):

        x = X[0]
        y = X[1]

        hp = DATA_MTX[i][3]

        if hp <= 25:
            clr = 'grey'
        elif hp > 25 and hp <= 50:
            clr = 'yellow'
        elif hp > 50 and hp <= 80:
            clr = 'orange'
        elif hp > 80 and hp <= 110:
            clr = 'red'
        elif hp > 110:
            clr = 'purple'

        plt.scatter(x, y, color = clr, alpha=0.7)

        if names:

            name = names[i + 1]
            plt.annotate(name, (x, y))

    plt.tick_params(labelleft=False, labelbottom=False, labelright=False, labeltop=False)
    plt.show()

