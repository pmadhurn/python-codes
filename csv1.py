"""import csv
f=open("commasvalues.csv","w")
a=csv.writer(f)
a.writerow(["index","name","roll no."])
a.writerow([1,"madhur patel",11])
a.writerow([2,"anil",102])

f.close()

f=open("commasvalues.csv","r")
b=csv.reader(f)

for i in b:
    print(i)

f.close()
"""

import csv
"""
with open('names.csv','w',newline='') as csvfile:
    fieldnames=['first_name','Last_name']
    writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'first_name':'Madhur','Last_name':'Patel'})
    writer.writerow({'first_name':'Anjali','Last_name':'Patel'})
    writer.writerow({'first_name':'Natwar','Last_name':'Patel'})
    csvfile.close()

f=open('names.csv','r')
b=csv.reader(f)

j=open('new1.csv','w')
k=csv.writer(j)
for i in b:
    k.writerow(i)
j.close()
f.close()


f=open("new1.csv","r")
b=csv.reader(f)
for i in b:
    print(i)
f.close()
"""
"""
import csv
data=[
    ['Name','Age','City'],
    ['Madhur','20','New York'],
    ['Anjali','25','New Jersey'],
    ['Raj','24','San Fransisco']
]

with open('new2.csv','w',newline='') as f:
    a=csv.writer(f)
    a.writerows(data)

f=open("new2.csv","r")
b=csv.reader(f)
for i in b:
    print(i)
f.close()

"""

import csv
f=open("Student.csv","w")
s=csv.writer(f)
s.writerow([])