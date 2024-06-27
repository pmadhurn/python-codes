def Password():
    i=0
    while True:
        i=i+1
        
        if i<10:
            print("for character No {} ".format(i))
            
            a=int(input("enter the single digit charater :"))

            b=a*a
            c=b%10

            print("{} is the {} character for after the decryption.\n".format(c,i))
        
        elif i==10:
            a=input("enter the special character :")
            print("{} is the 10th character.".format(a))

        elif 10<i<20:
            
            a=input("enter the character : ")
            b=chr(ord(a) - 1)
            print("{} is the {} th character.".format(b,i))

    
        else:
            break

#Password()


def TASK2():
    a=input("ENTER YOUR NAME:")
    print("WELCOME ---{}---".format(a))
    b=int(input("ENTER THE TONNES OF GOLD AND IT SHOULD BE LESS THAN 94 TONNES : "))

    c=int(b/10)
    d=b%10
    e=int(d/5)
    f=int(d%5)

    print("Bags of 10 tons needed (N): {}".format(c))
    print("Bags of 5 tons needed (M): {}".format(e))
    print("Bags of 1 tons needed (O): {}".format(f))
    rio=0
    malina=0
    helinski=0
    paleramo=0
    tokyo=0

    if c>6:
        helinski=6
        c=c-6
        paleramo=c
        tokyo=e
        malina=f
    else:
        helinski=c
        paleramo=e
        tokyo=f

    print("Members to hold bags : ")
    print("\tMEMBER\t\t|\tNUMBER OF BAGS")
    print("\tHLENSIKI\t|\t{}".format(helinski))
    print("\tPALERMO\t\t|\t{}".format(paleramo))
    print("\tTOKYO\t\t|\t{}".format(tokyo))
    print("\tMANILA\t\t|\t{}".format(malina))
    print("\tRIO\t\t|\t{}".format(rio))
    



TASK2()