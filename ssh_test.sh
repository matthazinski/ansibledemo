#!/bin/bash

# This is a demo. Don't disable host key checking irl.

for i in `lxc-ls -f -F ipv4 | tail -n+3`
do 
    ssh -o StrictHostKeyChecking=no $i hostname
done
