# read -p "Enter a number: " num
# if [ $num -gt 0]; then
#     echo "$num is positive"
# elif [ $num -lt 0]; then
#     echo "$num is negative"
# else 
#     echo "$num is zero"
# fi


# read -p "Enter your age: " age
# if [ $age -ge 0 ] && [ $age -le 10 ]; then
#     echo "$age You are  child"
# elif [ $age -ge 11 ] && [ $age -le 20 ]; then
#     echo "$age You are  teenager"
# elif [ $age -gt 20 ] && [ $age -le 100 ]; then
#     echo "$age You are  adult"
# else
#     echo "$age Invalid age"
# fi


count=1
while [ $count -le 5 ]; do
  echo "Count: $count"
  ((count++))
done