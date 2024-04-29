#!/bin/dash

until test -z $1; do
	eval 'export $1="$(cat $2)"'
	shift; shift
done
</dev/stdin envsubst
