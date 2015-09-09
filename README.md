# Tips and Tricks for Writing Scientific Papers

## What is this?

We gather in this repository at list of tool, best practices, tips and other guidelines we found useful/important when writing scientific papers.
Some are a matter of style (we tend to follow the guidelines of the Chicago Manual of Style), and we are well aware that other people prefer to do differently, but we list them anyway to have a consistent guide.
Feel free to adapt, change, ignore, or even challenge everything we write!

## Typesetting your paper

We list below recommendations related to typesetting your paper.
Some tips are specific to LaTeX, but others apply regardless of what you are using.

### Capitalization

We will refer below to two types of capitalization:
* sentence format : The title of the nice book
* title format: The Title of the Nice Book

### Tables

Use [booktabs](https://www.ctan.org/pkg/booktabs) to typeset your tables.

```
\usepackage{booktabs}
% --
\begin{table}
	\centering
	\begin{tabular}{lcc}
		\toprule
		& \multicolumn{2}{c}{Data} \\ \cmidrule(lr){2-3}
		Name & Column 1 & Another column \\
		\midrule
		Some data & 10 & 95 \\
		Other data & 30 & 49 \\
		\addlinespace
		Different stuff & 99 & 12 \\
		\bottomrule
	\end{tabular}
	\caption{My caption.}
	\label{tab-label}
\end{table}
```

![Booktabs example][https://github.com/Wookai/paper-tips-and-tricks/raw/master/examples/booktabs/booktabs.png]

As a rule of thumb, you should avoid using vertical lines but group the column headers if required using `\cmidrule`.
You can also replace horizontal lines with spacing, using `\addlinespace`.
Column heads should use sentence format capitalization (see http://www.chicagomanualofstyle.org/15/ch13/ch13_sec019.html).
You can find more advice on table formatting here: http://www.inf.ethz.ch/personal/markusp/teaching/guides/guide-tables.pdf

Here is a nice GIF that illustrates some of these rules:

![Better table formatting][http://darkhorseanalytics.com/blog/wp-content/uploads/2014/03/ClearOffTheTableMd.gif]

### Number formatting

Use the [siunitx](https://ctan.org/pkg/siunitx) package to format all numbers.
For example, use `\SI{1234567}{\$}` to produce `$1 234 567`.
You can also use it to round numbers, etc.


## Bibliography

### Back references

For longer documents, such as a master or PhD thesis, it could be useful to have back references in the bibliography, to show where a reference was cited.
To do so, simply add the option `backref=page` to the `hyperref` package:

```
\usepackage[backref=page]{hyperref}
```

You can customize the way the back references appear with the following commands:

```
\renewcommand*{\backref}[1]{}
\renewcommand*{\backrefalt}[4]{{\footnotesize [%
    \ifcase #1 Not cited.%
	\or Cited on page~#2%
	\else Cited on pages #2%
	\fi%
]}}
```

## Creating figures

Figures are a very important part of a majority of papers: they are your way of communicating your results.
You should always think about what you are trying to say with each figure, and make sure that there is just enough information to support your message, not more.
For example, if you want to show patterns in 2d points (there are two clusters well separated), maybe it is not necessary to put ticks and values on the axes (the scale does not really matter)?

### One script per data-driven figure

Some figures are hand-made, to explain a system or give a global picture.
Others are data-drive, i.e., visualize some data.
These must be scripted as much as possible: ideally, if your data changes, you should only have to launch a script once to update your figure, without any other intervention (setting the view, zooming, saving/cropping the figure, etc.).
Similarly, if the data required to generate a figure takes more than seconds to be produced, you should have a first script that computes and saves the data, and a second script that plots it.
This way, you will save a lot of time when working on the plot: you won't have to wait after each small change to the figure to see its effect.


## Useful resources

* Automatically capitalize your title: http://titlecapitalization.com
* Chicago Manual of Style: http://www.chicagomanualofstyle.org
* Command-line check of weasel words, passive, etc: https://github.com/devd/Academic-Writing-Check
