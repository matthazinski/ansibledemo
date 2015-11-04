#!/bin/bash
for i in `lxc-ls`
do
    mkdir -p /var/lib/lxc/$i/rootfs/root/.ssh/
    cp /root/.ssh/id_rsa.pub /var/lib/lxc/$i/rootfs/root/.ssh/authorized_keys
    lxc-attach -n $i apt-get -y install python
done

