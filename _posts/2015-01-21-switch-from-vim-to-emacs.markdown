---

layout: post
title: switch from vim to Emacs
date: 2015-01-21 22:53:37
category: blog

---

This page should help you get started on your Emacs journey from using vim.

<Br />

How I start with transition most people from vim over to Emacs, is first turning Emacs into a vim clone. Then help slowly them explore the features of Emacs.

<Br />

Lets setup a quick `~/.emacs` file that will turn make Emacs behave like vim.

{% highlight lisp %}
$ cat << EOF > ~/.emacs
  (require 'package)
  (package-initialize)
  (add-to-list 'package-archives '("gnu" . "http://elpa.gnu.org/packages/"))
  (add-to-list 'package-archives '("melpa" . "http://melpa.org/packages/"))
  (add-to-list 'package-archives '("melpa" . "http://melpa.milkbox.net/packages/"))
  (add-to-list 'package-archives '("marmalade" . "http://marmalade-repo.org/packages/"))
  (package-refresh-contents)
  (package-install 'evil)
  ;; Enable evil for vim bindings
  (require 'evil)
  ;; Turn on VIM emulation
  (evil-mode 1)
  ;; Turn off all the bars, just like a vim terminal session
  (menu-bar-mode -1)
  (toggle-scroll-bar -1)
  (tool-bar-mode -1)
  ;; show line numbers in the side bar
  (linum-mode -1)
EOF
{% endhighlight %}

Start Emacs

    $ emacs

