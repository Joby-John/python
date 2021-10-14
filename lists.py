#list creation
Num = input("Enter numbers seperated by space: ")
Num = Num.split(" ")

print("\nhere comes the numbers\n")
print(Num[::-1])
#append
Num.append(input("enter one more "))
print(Num)
#extend
#Num.extend(input("enter more"))
print(Num)
#remove
Num.remove(input("enter element to be removed :"))
print("updated list")
print(Num)
#popping
Num.pop()
print(Num)#after popping