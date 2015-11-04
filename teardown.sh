#!/bin/bash
for i in `lxc-ls`
do
    lxc-destroy -n $i -f
done
