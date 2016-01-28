#!/bin/sh
#s=`pbpaste|wc -w|awk {'print $1'}`
##printf 'less than \E[36m'
##printf $(($s/${1}))  
##printf ":"
##printf $(($s%(${1}/60)))  
##printf '\E[0m minutes read.\n'

if [ -z "${1}" ] 
then
	wordsPerMinute=500
else
	wordsPerMinute=${1}
fi
pbpaste|say -v Alex -r $wordsPerMinute -i