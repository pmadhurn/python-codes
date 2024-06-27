#Grocery store capstone project
def Capstone1():
    print("Welcome to Grocery Store")
    name={'Bread':['price':30,'quantity':50], 'Cheese','Cheese','Biscuit','Flour','Chocolate'}
    print("Options:")
    print("1.Add a new product\t \n2.Update product quantity\t\n3.View Inventory\t\n4.Generate reports\t\n5.Exit")
    a=eval(input("Choose your option: \n"))
    if a==1:
        print("Add a new product")
        p=input("Enter product :")
        pr=eval(input("Enter price :"))
        if p in name:
            print("Error")
        else:
            print("Adding the product in the stock")
            d1={}  #dictionary name
            d1.update({p:pr})
            print(d1.items())
            '''name.append() #Add in list
            print(name) # here append in the name list is not happening'''
    elif a==2:
        print("Update Product Quantity")
        p=input("Enter product :")
        for i in name:
            if p==i:
                q=eval(input("Enter New Quantity :"))
                q1=q
                print(q1)
            elif p!=i:
                print("Error")
                break
            '''here error is getting printed even if the product exists'''
    elif a==3:
        print("View Inventory")
        for j in name and x in Qt and y in price:
            print(j,x,y)
                                                    
Capstone1()