read x && read y
if ((x > y));then
    echo "X is greater than Y"
elif ((x == y)); then
    echo "X is equal to Y"
elif ((x < y)); then
    echo "X is less than Y"
fi


# this is mindblowing 0 the below makes use of the boolean check "&&" get a true/false from an expression, and then echoes the string if true - genius
read x && read y
[[ $x -gt $y ]] && echo 'X is greater than Y'
[[ $x -eq $y ]] && echo 'X is equal to Y'
[[ $x -lt $y ]] && echo 'X is less than Y'

read c

if [[  $c  =~ ^(y|Y)$ ]]; then 
    echo "YES"
elif [[ $c =~ ^(n|N)$ ]]; then 
    echo "NO"
fi
