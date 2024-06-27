def Q1():
    s=0
    #sum all the elements in list
    l=eval(input("Enter : "))
    for i in l:
        s=s+i
    print("Sum of List Elements = ",s)
    
#Q1()
def Q2():
    l=eval(input("Enter : "))
    m=0
    #find greatest
    for i in l:
        if i>m:
            m=i
    print("Greatest Number = ",m)
#Q2()
def Q3():
    i=f=s=0
    #count total string,int,float from given list
    l=[11,2.2,33,4,"abc","xyz","pqr",3.4,80]
    for j in l:
        if type(j)==int:
            i=i+1
        elif type(j)==float:
            f+=1
        elif type(j)==str:
            s+=1
    print("Integers = ",i)
    print("Float = ",f)
    print("Strings = ",s)
#Q3()
def Q4():
    l=["abc","xyz","abba","pqr","madhur","AB","PQ"]
    for i in l:
        if i[0]==i[-1]:
            print(i)
        '''if len(i)==2:
            print(i)'''
Q4()            
    
        
        
