#facorial of a number using Python
print("Enter a number to check factorial")
num = int(input(":"))
number = num
fact = 1

if num == 0:
    result = 1
else:
    while(num >= 1):
        fact = fact*num
        num = num - 1
    result = fact

print("factorial of {} is {}".format(number,fact))        
     
