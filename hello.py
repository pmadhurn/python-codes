print("hello World")
name="madhur"
print("My Name is ",name)
print("{:*>7}".format(name))
print("{:*<20}".format(name))
print("{:*^20}".format(name))


print(name.ljust(10,"*"))
print(name.center(20,"*"))
age=19
print("My Name = ",name,"\nMy Age = ",age)
x=20
y=3.9
print("x=",x,"y=",y)
z=x+y
print("Sum = {:10.2f}".format(z))
print(str(x).rjust(8,'-'))
print(str(x).ljust(8,'-'))
print(str(y).center(10,'*'))
print(x,y,z,sep="#",end="$")
print("My name is {} & age is {}".format(name,age))
print(f"{name} is {age} years old")

#10 + 5 = 15
a=10
b=5
print(f"{a} + {b} = {a+b}")
print(f"{a} - {b} = {a-b}")
print(f"{a} * {b} = {a*b}")
print(f"{a} / {b} = {a/b}")

print("{} + {} = {}".format(a,b,a+b))
print("{} - {} = {}".format(a,b,a-b))
print("{} * {} = {}".format(a,b,a*b))
print("{} / {} = {}".format(a,b,a/b))

q=a+b
print("Sum of {} and {} is {:.3f}".format(a,b,q))
print(a,b,q,sep="$")
print(a,b,q,sep="&")
