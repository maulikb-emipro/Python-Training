import datetime
import re
class Purchase:
    """ This class used to store purchase of products """
    
    purchase_details={}
    def create_purchase_order(self,products,vendor_name):
        """
        func :- Used to create new purchase order.
        params :- products' names, quantity, type and price - dictionary
        params :- vendor name - string
        returns :- Error msg if more than purchase price else purchase number 
        """
        tempDictionary={}
        tempDictionary['total_price']=0
        
        for product in products:
            if not product['name'] in self.products_data:
                new_product=super(Purchase,self).__init__(product['name'],product['type'],0,product['price'])
            product_price=product['quantity']*product['price']
            tax=product_price*self.products_data[product['name']]['purchase_tax']/100
            product['total_price']=product_price+tax
            tempDictionary['total_price']+=product['total_price']
            if (self.products_data[product['name']])['max_purchase']<product['total_price']:
                if (self.products_data[product['name']])['onhand']==0:
                    del self.products_data[product['name']]
                print("Purchase price limit exceeds...")
                return False
         
        
        tempDictionary['date']=datetime.datetime.utcnow()
        tempDictionary['state']='Confirm'
        tempDictionary['products']=products
        tempDictionary['vendor_name']=vendor_name

        order=list(sorted(self.purchase_details.keys()))
        if order==[]:
            key='PO/0001'
        else:
            number=re.findall('\d+', order[-1])[0]
            number=int(number)+1
            key='PO/'+str(number).zfill(4)
        
        self.purchase_details[key]=tempDictionary
        
        return key
        
    def confirm_purchase_order(self,purchase_order):
        """
        func :- Used to manage purchased products
        params :- purchase order - string
        returns :- True or False as Order confirms 
        """
        order=self.purchase_details[purchase_order]
        order['state']='Done'
        for product in order['products']:
            pro_data=self.products_data[product['name']]
            pro_data['onhand']+=product['quantity']
            self.products_data[product['name']]['purchase_order'].append(purchase_order)
        
        
        return True
        