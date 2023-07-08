#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Product:
    def __init__(self, name, price, quantity,day):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.day = day
        

class BillingSystem:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def calculate_total(self):
        total = 0
        for product in self.products:
            total += product.price * product.quantity
        return total

    def print_receipt(self, product):
        print("Items\tNumber of Items\tPrice of Item\tTotal Price\tDiscount")
        if(product.day==1):
            for product in self.products:
                print(f"{product.name}\t{product.quantity}\t\t{product.price}\t\t{product.price * product.quantity}\t\t{product.price * product.quantity*0.2}")
            
            print("=====================================================")
            print(f"Final Price: {self.calculate_total()-(product.price * product.quantity*0.2)}")
            print("=====================================================")
        if(product.day==2):
            for product in self.products:
                print(f"{product.name}\t{product.quantity}\t\t{product.price}\t\t{product.price * product.quantity}\t\t{product.price * product.quantity*0.2}")
            
            print("=====================================================")
            print(f"Final Price: {self.calculate_total()-(product.price * product.quantity*0.3)}")
            print("=====================================================")
        if(product.day==3):
            for product in self.products:
                print(f"{product.name}\t{product.quantity}\t\t{product.price}\t\t{product.price * product.quantity}\t\t{product.price * product.quantity*0.2}")
            
            print("=====================================================")
            print(f"Final Price: {self.calculate_total()-(product.price * product.quantity*0.15)}")
            print("=====================================================")
        if(product.day==4):
            for product in self.products:
                print(f"{product.name}\t{product.quantity}\t\t{product.price}\t\t{product.price * product.quantity}\t\t{product.price * product.quantity*0.2}")
            
            print("=====================================================")
            print(f"Final Price: {self.calculate_total()-(product.price * product.quantity*0.14)}")
            print("=====================================================")
        if(product.day==5):
            for product in self.products:
                print(f"{product.name}\t{product.quantity}\t\t{product.price}\t\t{product.price * product.quantity}\t\t{product.price * product.quantity*0.2}")
            
            print("=====================================================")
            print(f"Final Price: {self.calculate_total()-(product.price * product.quantity*0.18)}")
            print("=====================================================")
        if(product.day==6):
            for product in self.products:
                print(f"{product.name}\t{product.quantity}\t\t{product.price}\t\t{product.price * product.quantity}\t\t{product.price * product.quantity*0.2}")
            
            print("=====================================================")
            print(f"Final Price: {self.calculate_total()-(product.price * product.quantity*0.17)}")
            print("=====================================================")
        if(product.day==7):
            for product in self.products:
                print(f"{product.name}\t{product.quantity}\t\t{product.price}\t\t{product.price * product.quantity}\t\t{product.price * product.quantity*0.2}")
            
            print("=====================================================")
            print(f"Final Price: {self.calculate_total()-(product.price * product.quantity*0.18)}")
            print("=====================================================")

    
billing_system = BillingSystem()
count=0
while True:
    c=int(input("Enter 1 to continue(for Exit press stop):"))
    print()
    if c!=1:
        break
    
    else:
        x=input("Enter Product Name:")
        while(x==""):
            x=input("Please Enter name first:")
        y=int(input("Enter Product Price:"))
        
        z=int(input("Enter Product Quantity:"))
        day=int(input("Choose day:\n1_Monday \n2_Tuesday \n3_Wednesday \n4_Thursday \n5_Friday \n6_Saturday \n7_Sunday \nEnter number:"))
        print()
        temp=Product(x,y,z,day)
    billing_system.add_product(temp)
    billing_system.print_receipt(temp)
print("===========================  Thankyou  ==============================")


# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


a

