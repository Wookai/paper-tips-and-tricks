---
layout: page
shorttitle: Bibliography
title: Bibliography
order: 4
---

## Back references

[(complete example)](https://github.com/Wookai/paper-tips-and-tricks/tree/master/examples/backref)

For longer documents, such as a master or PhD thesis, it can be useful to have back references in the bibliography, to show where a reference was cited.
To do so, simply add the option `backref=page` to the `hyperref` package:

{% highlight latex %}
\usepackage[backref=page]{hyperref}
{% endhighlight %}

You can customize the way the back references appear with the following commands:

{% highlight latex %}{% raw %}
\renewcommand*{\backref}[1]{}
\renewcommand*{\backrefalt}[4]{{\footnotesize [%
    \ifcase #1 Not cited.%
	\or Cited on page~#2%
	\else Cited on pages #2%
	\fi%
]}}
{% endraw %}{% endhighlight %}

![Backref custom appearance](https://github.com/Wookai/paper-tips-and-tricks/raw/master/examples/backref/backref.png)

