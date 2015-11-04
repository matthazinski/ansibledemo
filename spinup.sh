#!/bin/bash

make_container () {
    lxc-create -n $1 -t debian
    lxc-start -n $1 -d
}

for i in $(seq 1 $1)
do
    make_container ansible$i &
done
