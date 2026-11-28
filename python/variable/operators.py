#arithmetic operations
price = 20
quantity = 6
print("Addition:", price + quantity)
print("Subtraction:", price - quantity)
print("Multiplication:", price * quantity)
print("Division:", price / quantity)
print("Floor Division:", price // quantity)
print("Modulus:", price % quantity)
print("Exponentiation:", price ** quantity)

#Assignment Operators
salary = 10000
salary += 500
print("Addition assignment:", salary)
salary -= 200
print("Subtraction assignment:", salary)
salary *= 2
print("Multiplication assignment:", salary)
salary /= 2
print("Division assignment:", salary)
salary = 10000
salary //= 3
print("Floor division assignment:", salary)
salary = 10000
salary %= 3
print("Modulus assignment:", salary)
salary = 2
salary **= 3
print("Exponentiation assignment:", salary)

#Comparison Operators
mobile_price = 25000
laptop_price = 50000
print("Equal:", mobile_price == laptop_price)
print("Not equal:", mobile_price != laptop_price)
print("Greater than:", mobile_price > laptop_price)
print("Less than:", mobile_price < laptop_price)
print("Greater than or equal:", mobile_price >= laptop_price)
print("Less than or equal:", mobile_price <= laptop_price)

#Logical Operators
price = 500
discount = 100
is_member = True
print("Eligible for discount:", price >= 500 and is_member == True)
print("Special offer:", discount >= 100 or is_member == True)
print("Not a member:", not is_member)