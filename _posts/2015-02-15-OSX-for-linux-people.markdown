---

layout: post
title: OSX for linux people
date: 2015-02-15 22:21:02
category: blog

---

Moving to my first OSX laptop for work from my linux machines.
I needed to fix a few things to keep me happy.


Install homebrew to get a cli based package manager

    ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"


Install coreutils

    brew install coreutils

Install wget

    brew install wget

Install emacs (24+)

    brew install emacs

Install X11 (xquartz) to allow X11 apps to run

* Download the pkg from http://xquartz.macosforge.org/landing/

You will need to update your path in order to use the nicer tools

    cat << EOF >> ~/.bashrc
    export PATH="/usr/local/bin:$PATH"
    export MANPATH="/usr/local/opt/coreutils/libexec/gnuman:$MANPATH"
	EOF


Restart your machine.
