def Q5():
#ip l b h from user find area and perminteter'

ln=eval(input("Enter Length :"))
b=eval(input("Enter Breath :"))
h=eval(input("Enter Height :"))

a=2(ln*b+b*h+h*ln)
p=4(ln+b+h)

print("THE PERIMETER OF A CUBOID IS {} AND THE AREA IS {}".format(p,a))



#ip total amt from user and count no of notes
def Q6():
a=int(input("Enter the Amount for which you want to count the Notes: "))

b=a%500
c=a/500
print(a,b,c)

Q6()
