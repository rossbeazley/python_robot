#!/bin/sh

tar -cf *.py deploy.tar
scp deploy.tar root@robotpi:
ssh root@robotpi 'tar -xf deploy.tar'

#ssh root@robotpi '/etc/init.d/robot restart'
