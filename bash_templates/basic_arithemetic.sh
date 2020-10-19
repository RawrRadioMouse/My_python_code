read x && read y
echo $((x+y))
echo $((x-y))
echo $((x*y))
echo $((x/y))

# OR

read X
read Y
printf "%s\n" $X{+,-,*,/}"($Y)" | bc # this expression prints each string as new line (%s\n) and then takes $X, declares a range containing operators and then Y
