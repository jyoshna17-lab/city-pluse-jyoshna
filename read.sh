# echo "enter input"
# read num

# echo $num

# read -p "enter number" sum

# echo $sum

read -p "your name: " name
#echo $name
read -p "your  roll number: " roll_no
#echo $roll_no
read -p "Enter comment: " comment
#echo $comment
echo "your name: $name"
echo "your roll no: $roll_no"
echo "comment : $comment"

echo "Name: $name" > output/output.txt
echo "Roll Number: $roll_no" >> output/output.txt
echo "Comment: $comment" >> output/output.txt
cat output/output.txt