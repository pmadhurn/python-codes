def Q5():
#ip l b h from user find area and perminteter

    ln = eval(input("Enter Length :"))
    b=eval(input("Enter Breath :"))
    h=eval(input("Enter Height :"))

    a=2*(ln*b+b*h+h*ln)
    p=4*(ln+b+h)

    print("THE PERIMETER OF A CUBOID IS {:.2f} AND THE AREA IS {:.2f}".format(p,a))
#Q5()

#ip total amt from user and count no of notes
def Q6():

    a=int(input("Enter the Amount for which you want to count the Notes: "))
    b=a%500
    c=a/500

    d=b%200
    e=b/200

    f=d%100
    g=d/100

    g=f%50
    h=f/50

    i=g%20
    j=g/20

    k=i%10
    l=i/10

    print("The Number of 500 rupee Notes will be :{:.0f}\nThe Number of 200 rupee Notes will be :{:.0f}\nThe Number of 100 rupee Notes will be :{:.0f}\nThe Number of 50 rupee Notes will be :{:.0f}\nThe Number of 20 rupee Notes will be :{:.0f}\nThe Number of 10 rupee Notes will be :{:.0f}\n".format(c,e,g,h,j,l))

#Q6()