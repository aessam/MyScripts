#!/bin/sh
exiftool "${1}" |grep "Media Duration"|cut -d':' -f4 -f3 -f2 |sed 's/:/ /g'| awk '{print ((($1*60)+$2)*60)+$3}'


