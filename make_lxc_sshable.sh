#!/bin/bash
for i in `lxc-ls`
do
    mkdir /var/lib/lxc/$i/rootfs/root/.ssh/
    cp /root/.ssh/id_rsa.pub /var/lib/lxc/$i/rootfs/root/.ssh/authorized_keys
done

