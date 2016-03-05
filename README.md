dansysadm.com
-------------

Installing
----------

    gem install jekyll
    gem install jekyll-gist
    
building
--------

    jekyll build
    

shipping
--------

Sucks, but good enough for now

    ssh dansysadm.com sudo -u www-data "bash -c 'cd /usr/share/nginx/dansysadm.com && git pull'"
