# Tips and Tricks for Writing Scientific Papers

## What is this?

We gather in this repository at list of tool, best practices, tips and other guidelines we found useful/important when writing scientific papers.
Some are a matter of style (we tend to follow the guidelines of the Chicago Manual of Style), and we are well aware that other people prefer to do differently, but we list them anyway to have a consistent guide.
Feel free to adapt, change, ignore, or even challenge everything we write!

## Typesetting your paper

We list below recommendations related to typesetting your paper.
Some tips are spectific to LaTeX, but others apply regardless of what you are using.

### Capiatlization

We will refer below to two types of capitalization:
* sentence format : The title of the nice book
* title format: The Title of the Nice Book

### Number formatting

Use the [siunitx](https://ctan.org/pkg/siunitx) package to format all numbers.
For example, use `\SI{1234567}{\$}` to produce `$1 234 567`.
You can also use it to round numbers, etc.

### Tables

Use [booktabs](https://www.ctan.org/pkg/booktabs) to typeset your tables.

```
\usepackage{booktabs}
% --
\begin{table}
\centering
\begin{tabular}{ll}
\toprule
Column 1 & Another column \\
\midrule
10 & 95 \\
30 & 49 \\
\bottomrule
\end{tabular}
\caption{My caption.}
\label{tab-label}
\end{table}
```

Column heads should use sentence format capitalization (see http://www.chicagomanualofstyle.org/15/ch13/ch13_sec019.html)

## Useful resources

* Automatically capitalize your title: http://titlecapitalization.com
* Chicago Manual of Style: http://www.chicagomanualofstyle.org
* A small guide to making nice tables: http://www.inf.ethz.ch/personal/markusp/teaching/guides/guide-tables.pdf
* Better table formatting: http://darkhorseanalytics.com/blog/wp-content/uploads/2014/03/ClearOffTheTableMd.gif
