#!/bin/sh

#  step2.sh
#  
#
#  Created by Admin on 2017-09-29.
#
printf "%0.sa" > step2.txt
wait
nc localhost 1233 < step2.txt
