---
layout: page
shorttitle: Equations
title: Mathematical notation
order: 2
---

[(complete example)](https://github.com/Wookai/paper-tips-and-tricks/tree/master/examples/notation)

When writing equations, it is helpful to have a coherent and consistent way of writing variables, vectors, matrices, etc.
It helps the reader identifying what you are talking about and remembering the semantics of each symbol.

## Notation

We propose the following rules for writing math:

 * lowercase italic for variables: *x* (`$x$`)
 * lowercase italic bold for vectors: **_x_** (`$\mathbold{x}$`)
 * uppercase italic bold for matrices: **_X_** (`$\mathbold{X}$`)
 * uppercase italic for random variables: *X* (`$X$`)

The `\mathbold` command comes from the [`fixmath`](https://www.ctan.org/pkg/fixmath) package and is similar to `\boldmath` or `\bm`, except that all symbols are in italics, event greek letters (other packages do not italicize greek letters).

When adding indices or exponents to variables, make sure that you add them outside of the styling of the variable, i.e., write `$\mathbold{x}_i$` and not `$\mathbold{x_i}$`.

### Define custom commands

Because we often refer to variables, we suggest defining the following two commands:

{% highlight latex %}
\renewcommand{\vec}[1]{\mathbold{#1}}
\newcommand{\mat}[1]{\mathbold{#1}}
{% endhighlight %}

You can then use `$\vec{x}$` and `$\mat{X}$` in your document.
If you decide to change the way you want to format matrices, you simply have to change the `\mat` command, and it will update the whole document.

We also suggest defining commands for the variables you use the most.
For example, if you use `\vec{x}` and `\mat{X}` a lot, consider defining these commands:

{% highlight latex %}
\newcommand{\vx}{\vec{x}}
\newcommand{\vX}{\mat{X}}
{% endhighlight %}

You can then write more compact equations: `$\vx^T \vy = \vZ$`.

### Use the correct notation for columns et elements

Note that you should always style the variables with respect to their type.
For example, the *i*th element of a vector `\vx` is `x_i` and not `\vx_i` (it is a number).
Similarly, if you have a matrix `\vX`, its *i*th column is `\vx_i`, and not `\vX_i` (it is a vector, thus in bold), and one of its element is `x_{ij}`, and not `\vX_{ij}`.

## Environments

Use `\(...\)` to write inline equations.
You can also use `$...$`, but it is a TeX command and gives more obscure error messages.

To write centered equations on their own lines, do not `$$...$$` (it is one of the [deadly sins of LaTeX use](http://www.pirbot.com/mirrors/ctan/info/l2tabu/english/l2tabuen.pdf)).
It works, but gives wrong spacing.
Use `\begin{equation}` or `\begin{align}` instead.
n essential guide to LaTeX 2e usage: http://www.pirbot.com/mirrors/ctan/info/l2tabu/english/l2tabuen.pdf
