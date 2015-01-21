---

layout: post
title: posting jekyll from emacs
date: 2015-01-21 18:14:34
category: blog

---


Short blog post about how I can post updates into jekyll from emacs using a very simple function.

{% highlight lisp %}
    (defun new-blog-post (title)
     (interactive "s")
     (let ((date (format-time-string "%Y-%m-%d")))
       (find-file (
		   format 
		   "~/code/github/daniellawrence.github.io/_posts/%s-%s.markdown" 
		   date (replace-regexp-in-string " " "-" title)))
       (insert "---\n\n")
       (insert "layout: post\n")
       (insert (format "title: %s\n" title))
       (insert (format-time-string "date: %Y-%m-%d %H:%M:%S\n"))
       (insert "category: blog\n\n")
       (insert "---\n\n\n")
       (markdown-mode)))
{% endhighlight %}


Now `M-x new-blog-post` will create a new blog post for me, I just need to commit the changes `M-z` and then push them back up to danysadm.com via github.com pages.

You can see my whole `~/.emacs` configuration file on [github.com](https://github.com/daniellawrence/dot-files/blob/master/dot-emacs).

---------------

Hooray for emacs
----------------
