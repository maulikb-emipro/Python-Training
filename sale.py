from tax import Tax
import re
import datetime

class Sell(Tax):
    "Class for collecting data about sell of Product"
    
    sell_details={}
    def sell(self,pro_type,quantity,name,price):
        """
        func :- This function is called from product class when product is sold.
        params :- product type - string
        params :- product quantity - integer
        params :- customer name - string
        params :- selling price - integer
        returns :- sell order number.
        """
        tempDictionary={}
        tempDictionary['price']=price*quantity
        tempDictionary['total_tax']=self.get_tax(pro_type,tempDictionary['price'],'sell')
        
        order=list(sorted(self.sell_details.keys()))
        if order==[]:
            key='SO/0001'
        else:
            number=re.findall('\d+', order[-1])[0]
            number=int(number)+1
            key='SO/'+str(number).zfill(4)
            
        tempDictionary['date']=datetime.date.today().strftime("%d/%m/%Y")
        tempDictionary['name']=name
        tempDictionary['quantity']=quantity
        tempDictionary['total_price']=tempDictionary['price']+tempDictionary['total_tax']
        tempDictionary['unit_price']=tempDictionary['total_price']/quantity
        
        self.sell_details[key]=tempDictionary
        
        return tempDictionary['total_price']

        