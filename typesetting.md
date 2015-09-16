---
layout: page
shorttitle: Typesetting
title: Typesetting your paper
order: 1
---

Typesetting is the composition of text by means of arranging the types, i.e., letters and symbols.
It is mostly a question of a aesthetics, but beautiful typography makes documents easier and more pleasant to read, helping the reader to get to the message.

We list below some typesetting tips and tools to help you when composing your documents.
Some tips are specific to LaTeX, but others apply regardless of what you are using.

## One sentence per line

When writing LaTeX documents, put one sentence per line in your source file.
Write:
{% highlight latex %}
This is my first sentence.
This is the second one.
{% endhighlight %}
and not:
{% highlight latex %}
This is my first sentence. This is the second one.
{% endhighlight %}

The main reason for this is source control and collaboration: when looking at the changes of a commit, it is much easier to identify what sentence was changed if they are each on their separate line.
Your coworkers will thus be able to see the changes more easily.

Another benefit is that you will be able to better identify errors when only given a line number by our LaTeX compiler.

## Capitalization

We will refer below to two types of capitalization:
* sentence format : The title of the nice book
* title format: The Title of the Nice Book

Use title format for all section, subsection, etc. titles. In order to help you capitalize the right words, there's a handy website: [titlecapitalization.com](http://titlecapitalization.com/).

## Tables

[(complete example)](https://github.com/Wookai/paper-tips-and-tricks/tree/master/examples/booktabs)

[booktabs](https://www.ctan.org/pkg/booktabs) can help you produce clean and nice-looking tables.

{% highlight latex %}
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
{% endhighlight %}

![Booktabs example](https://github.com/Wookai/paper-tips-and-tricks/raw/master/examples/booktabs/booktabs.png)

In general, avoid using vertical lines in your tables.
Instead, if you want to group columns, do it in the headers using `\cmidrule`.
You can also replace horizontal lines with spacing, using `\addlinespace`.

Column heads should use sentence-format capitalization (see [www.chicagomanualofstyle.org/15/ch13/ch13_sec019.html](http://www.chicagomanualofstyle.org/15/ch13/ch13_sec019.html)).

You can find more advice on table formatting here: [www.inf.ethz.ch/personal/markusp/teaching/guides/guide-tables.pdf](http://www.inf.ethz.ch/personal/markusp/teaching/guides/guide-tables.pdf).
Here is a nice GIF that illustrates some of these rules:

![Better table formatting](http://darkhorseanalytics.com/blog/wp-content/uploads/2014/03/ClearOffTheTableMd.gif)

## Number formatting

[(complete example)](https://github.com/Wookai/paper-tips-and-tricks/tree/master/examples/siunitx)

Use the [siunitx](https://ctan.org/pkg/siunitx) package to format all numbers, currencies, units, etc:
{% highlight latex %}
\usepackage{siunitx}
% ---
This thing costs \SI{123456}{\$}.
There are \num{987654} people in this room, \SI{38}{\percent} of which are male.
{% endhighlight %}

![Siunitx formatting](https://github.com/Wookai/paper-tips-and-tricks/raw/master/examples/siunitx/siunitx-formatting.png)

You can also use it to round numbers:
{% highlight latex %}
\usepackage{siunitx}
% ---
\sisetup{
	round-mode = places,
	round-precision = 3
}%
You can also round numbers, for example \num{1.23456}.
{% endhighlight %}
![Siunitx formatting](https://github.com/Wookai/paper-tips-and-tricks/raw/master/examples/siunitx/siunitx-rounding.png)

Finally, it can help you better align numbers in a table:
{% highlight latex %}
\usepackage{booktabs}
\usepackage{siunitx}
%---
\begin{table}
	\centering
	\begin{tabular}{lS}
		\toprule
		Name & {Value} \\ % headers of S columns have to be in {}
		\midrule
		Test & 2.3456 \\
		Blah & 34.2345 \\
		Foo & -6.7835 \\
		Bar & 5642.5 \\
		\bottomrule
	\end{tabular}
	\caption{Numbers alignment with \texttt{siunitx}.}
\end{table}
{% endhighlight %}
![Siunitx formatting](https://github.com/Wookai/paper-tips-and-tricks/raw/master/examples/siunitx/siunitx-table.png)
