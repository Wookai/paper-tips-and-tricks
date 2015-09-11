import argparse
import matplotlib.pyplot as plt
import numpy as np
import plot_utils as pu


def main(args):
    x = np.linspace(-6, 6, 200)
    y = 1/(1 + np.exp(-x))

    pu.figure_setup()

    fig_size = pu.get_fig_size(10, 5)
    fig = plt.figure(figsize=fig_size)
    ax = fig.add_subplot(111)

    ax.plot(x, y, c='b', lw=pu.plot_lw())

    ax.set_xlabel('$x$')
    ax.set_ylabel('$\\sigma(x)$')

    ax.set_axisbelow(True)

    plt.grid()
    plt.tight_layout()

    if args.save:
        pu.save_fig(fig, args.save)
    else:
        plt.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-s', '--save')

    args = parser.parse_args()
    main(args)
