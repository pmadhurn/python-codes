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

































