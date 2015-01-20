---
layout: page
title: blog
permalink: /blog/
---

{% for post in site.posts %}

{{ post.date | date: "%-d %b, %Y" }}
- [{{post.title}}](/../{{ post.url }})

{% endfor %}
