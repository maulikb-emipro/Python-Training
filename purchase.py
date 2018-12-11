from tax import Tax
import re
from _datetime import datetime

class Purchase(Tax):
    "It collects data of purchasing Product"
    
    purchase_details={}
    def purchase(self,quantity,name,price):
        """
        func :- This function is called from product class when product is purchased.
        params :- product type - string
        params :- product quantity - integer
        params :- vendor name - string
        params :- purchasing price - integer 
        returns :- purchase order number.
        """
        tempDictionary={}
        tempDictionary['price']=price*quantity
        tempDictionary['total_tax']=self.get_tax('consumable',tempDictionary['price'],'purchase')
        
        order=list(sorted(self.purchase_details.keys()))
        if order==[]:
            key='PO/0001'
        else:
            number=re.findall('\d+', order[-1])[0]
            number=int(number)+1
            key='PO/'+str(number).zfill(4)
            
        tempDictionary['date']=str(datetime.now().date())
        tempDictionary['name']=name
        tempDictionary['quantity']=quantity
        
        self.purchase_details[key]=tempDictionary
        
        return tempDictionary['price']+tempDictionary['total_tax']
        
        