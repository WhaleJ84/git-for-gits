# Git for Gits

A project to teach the usage of Git and related technologies.

![](https://miro.medium.com/max/640/0*Gb3B1-Xk5qHaxU7v.jpg)

## Markdown for Morons

This document is written in Markdown[^1] and named `README.md`.
Following this format will have it rendered in the repository's directory.
Most IDEs[^ide] will render the file in realtime, removing the need to push your changes to a repository to see how it looks.
If you're a :neckbeard: using a Debian based system, you can render it locally with:

```shell
# Install dependencies (only needs to be done once)
sudo apt install -y pandoc w3m w3m-img

# Render and view markdown
pandoc README.md | w3m -T text/html

# Inside Vim
:! pandoc % | w3m -T text/html
```

You may question why Markdown is relevant to learning Git;
It is important to document what your projects are about and how to use them.
You are not just writing documentation for others, ==you are also writing it for yourself.==
There will come a time where you return to a project after a long period and have no idea where to resume without it.

[^1]: [This guide](https://www.markdownguide.org/basic-syntax) provides a handy link to learning the syntax.
[^ide]: Integrated Development Environment
	: Software for building applications that combines common developer tools into a single graphical user interface
