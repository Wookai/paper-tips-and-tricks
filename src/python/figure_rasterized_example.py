import argparse
import matplotlib.pyplot as plt
import numpy as np
import plot_utils as pu


def main(args):
    data = np.random.randn(args.n_points, 2)

    pu.figure_setup()

    fig_size = pu.get_fig_size(10, 10)
    fig = plt.figure(figsize=fig_size)
    ax = fig.add_subplot(111)

    ax.scatter(data[:, 0], data[:, 1], alpha=0.1, rasterized=True)

    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')

    plt.tight_layout()

    if args.save:
        pu.save_fig(fig, args.save)
    else:
        plt.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-n', '--n_points', type=int,
                        default=10000)
    parser.add_argument('-s', '--save')

    args = parser.parse_args()
    main(args)
