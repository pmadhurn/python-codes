#CREATE A FILE STORY.TXT AND ADD 500 WORDS OF STORY 
'''
STEP 1 REPLACE THE  WITH A AND DISPLAY THE FILELINE FIRST 100 CHARACTERS 
'''

def X1():
    file=open("story.txt","w")
    file.write("The Magical Garden Gnome\n\nIn a cozy little cottage at the edge of Whispering Woods lived a young girl named Lily. She had wild curly hair, bright green eyes, and a passion for gardening. Every day after school, Lily would rush to her backyard to tend to her colorful flower beds and vegetable patches.\n\nOne sunny afternoon, as Lily was planting some new sunflower seeds, she noticed something peculiar. A tiny red hat poked out from behind her tomato plants. Curious, she crept closer and gasped in surprise. There, standing no taller than her hand, was a garden gnome! But this was no ordinary statue – the gnome was alive and moving!\n\n'Oh, hello there!' the gnome said with a friendly wave. I'm Gus the Garden Gnome. I hope you don't mind me dropping by.\n\nLily's eyes widened with wonder. Not at all! she exclaimed. I'm Lily. I've never met a real garden gnome before!\n\nGus chuckled, his rosy cheeks growing even rosier. Well, we're a bit shy, you see. But I couldn't resist visiting such a lovely garden. You've done a marvelous job!\n\nLily beamed with pride. Thank you! Would you like a tour?\n\nAnd so began an extraordinary friendship. Every day after school, Lily would race to the garden to chat with Gus. The little gnome shared magical gardening secrets, like how to whisper to the flowers to help them grow and which songs the vegetables liked best.\n\nOne day, Lily arrived home to find her garden in chaos. A family of rabbits had snuck in and nibbled on her precious carrots and lettuce. Lily was heartbroken.\nDon't worry, Gus said, patting her hand. I have an idea.\n\nThat night, under the light of the full moon, Gus taught Lily how to perform a special gnome dance. They twirled and hopped around the garden, singing a silly song about friendship and growth. As they danced, tiny sparkles of magic drifted from their fingertips, settling on the damaged plants.\n\nThe next morning, Lily couldn't believe her eyes. Her garden had transformed overnight! The nibbled vegetables had regrown, even bigger and more vibrant than before. New flowers had sprouted, filling the air with sweet fragrances.\n\nGus, it's amazing! Lily exclaimed, twirling with joy.\n\nThe gnome winked. That's the power of a little magic and a lot of love.\n\nFrom that day on, Lily and Gus worked together to make their garden the most magical place in all of Whispering Woods. Word spread about the extraordinary plants that grew there, and soon, neighbors began stopping by to admire the beautiful blooms and tasty vegetables.\n\nLily and Gus decided to share their bounty with the whole town. They set up a small stand at the end of the driveway, offering free flowers and vegetables to anyone who needed them. The garden's magic seemed to spread, making everyone who visited a little happier and kinder.\n\nAs for the rabbits, Gus helped Lily create a special section of the garden just for them, full of their favorite treats. This way, everyone could enjoy the magical garden in harmony.\n\nYears passed, and Lily grew taller, but her friendship with Gus remained as strong as ever. She never forgot the lessons he taught her about nurturing plants, spreading kindness, and believing in a little bit of magic.\n\nEven when Lily went off to college, she would return home every summer to tend to her magical garden with Gus. And on quiet nights, passersby might catch a glimpse of a young woman and a tiny gnome, dancing under the moonlight, their laughter echoing through Whispering Woods.\n\nThe end.\n")
    file.close()

    f=open("story.txt","r")
    a=f.read()
    a=a.replace("the","a")
    f.close()
    
    f=open("story.txt","w")
    f.write(a)
    f.close()

    f=open("story.txt","r")
    print(f.readlines(100))
#X1()

f=open("data.txt","w")
f.write("The Magical Garden Gnome\n\nIn a cozy little cottage at the edge of Whispering Woods lived a young girl named Lily. She had wild curly hair, bright green eyes, and a passion for gardening. Every day after school, Lily would rush to her backyard to tend to her colorful flower beds and vegetable patches.\n\nOne sunny afternoon, as Lily was planting some new sunflower seeds, she noticed something peculiar. A tiny red hat poked out from behind her tomato plants. Curious, she crept closer and gasped in surprise. There, standing no taller than her hand, was a garden gnome! But this was no ordinary statue – the gnome was alive and moving!\n\n'Oh, hello there!' the gnome said with a friendly wave. I'm Gus the Garden Gnome. I hope you don't mind me dropping by.\n\nLily's eyes widened with wonder. Not at all! she exclaimed. I'm Lily. I've never met a real garden gnome before!\n\nGus chuckled, his rosy cheeks growing even rosier. Well, we're a bit shy, you see. But I couldn't resist visiting such a lovely garden. You've done a marvelous job!\n\nLily beamed with pride. Thank you! Would you like a tour?\n\nAnd so began an extraordinary friendship. Every day after school, Lily would race to the garden to chat with Gus. The little gnome shared magical gardening secrets, like how to whisper to the flowers to help them grow and which songs the vegetables liked best.\n\nOne day, Lily arrived home to find her garden in chaos. A family of rabbits had snuck in and nibbled on her precious carrots and lettuce. Lily was heartbroken.\nDon't worry, Gus said, patting her hand. I have an idea.\n\nThat night, under the light of the full moon, Gus taught Lily how to perform a special gnome dance. They twirled and hopped around the garden, singing a silly song about friendship and growth. As they danced, tiny sparkles of magic drifted from their fingertips, settling on the damaged plants.\n\nThe next morning, Lily couldn't believe her eyes. Her garden had transformed overnight! The nibbled vegetables had regrown, even bigger and more vibrant than before. New flowers had sprouted, filling the air with sweet fragrances.\n\nGus, it's amazing! Lily exclaimed, twirling with joy.\n\nThe gnome winked. That's the power of a little magic and a lot of love.\n\nFrom that day on, Lily and Gus worked together to make their garden the most magical place in all of Whispering Woods. Word spread about the extraordinary plants that grew there, and soon, neighbors began stopping by to admire the beautiful blooms and tasty vegetables.\n\nLily and Gus decided to share their bounty with the whole town. They set up a small stand at the end of the driveway, offering free flowers and vegetables to anyone who needed them. The garden's magic seemed to spread, making everyone who visited a little happier and kinder.\n\nAs for the rabbits, Gus helped Lily create a special section of the garden just for them, full of their favorite treats. This way, everyone could enjoy the magical garden in harmony.\n\nYears passed, and Lily grew taller, but her friendship with Gus remained as strong as ever. She never forgot the lessons he taught her about nurturing plants, spreading kindness, and believing in a little bit of magic.\n\nEven when Lily went off to college, she would return home every summer to tend to her magical garden with Gus. And on quiet nights, passersby might catch a glimpse of a young woman and a tiny gnome, dancing under the moonlight, their laughter echoing through Whispering Woods.\n\nThe end.\n")
f.close()   

#1:write a program to read entire content of text file ("data.txt")

def Q1():
    f=open("data.txt","r")
    f.read()
    f.close()
#Q1()

#2: write a program to read first 5 characters in the text file ("data.txt")
def Q2():
    f=open("data.txt","r")
    f.readlines(5)
    f.close()
#Q2()

#3:write a program to read first line from the text file ("data.txt")

def Q3():
    f=open("data.txt","r")
    f.readline()
    f.close()
#Q3()

#4:wap in python to display no of lines in python

def Q4():
    f=open("file.txt","r")
    a=f.readlines()
    print(len(a))
    f.close()
#Q4()

#5: wap in python  to display first line from the text file("data.txt") using readlines


def Q5():
    f=open("data.txt","r")
    a=f.readlines()
    f.close()
    x=a[0]
    print(x)
#Q5()


#6:write a program to display first char from all lines in (data.txt)
def Q6():
    f=open("data.txt","r")
    a=f.readlines()
    f.close()
    for i in a:
        print(i[0])
    
#Q6()

#7:write a program in python to display all the lines from text file data.txt with first chase in upper case
def Q7():
    f=open("data.txt","r")
    a=f.readlines()
    f.close()
    for i in a:
        if i[0].isalpha():
            i[0]=i[0].upper()
    for i in a:
        print(i)
#Q7()


#wap to find no of char in data.txt
def Q8():
    x=0
    f=open("data.txt","r")
    a=f.readlines()
    f.close()
    for i in a:
        x=x+(len(i))

    print(x)    
#Q8()


#9:wap in py to find no of char in firstline in data.txt using readline()
def Q9():
    f=open("data.txt","r")
    a=f.readline()
    a=len(a)
    print(a)
#Q9()

#10:wap in py tofind no of char in firstline in data.txt using readlines()
def Q10():
    f=open("data.txt","r")
    a=f.readlines()
    b=a[0]
    b=len(b)
    print(b)
#Q10() 

#

def Q7() :
    f=open("story.txt","r")
    a=f.readlines()
    f.close()
    for i in range(0,len(a)) :
        a[i]=a[i].capitalize()
    print(a)

#11:WAP TO WRITE TWO CHAR OF ALL THE LINES FROM FILE (data.txt)

def Q11():
    f=open("data.txt","r")
    a=f.readlines()
    for i in a:
        i=i.strip()
        if len(i)>=2:
            print(i[-1]," and ",i[-2])
        elif len(i)==1:
            print(i[-1])
        else:
            print("\n")

#Q11()

#12:wap to reas all the characters from the file (and display in upper case)

def Q12():
    f=open("data.txt","r")
    a=f.readlines()
    b=[]
    for i in a:

        for j in i:
            if j.isalpha():
                b.append(j.upper())
    
    print(b)

#Q12()

#13:wap to count all the upper case cahracters from the file (data.txt)
def Q13():
    f=open("data.txt","r")
    a=f.readlines()
    b=[]
    for i in a:

        for j in i:
            if j.isupper():
                b.append(j)
    print(b)
#Q13()

#14:wap to count number of spaces from hte file data.txt

def Q14():
    f=open("data.txt","r")
    a=f.readlines()
    b=0
    for i in a:

        for j in i:
            if j==" ":
                b+=1
    print(b)
#Q14()

#15:wap to count no if vovel in python:


def Q15():
    f=open("data.txt","r")
    a=f.readlines()
    b=0
    c=["a","e","i","o","u","A","E","I","O","U"]
    for i in a:

        for j in i:
            if j in c:
                b+=1
    print(b)
#Q15()



#16:wap to write following lines in program:

def Q16():
    f=open("data.txt","a")
    f.write("I am learning Python\n")
    f.write("I am writing this blog")
    f.write("Welcome to my Blog")
    f.close()
    f=open("data.txt","r")
    print(f.read())
#Q16()
    

#17:wap to read from data and write to dest.txt
def Q17():
    f=open("data.txt","r")
    a=f.readlines()
    f.close()
    f=open("dest.txt","w")
    f.writelines(a)
    f.close()
    f=open("dest.txt","r")
    print(f.read())
    
#Q17()

#18:wap to read f4rom data.txt adn writ to dest except spaces.
def Q18():
    f=open("data.txt","r")
    a=f.read()
    a=a.replace(" ","")
    f.close()
    f=open("dest.txt","w")
    f.writelines(a)
    f.close()
    f=open("dest.txt","r")
    print(f.read())

##Q18()



#19:wap to read from data.txt and write to dest.txt except vovels

def Q19():
    c=["a","e","i","o","u","A","E","I","O","U"]
    f=open("data.txt","r")
    a=f.read()
    for i in range(len(c)): 
        a=a.replace(c[i],"")
    f.close()
    f=open("dest.txt","w")
    f.writelines(a)
    f.close()
    f=open("dest.txt","r")
    print(f.read())

#Q19()

#20:wap to count frequency of char entered by of the user:

def Q20():
    f=open("data.txt","r")
    a=f.readlines()
    b=0
    c=input("enter the frequency of the charor thing you want to find : ")
    for i in a:

        for j in i:
            if j==c:
                b+=1
    print(b)
#Q20()



#21:wap to read from data.txt amd write alternate line to dest.txt

def Q21():
    f=open("data.txt","r")
    a=f.readlines()
    f.close()
    f=open("zest.txt","w")
    b=len(a)
    for i in range(1,b):
        if b%2==0:
            f.write(a[i])
    f.close()
    f=open("zest.txt","r")
    
    print(f.read())

    f.close()
    
#Q21()


#22.Write a program to read entire data from the file"data.txt" and write only those lines to file "dest.txt" which starts from word "The"

def Q22():
    f=open("data.txt","r")
    a=f.readlines()
    f.close()
    f=open("pest.txt","w")
    for i in a:
        if len(i)>3:
            if i[0]== "t" or "T"  and i[1]=="h" or "H" and i[2]=="e"or "e":
                f.write(i)

    f.close()
    f=open("pest.txt","r")
    
    print(f.read())

    f.close()
    
#Q22()

#23.Write a program to read entire data from file"data.txt" using readline() method.


def Q23():
    f=open("data.txt","r")
    print(f.readline())
    """line = f.readline()
    while line:
        print(line.strip())  # strip() removes the trailing newline
        line = f.readline()
    """
    for i in range(39):
        print(f.readline())
    f.close()
#Q23()

#24.Write a program to read the content from file "data.txt" and write to file "dest.txt" after changing the case(convert lower case to upper case and vice-versa)

def Q24():
    f=open("data.txt","r")
    a=f.read()
    #b=f.swapcase()
    f.close
    b=a.swapcase()
    f=open("dest.txt","w")
    f.write(b)
    print(b)
#Q24()

#25. Write a program to create a list of 5 numbers (input from user) and write that list in a file "data.txt".

def Q25():
    l=[]
    x=0
    while x!=5:
        x+=1
        y=int(input("Enter a number : "))
        l.append(y)
    
    f=open("data.txt","w")
    f.writelines(str(l))
    f.close()
    f=open("data.txt","r")
    print(f.read())
    

#Q25()

#26.Write a program to create a list of 5 numbers(input from user) and write list in file "data.txt". Now read the numbers from data.txt and write only even numbers to another file "dest.txt". TAG

def Q26():
    l=[1,2,3,4,5,6,7,8,9]
    x=5
    while x!=5:
        x+=1
        y=int(input("Enter a number : "))
        l.append(y)
    
    f=open("data.txt","w")
    f.writelines(str(l))
    f.close()
    f=open("data.txt","r")
    a=f.read()
    f.close()
    x=len(a)
    z=[]
    for i in range(x):
        z.append(eval(a[i]))
    
    f=open("dest.txt","w")
    for i in z:
        
        if i%2==0:
            f.write(i)
    f.close()
    
    f=open("dest.txt","r")
    print(f.read())

#Q26()

#27.Write a program to read a file "data.txt" and replace word "school" by collage and write it in dest.txt

def Q27():
    f=open("data.txt","r")
    a=f.read()
    f.close()
    a=a.replace("school","collage")
    f=open("bert.txt","w")
    f.write(a)
    f.close()



#Q27()

#28. Write a program to replace a word "school" to"college" in the same file("data. txt"). C-1

def Q28():
    f=open("data.txt","r")
    a=f.read()
    f.close()
    a=a.replace("school","collage")
    f=open("data.txt","w")
    f.write(a)
    f.close()


#Q28()

#29. Write a program in python to replace all word "the" by another word "them" in a file "poem txt".
def Q29():
    f=open("poem.txt")
    a=f.read()
    a=a.replace("the","them")
    f.close()
    f=open("poem.txt","w")
    f.write(a)

Q29()

#30. Write a program in python to replace a character by another character in a file "story.txt. (Accept both the characters from the user)

def Q30():
    x=input("enter the character you want to replace")
    b=input("enter the character you want to replace it with : ")
    f=open("poem.txt")
    a=f.read()
    a=a.replace(x,b)
    f.close()
    f=open("poem.txt","w")
    f.write(a)
#Q30()

#31.Write a program in python to replace all the 'a' by '@' in a file "data.txt".

def Q31():
    
    f=open("poem.txt")
    a=f.read()
    a=a.replace("a","@")
    f.close()
    f=open("poem.txt","w")
    f.write(a)
    f.close()
#Q31()




#32.Write a program in python to read file "data.txt" and display only those lines whose length is more than 40 characters.
def Q32():
    f=open("data.txt","r")
    a=f.readlines()
    for i in a:
        if len(i)>40:
            print(i)
#Q32()

#33.Write a program in python to remove all duplicate lines from the file "story.txt".
def Q33():
    f=open("story.txt","r")
    a=f.readlines()
    j=[]
    for i in a:
        if i not in j:
            j.append(i)
    
    f.close()
    f=open("story.txt",'w')
    f.writelines(j)

#Q33()
        
#34.Write a program in python to display only unique words from the file "story.txt".

def Q34():
    
#35.Write a program in python to count the frequency of each vowels in a file "task.txt".

def Q35():
    f=open("story.txt","r")
    j=f.readlines()
    f.close()
    a=0
    e=0
    i=0
    o=0
    u=0
    l=['e',"e","E","E"]
    for x in j:
        y=len(x)
        l=['a',"a",'A',"A"]
        for z in range(y):
            if x[z] in l:
                
                a+=1
        
        l=['e',"e","E","E"]
    
        for z in range(y):
            if x[z] in l:
                
                e+=1

        l=['i',"i",'I',"I"]

        for z in range(y):
            if x[z] in l:
                
                i+=1

        l=['o',"o",'O',"O"]
        for z in range(y):
            if x[z] in l:
                
                o+=1
        
        l=['U',"U",'u',"u"]
        
        for z in range(y):
            if x[z] in l:
                
                u+=1
              

    print("a:",a,"e:",e,"i:","o:",o,"u:",u)
Q35()


"""



36.Write a program in python to count those words whose length is more than 7 characters in a file "story.txt".

37.Write a program in python to count those lines from the file"div.txt"

38.which are starting from 'T' or 'M'. Write a program in python to count those lines from the file "div.txt" which are not starting from 'M'.

39.Write a program in python to display those words from a file "image. txt" which are ending from alphabet 'm'.

40.Write a program in python to read all lines of file "data.txt" using readline() only.

41.Write a program in Python to copy the entire conten file "data.txt" to "story.txt". AG

42.Write a program in Python to copy the alternate lines from file "data.txt" to "story.txt".

43.Write a program in Python to read the entire content from file "data. txt" and copy the contents to "story.txt" in upper case.

44.Write a program in Python to read the entire content from file "data.txt" and copy only those words to "story.txt" which start from vowels.

45.Write a program in Python write a program in python to read the entire content from file"data.txt" and copy only those words in separate lines to "story.txt" which are starting from lower case alphabets.

46.Write a function disp_mob(model no.) in Python which will display the record of a mobile from "mobile.dat" whose model number (integer type) is passed as an argument. Structure of "mobile.dat" is [Mobile id, Mobile brand, Model No., Price]

47.Write a menu driven program which shows all operations on Binary File
        
    1. Add Record

    2. Display All Record

    3. Display Specific Record

    4. Modify Record

    5. Delete Record

    Use "data.dat" file which stores the record of "Hotel" in the for list containing Room_no, Price, Room_type.

48.Write a function disp75() in Python to display only those records of students from file "school.dat" who scored more than 75 percent marks. Structure stored in "school.dat" is in the form list containing information like [rollno, name, class, percentage].

49.Write a program in Python which display the longest line from file "star.txt".

50.Consider a binary file "data.dat" which stores the record of

    "Hotel" in the form of list containing Room_no, Price, Room_type.

    Do the following task in a file

    1. Write a function addrec() to add a record in a file.

    2. Write a function disp() to display all the records from the file.

    3. Write a function specific disp(room no) which takes room number as argument and display its details.

    4. Write a function mod(room no) which takes room number as argument and modify it's details,

    5. Write a function del (room_no) which takes room number as argument and delete it's record from file "data dat".

"""






























