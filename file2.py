'''
#create om.txt file write any file lines and close the file then read data from om.txt file display data line by line
def Q1():
    """try:
        f=open("poem.txt","w")
        f.writelines("twinkle twinkle little star\n")
        f.writelines("how i wonder what you are \n")
        f.write("up above the world so high\n")
        f.write("like a diamond in the sky\n")
        f.close
        print("file has been created successfully")
    except:
        print("sorry there is a error in creation of your file")
    """
    f=open("poem.txt","r")
    a=f.readlines()
    for i in a:
        print(i)


#Q1()
"""
#replace all words (twinkle ) by shine
def Q2():
    f=open("poem.txt","r")
    a=f.read()
    f.close
    a=a.replace("twinkle","shining") 
    f=open("poem.txt","w")
    f.write(a)
    f.close()
Q2()         
"""
""""
    
#get input from user

def Q3():
    f=open("poem.txt","r")
    a=f.read()
    f.close
    b=input("enter the string that you want to get replaced by shining : ")
    a=a.replace("shining",b) 
    f=open("poem.txt","w")
    f.write(a)
    f.close()
Q3()         
"""
'''