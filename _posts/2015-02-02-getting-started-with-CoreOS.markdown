---

layout: post
title: getting started with CoreOS via QEMU
date: 2015-02-02 15:19:10
category: blog

---

Install QEMU

    sudo apt-get install qemu-system-x86 qemu-utils

Grab everything required from coreos.com

    mkdir coreos; cd coreos
    wget http://stable.release.core-os.net/amd64-usr/current/coreos_production_qemu.sh
    wget http://stable.release.core-os.net/amd64-usr/current/coreos_production_qemu_image.img.bz2 -O - | bzcat > coreos_production_qemu_image.img
    chmod +x coreos_production_qemu.sh

Copy over your public keys that you have authorized on you machine to the machine we going to start running CoreOS

    ./coreos_production_qemu.sh -a ~/.ssh/authorized_keys -- -nographic

Configure your ssh

    cat << EOF >> ~/.ssh/config
    Host coreos
        HostName localhost
        Port 2222
        User core
        StrictHostKeyChecking no
        UserKnownHostsFile /dev/null
	EOF

Connect to your newly built CoreOS machine

    ssh coreos

Test our CoreOS by running busybox

    docker run busybox /bin/echo hello world

Startup etcd and fleet via systemd

    sudo systemctl start etcd
    sudo systemctl start fleetctl

Testing CoreOS with fleet

    cat << EOF > hello.service
	[Unit]
	Description=My Service
	After=docker.service

    [Service]
    TimeoutStartSec=0
    ExecStartPre=-/usr/bin/docker kill hello
    ExecStartPre=-/usr/bin/docker rm hello
    ExecStartPre=/usr/bin/docker pull busybox
    ExecStart=/usr/bin/docker run --name hello busybox /bin/sh -c "while true; do echo Hello World; sleep 1; done"
    ExecStop=/usr/bin/docker stop hello
	EOF

Load the hello.service via fleet

    fleetctl load hello.service
	Unit hello.service loaded on e81bb63c.../10.0.2.15

Start the hello.service via fleet

    fleetctl start hello.service
	Unit hello.service launched on e81bb63c.../10.0.2.15

Verify its working via systemd and docker

    fleetctl start hello.service
	● hello.service
	  Loaded: loaded (/run/fleet/units/hello.service; linked-runtime)
	  Active: active (running) since Mon 2015-02-02 04:38:40 UTC; 4s ago
	Process: 1118 ExecStop=/usr/bin/docker stop hello (code=exited, status=0/SUCCESS)
	Process: 1400 ExecStartPre=/usr/bin/docker pull busybox (code=exited, status=0/SUCCESS)
	Process: 1391 ExecStartPre=/usr/bin/docker rm hello (code=exited, status=1/FAILURE)
	Process: 1383 ExecStartPre=/usr/bin/docker kill hello (code=exited, status=1/FAILURE)
	Main PID: 1435 (docker)
	  CGroup: /system.slice/hello.service
      └─1435 /usr/bin/docker run --name hello busybox /bin/sh -c while true; do echo Hello World; sleep 1; done
	Feb 02 04:38:40 coreos_production_qemu-522-6-0 systemd[1]: Started hello.service.
	Feb 02 04:38:40 coreos_production_qemu-522-6-0 docker[1400]: Status: Image is up to date for busybox:latest
	Feb 02 04:38:41 coreos_production_qemu-522-6-0 docker[1435]: Hello World
	Feb 02 04:38:42 coreos_production_qemu-522-6-0 docker[1435]: Hello World
	Feb 02 04:38:43 coreos_production_qemu-522-6-0 docker[1435]: Hello World
	Feb 02 04:38:44 coreos_production_qemu-522-6-0 docker[1435]: Hello World
	Feb 02 04:38:45 coreos_production_qemu-522-6-0 docker[1435]: Hello World


