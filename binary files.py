import pickle
'''
f=open("myfile.dat","wb")
l=["abc","pqr","xyz","hello","good"]
pickle.dump(l,f)
print("successful")
f.close()
'''


"""f=open("myfile.dat","rb")
a=pickle.load(f)
f.close()
print(a)
"""

"""
f=open("student.dat","wb")
l={"madhur":[1,50],"aakash":[2,30],"ruchit":[3,55],"maitri":[4,40],"raj":[5,50]}

pickle.dump(l,f)
print("Successful")
f.close()
"""



f=open("student.dat","rb")
a=pickle.load(f)
f.close()



for i,j in a.items():
    print("\nName : ",i,"\nRoll no. : ",j[0],"\nMarks : ",j[1])
    

x={}
y={"enter the number of students you want to add in list:"}
z=0
while z<y:
    z=z+1
    name=input(f"enter the name of student {1}")
