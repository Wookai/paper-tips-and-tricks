---
layout: page
shorttitle: Figures
title: Creating quality figures
order: 5
---

Figures are a very important part of a majority of papers: they are your way of communicating your results.
You should always think about what you are trying to say with each figure, and make sure that there is just enough information to support your message, not more.
For example, if you want to show patterns in 2d points (there are two clusters well separated), maybe it is not necessary to put ticks and values on the axes (the scale does not really matter)?
Figures should also not be too complex: it is better to have several figures conveying each one or two messages (method A is better than B, but converges slower) than one big messy figure.

## One script per data-driven figure

Some figures are hand-made, e.g., to explain a system or give a global picture, whereas others are data-driven, i.e., illustrate some data.
These data-driven figures should be scripted as much as possible: ideally, if your data changes, you should only have to run a script once to update your figure, without any other intervention (setting the view, zooming, saving/cropping the figure, etc).
Similarly, if the data required to generate a figure takes more than seconds to be produced, you should have a first script that computes and saves the data, and a second script that plots it.
This way, you will save a lot of time when working on the plot: you won't have to wait after each small change to the figure to see its effect.

We also recommend to save the command used to generate a figure in the LaTeX file, for example as a comment above the figure, especially if the script requires arguments.

{% highlight latex %}
\documentclass{article}

\usepackage{graphicx}

\begin{document}

% python figure_example.py --save ../../examples/figure/figure.eps
\begin{figure}
	\centering
	\includegraphics{figure.eps}
	\caption{Example of a sigmoid function}
\end{figure}

\end{document}
{% endhighlight %}

## Python helper script

If possible, all figures should use the same fonts for their labels, axes, etc.
In particular, you should not have one figure with big labels/ticks, and another with smaller ones.
One solution to achieve this is to define the size of your figure in the script that generates it, and not rescale it in your document (e.g., do not change set the width of the figure to `\textwidth` in your LaTeX document).

To have consistent figures, we recommend using a helper script, similar to our [`plot_utils.py`](https://github.com/Wookai/paper-tips-and-tricks/blob/master/src/python/plot_utils.py).
Using this script, you simply have to call the `figure_setup()` function to define all the sizes, then create a figure of the size you want, and save it.

{% highlight python %}
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
{% endhighlight %}

## Figures format

We recommend saving all figures in the `EPS` format.
This way, you can use both `latex` and `pdflatex` to generate your documents, and enjoy beautiful vector graphics and texts.

As of September 2015, on Mac OS X and with up-to-date versions of Python, Matplotlib and TeX Live, there is a loss of quality when printing figures that were directly saved as `PDF` from Matplotlib.
It becomes clearly when printed on real paper; try it out for yourself.
This is another reason to prefer saving Matplotlib-generated pictures in `EPS`.
If you really want to keep only a PDF version of the figure, use the `epspdf` command line tool---the resulting PDF will be better than that directly produced by Matplotlib.

For completeness, note that there is another Matplotlib backend, [PGF](http://matplotlib.org/users/pgf.html), that produces slightly superior results.
However, as of September 2015, the resulting PDFs are twice as heavy as those obtained with the default backend and `epspdf`.

Matplotlib, even when using [tight layout features](http://matplotlib.org/users/tight_layout_guide.html), adds at times too much white space in the margins.
A nifty command-line tool to crop a PDF to its tightest bounding box `pdfcrop`.

## Rasterize parts of the figure

If you have many data points in your plot, the resulting EPS file might be very big.
You could save your figure as a PNG file, but this would result in blurry texts.
The solution is to rasterize parts of your figure, i.e., to tell `matplotlib` that the data points have to be rendered as a bitmap in the EPS file, while the rests is in vector format.

You can pass the `rasterized=True` keyword to most plotting fuctions in `matplotlib`.
You can also tell use different layers using the `zorder` and tell `matplotlib` to rasterize all the layers below a given `zorder` using the `set_rasterization_zorder()` method of the axis.
See [figure_rasterized_example.py](https://github.com/Wookai/paper-tips-and-tricks/blob/master/src/python/figure_rasterized_example.py) and [matplotlib.org/examples/misc/rasterization_demo.html](http://matplotlib.org/examples/misc/rasterization_demo.html) for examples of rasterization.


