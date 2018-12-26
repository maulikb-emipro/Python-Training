from sell import Sell
from purchase import Purchase
from manufacture import Manufacture
from product import Product
from pytz import timezone
import datetime
import pytz

class My_company(Sell,Purchase,Manufacture,Product):
    """ This class handles all product operations """
    
    company_data={}
    def __init__(self,name,city,state,country,tzone):
        """
        func :- It initializes data of company.
        params :- company name - string
        params :- city - string
        params :- state - string
        params :- country - string
        params :- timezone - string
        returns :- nothing
        """
        self.company_data={'name':name,'city':city,'state':state,'country':country,'tzone':tzone,'total_sell':0,'total_investment':0,'total_profit':0}
        super(My_company, self).__init__('Watch','stockable',50,10)
        super(My_company, self).__init__('Diamond','stockable',50,15)
        
    def create_manufacture_order(self,new_product,raw_material,quantity,price):
        """
        func :- checks for raw material is available or not.
        params :- new product name - string
        params :- raw material name and quantity - dictionary
        params :- quantity - integer
        returns :- calls super method if available Or Error msg if not enough raw material.    
        """
        tempList=[]
        for products in raw_material:
            if products['quantity']<=self.products_data[products['name']]['onhand']:
                tempList.append(1)
            else:
                tempList.append(0)
                
        if not 0 in tempList:
            order=super(My_company, self).create_manufacture_order(new_product,raw_material,quantity,price)
            print(order,"is Confirmed.")
            
            if self.start_manufacturing(order):
                print(order,"is in Progress")
                
            if self.done_manufacturing(order):
                print(order,"is Done!")
        else:
            print("Not Enough Quantity")
            
    def create_purchase_order(self,products,vendor_name):
        """
        func :- Used to add new purchase order
        params :- products' names, quantity, type and price - dictionary
        params :- vendor name - string
        returns :- calls super method and confirms the purchase
        """
        order=super(My_company, self).create_purchase_order(products,vendor_name)
        if order:
            if self.confirm_purchase_order(order):  
                print("Purchase Successful.")
                print("Order No :-",order)
                
    def create_sell_order(self,products,customer_name):
        """
        func :- Used to add new sell order
        params :- products' names, quantity, discount and price - dictionary
        params :- customer name - string
        returns :- calls super method and confirms the sell
        """
        tempList=[]
        for product in products:
            if product['quantity']<=self.products_data[product['name']]['onhand'] and product['discount']<=self.products_data[product['name']]['max_discount']:
                tempList.append(1)
            else:
                tempList.append(0)
                
        if not 0 in tempList:
            order=super(My_company, self).create_sell_order(products,customer_name)
            if order:
                if self.confirm_sell_order(order):  
                    print("Sell Successful.")
                    print("Order No :-",order)
                
        else:
            print("Not Enough Quantity")
        
    def suggest_purchase(self):
        """
        func :- Suggests purchasing products which have not minimum stock available
        params :- nothing
        returns :- list of products
        """
        suggested_products=[]
        for product,data in self.products_data.items():
            if data['type']=='stockable' and data['onhand']<data['minimum_stock']:
                suggested_products.append(product)
        print("You should purchase",suggested_products)
        
    def get_manufacturing_orders(self,product_name=None,dateFrom=datetime.date.min,dateTo=datetime.date.today(),ascending=1,descending=0):
        """
        func :- Gives manufactured orders list as filter if given.
        params :- product name - string - optional
        params :- datefrom - date - optional
        params :- dateto - date - optional
        returns :- List of orders as given filter
        """
        results={}
        temp=1 if product_name==None else 0
        for order_no,order in self.manufacture_details.items():
            current_timezone=pytz.utc.localize(order['date']).astimezone(timezone(self.company_data['tzone'])).date()
            product_name=order['name'] if temp else product_name
            if order['name']==product_name and dateFrom<=current_timezone<=dateTo:
                results.update({order_no:order})
                
        if ascending:
            results=sorted(results.items(),key=lambda key:key[1]['date'])
        if descending:
            results=sorted(results.items(),key=lambda key:key[1]['date'],reverse=True)
        return results
    
    def get_sell_orders(self,product_name=None,dateFrom=datetime.date.min,dateTo=datetime.date.today(),customer=None,state=None,ascending=1,descending=0):
        """
        func :- Gives sell orders list as filter if given.
        params :- product name - string - optional
        params :- datefrom - date - optional
        params :- dateto - date - optional
        params :- customer name - string - optional
        params :- order state - string - optional
        returns :- List of orders as given filter
        """
        results={}
        temp=1 if product_name==None else 0
        temp1=1 if customer==None else 0
        temp2=1 if state==None else 0
        for order_no,order in self.sell_details.items():
            customer=order['customer_name'] if temp1 else customer
            state=order['state'] if temp2 else state
            current_timezone=pytz.utc.localize(order['date']).astimezone(timezone(self.company_data['tzone'])).date()
            if dateFrom<=current_timezone<=dateTo and order['customer_name']==customer and order['state']==state:
                for product in order['products']:
                    product_name=product['name'] if temp else product_name
                    if product['name']==product_name:
                        results.update({order_no:order})
                        
        if ascending:
            results=sorted(results.items(),key=lambda key:key[1]['date'])
        if descending:
            results=sorted(results.items(),key=lambda key:key[1]['date'],reverse=True)
        return results
    
    def get_purchase_orders(self,product_name=None,dateFrom=datetime.date.min,dateTo=datetime.date.today(),vendor=None,state=None,ascending=1,descending=0):
        """
        func :- Gives purchase orders list as filter if given.
        params :- product name - string - optional
        params :- datefrom - date - optional
        params :- dateto - date - optional
        params :- vendor name - string - optional
        params :- order state - string - optional
        returns :- List of orders as given filter
        """
        results={}
        temp=1 if product_name==None else 0
        temp1=1 if vendor==None else 0
        temp2=1 if state==None else 0
        for order_no,order in self.purchase_details.items():
            vendor=order['vendor_name'] if temp1 else vendor
            state=order['state'] if temp2 else state
            current_timezone=pytz.utc.localize(order['date']).astimezone(timezone(self.company_data['tzone'])).date()
            if dateFrom<=current_timezone<=dateTo and order['vendor_name']==vendor and order['state']==state:
                for product in order['products']:
                    product_name=product['name'] if temp else product_name
                    if product['name']==product_name:
                        results.update({order_no:order})

        if ascending:
            results=sorted(results.items(),key=lambda key:key[1]['date'])
        if descending:
            results=sorted(results.items(),key=lambda key:key[1]['date'],reverse=True)                       
        return results
    
    def get_product_stock(self,product_name=None):
        """
        func :- Displays stock of product
        params :- product name - string - optional
        returns :- Stock of product
        """
        product_stock={}
        temp=1 if product_name==None else 0
        for product_nm,product_data in self.products_data.items():
            product_name=product_nm if temp else product_name
            if product_nm==product_name:
                product_stock.update({product_nm:product_data['onhand']})
                
        return product_stock
    
    def get_sale_purchase_account_data(self):
        """
        func :- Gives all account data of company.
        params :- Nothing.
        returns :- Total sell, Total Purchase, Total investment in Dictionary
        """
        tempDict={'total_sell':self.company_data['total_sell'],'total_investment':self.company_data['total_investment'],'total_profit':self.company_data['total_profit']}
        return tempDict
    
    def get_most_selling_product(self,dateFrom=datetime.date.min,dateTo=datetime.date.today()):
        """
        func :- Gives Most selling Product
        params :- datefrom - date - optional
        params :- dateto - date - optional
        returns :- Most selling product
        """
        most_sold_product={}
        quantity=0
        for order in self.sell_details.values():
            current_timezone=pytz.utc.localize(order['date']).astimezone(timezone(self.company_data['tzone'])).date()
            if dateFrom<=current_timezone<=dateTo:
                for product in order['products']:
                    if product['quantity']>quantity:
                        quantity=product['quantity']
                        most_sold_product.update({product['name']:quantity})
                    
        return most_sold_product
        

emipro=My_company('Emipro Watches','Rajkot','Gujarat','India','Asia/Kolkata')

raw_material=[{'name':'Watch','quantity':5},{'name':'Diamond','quantity':2}]
order=emipro.create_manufacture_order('Diamond Watch', raw_material, 5,25)

products=[{'name':'Gold','type':'consumable','quantity':10,'price':20}]
emipro.create_purchase_order(products, 'Gold Miners')

emipro.suggest_purchase()

products=[{'name':'Watch','quantity':10,'price':15,'discount':5},{'name':'Diamond Watch','quantity':2,'price':30,'discount':7}]
emipro.create_sell_order(products, 'Maulik')
emipro.create_sell_order(products,'AKM')

manufacture_orders=emipro.get_manufacturing_orders()

sell_orders=emipro.get_sell_orders()

purchase_orders=emipro.get_purchase_orders(vendor="Gold Miners")

stock=emipro.get_product_stock()

most_selling_product=emipro.get_most_selling_product()

print(emipro.products_data)
print(emipro.company_data)
print(emipro.get_sale_purchase_account_data())

