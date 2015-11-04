#!/usr/bin/env python

# (c) 2013, Michael Scherer <misc@zarb.org>
# (c) 2014, Hiroaki Nakamura <hnakamur@gmail.com>
#
# This file is based on https://github.com/ansible/ansible/blob/devel/plugins/inventory/libvirt_lxc.py which is part of Ansible,
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

from subprocess import Popen,PIPE
import distutils.spawn
import sys
import json

result = {}

# NOTE: When you run ansible-playbook for the first time on the lxc host,
# lxc is not yet installed. So we skip building containers list.
if distutils.spawn.find_executable('lxc-ls'):
    result['containers'] = {}
#    pipe = Popen(['lxc-ls', '--active'], stdout=PIPE, universal_newlines=True)
    pipe = Popen(['lxc-ls', '-f', '-F', 'ipv4'], stdout=PIPE, universal_newlines=True)
    
    result['containers']['hosts'] = [x.strip() for x in pipe.stdout.readlines()[2:]]
    result['containers']['vars'] = {}
    result['containers']['vars']['ansible_connection'] = 'ssh'

result['local'] = {}
result['local']['hosts'] = ['localhost']
result['local']['vars'] = {}
result['local']['vars']['ansible_connection'] = 'local'

if len(sys.argv) == 2 and sys.argv[1] == '--list':
    print json.dumps(result)
elif len(sys.argv) == 3 and sys.argv[1] == '--host':
    if sys.argv[2] == 'localhost':
        print json.dumps({'ansible_connection': 'local'})
    else:
        print json.dumps({'ansible_connection': 'ssh'})
else:
    print "Need an argument, either --list or --host <host>"
