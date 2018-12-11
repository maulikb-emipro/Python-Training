from sale import Sell
from purchase import Purchase
import math

class Product(Sell,Purchase):
    "Class Handles all operation on Product"
    product={}
    
    def __init__(self,name,product_type,quantity,price):
        """
        func :- Defines product name, type and quantity.
        params :- product Name -string
        params :- product Type - string
        params :- product Quantity - integer
        params :- product price - integer
        returns :- nothing.
        """
        total_value=price*quantity
        self.product.update({'name':name,'type':product_type,'available_qty':quantity,'sell_order':[],'purchase_order':[],'profit_loss':0,'valuation_price':total_value,'purchase_value':total_value,'sell_value':0})
        if self.product['type'].lower()=='service':
            self.product['available_qty']=0
            self.product['valuation_price']=0
    
    def sell(self,quantity,name,price):
        """
        func :- Function is called, when product is sold. It will call super method of Sell class and fetch sale order number.
        params :- product quantity - integer
        params :- customer name - string
        params :- selling price - integer 
        returns :- nothing
        """
        if self.product['available_qty']>=quantity:
            sell_value=super(Product, self).sell(self.product['type'],quantity,name,price)
            self.product['sell_order']=list(self.sell_details.keys())
            print(self.sell_details)
            if not self.product['type'].lower()=='service':
                valuation=self.product['valuation_price']*quantity/self.product['available_qty']
                
                self.product['profit_loss']=math.ceil(sell_value-valuation)
                self.product['valuation_price']=math.ceil(self.product['valuation_price']-valuation)
                self.product['available_qty']-=quantity
                self.product['sell_value']+=sell_value
            else:
                self.product['profit_loss']=sell_value
        else:
            print("Only",self.product['available_qty'],self.product['name'],"Available.")
        
    def purchase(self,quantity,name,price):
        """
        func :- This function is called from product class when product is purchased.
        params :- product quantity - integer
        params :- vendor name - string
        params :- purchasing price - integer 
        returns :- nothing
        """
        if not self.product['type'].lower()=='service':
            purchase_value=super(Product, self).purchase(quantity,name,price)
            self.product['purchase_order']=list(self.purchase_details.keys())
            print(self.purchase_details)
            self.product['purchase_value']+=purchase_value
            self.product['valuation_price']+=purchase_value
            self.product['available_qty']+=quantity
            
        else:
            print("You can't purchase Service.")
        
# product_obj=Product('Wood','consumable',50,18)
# product_obj.purchase(10,"Maulikbhai", 25)
# product_obj.sell(10, "Baradbhai", 20)
# product_obj.purchase(10,"Maulikbhai", 15)
# print(product_obj.product)

product_name = input("Enter Product name :-")
product_type=input("Enter Product Type :-")
product_quantity = int(input("Enter Product quantity :-"))
product_price=int(input("Enter Product price :-"))

product_obj = Product(product_name,product_type, product_quantity,product_price)

while 1:
    print("Enter number from below options :- \n\t 1.Sell a Product \n\t 2.Purchase Product \n\t 3.Exit")
    option = int(input("Enter option number :- "))
    
    if option == 1:
        sell_quantity = int(input("Enter selling quantity of product:-"))
        name=input("Enter Customer Name :-")
        price=int(input("Enter product price :-"))
        product_obj.sell(sell_quantity, name, price)
        
    elif option == 2:
        puchase_quantity = int(input("Enter purchasing product quantity :-"))
        name=input("Enter Vendor Name :-")
        price=int(input("Enter product's purchasing price :-"))
        product_obj.purchase(puchase_quantity,name,price)
        
    elif option == 3:
        print(product_obj.product)
        
    elif option==4:
        break
    else:
        print("Please, select valid option.")
