import datetime
import calendar
import re
import math
class Sell:
    """ This class handles selling of product """
    
    sell_details={}
    def create_sell_order(self,products,customer_name):
        """
        func :- Used to add new sell order
        params :- products' names, quantity, discount, type and price - dictionary
        params :- customer name - string
        returns :- True or False
        """
        tempDictionary={}
        tempDictionary['date']=datetime.datetime.utcnow()
        tempDictionary['state']='Confirm'
        tempDictionary['products']=products
        tempDictionary['customer_name']=customer_name
        tempDictionary['total_price']=0
        
        c=calendar.Calendar()
        daylist=c.monthdatescalendar(2018,12)
        saturdays=[date for datelist in daylist for date in datelist if date.weekday()==5 and date.month==12]
        
        for product in products:
            product_price=product['quantity']*product['price']
            discount=product_price*product['discount']/100
            if tempDictionary['date'].date()==saturdays[1] or tempDictionary['date'].date()==saturdays[3]:
                discount+=product_price/100
            price_after_discount=product_price-discount
            
            tax=price_after_discount*self.products_data[product['name']]['sell_tax']/100
            product['total_price']=math.ceil(price_after_discount+tax)
            tempDictionary['total_price']+=product['total_price']
            
            base_value=self.products_data[product['name']]['sell_price']*product['quantity']
            self.company_data['total_profit']+=math.ceil(price_after_discount-base_value)
        
        order=list(sorted(self.sell_details.keys()))
        if order==[]:
            key='SO/0001'
        else:
            number=re.findall('\d+', order[-1])[0]
            number=int(number)+1
            key='SO/'+str(number).zfill(4)
        
        self.sell_details[key]=tempDictionary
            
        return key
            
    def confirm_sell_order(self,sell_order):
        """
        func :- Used to manage purchased products
        params :- sell order - string
        returns :- True or False as Order confirms 
        """
        order=self.sell_details[sell_order]
        order['state']='Done'
        for product in order['products']:
            pro_data=self.products_data[product['name']]
            pro_data['onhand']-=product['quantity']
            self.products_data[product['name']]['sell_order'].append(sell_order)
            self.products_data[product['name']]['total_sell']+=product['quantity']
            
        self.company_data['total_sell']+=order['total_price']
        
        return True
            
            
            