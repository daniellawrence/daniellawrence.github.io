---

layout: post
title: using docker in continuous integration (CI)
date: 2015-01-21 19:18:14
category: blog

---

Attached is a shell script that will help you to run your application within docker for your CI system.

It will take care of..

* Naming the container based on the git version and repo name.
* Grabbing any base images that you require
* Sending the output to STDOUT

It will assume that your have a `Dockerfile` in your current working directory when calling the script.

{% gist 5174d159357136239498 %}

