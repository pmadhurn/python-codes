#csv
def Q2():
    f=open("data1.csv","r")
    print(f.read())
    f.close()
#Q2()

def Q3():
    import csv
    f=open("data1.csv","r")
    ans=csv.reader(f)
    for i in ans:
        print(i[3])
    f.close()
#Q3()

def Q4():
    import csv
    f=open("student.csv","w")
    a=csv.writer(f)
    a.writerow(['Roll No','Name','Grade'])
    a.writerow(['101','Madhur','A'])
    a.writerow(['102','Matri','A'])
    a.writerow(['103','keval','B'])
    f.close()

Q4()