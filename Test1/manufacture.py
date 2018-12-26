import re
import datetime
from product import Product
class Manufacture:
    """ It is used to manufacture products """
    
    manufacture_details={}
    def create_manufacture_order(self,new_product,raw_material,quantity,price):
        """
        func :- Manufactures new product.
        params :- new product name - string
        params :- raw material name and quantity - dictionary
        params :- quantity - integer
        returns :- Manufacture order number    
        """
        tempDictionary={}
        tempDictionary['date']=datetime.datetime.utcnow()
        tempDictionary['state']='Confirm'
        tempDictionary['material']=raw_material
        tempDictionary['name']=new_product
        tempDictionary['quantity']=quantity
        tempDictionary['price']=price
        
        order=list(sorted(self.manufacture_details.keys()))
        if order==[]:
            key='MO/0001'
        else:
            number=re.findall('\d+', order[-1])[0]
            number=int(number)+1
            key='MO/'+str(number).zfill(4)
        
        self.manufacture_details[key]=tempDictionary
        
        return key
    
    def start_manufacturing(self,manufacture_order):
        """
        func :- Subtracts raw material from on hand quantity.
        params :- order number - string
        returns :- True or false as manufacturing started.
        """
        order=self.manufacture_details[manufacture_order]
        order['state']='In Progress'
        for material in order['material']:
            self.products_data[material['name']]['onhand']-=material['quantity']
        return True        
        
    def done_manufacturing(self,manufacture_order):
        """
        func :- Manages manufactured product.
        params :- order number - string
        returns :- True or false as manufacturing done.
        """
        order=self.manufacture_details[manufacture_order]
        order['state']='Done'
        if order['name'] in self.products_data:
            self.products_data[order['name']]['onhand']+=order['quantity']
            (self.products_data[order['name']])['manufacture_order'].append(manufacture_order)
        else:
            new_product=super(Manufacture, self).__init__(order['name'],'stockable',order['quantity'],order['price'])
            (self.products_data[order['name']])['manufacture_order'].append(manufacture_order)
        return True
        