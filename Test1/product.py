class Product:
    """ This class used to store product details """
    
    products_data={}
    def __init__(self,name,type,on_hand,sell_price,purchase_tax=15,sell_tax=17,max_purchase=1000,max_discount=10):
        """
        func :- initializes product object
        params :- name - string
        params :- type - string
        params :- sell_price - integer
        params :- purchase_tax - integer - optional(Default)
        params :- sell_tax - integer - optional(Default)
        params :- on hand quantity - integer
        params :- max_purchase - integer - optional(Default)
        params :- max_discount - integer - optional(Default)
        returns :- nothing
        """
        self.products_data.update({name:{'type':type,'onhand':on_hand,'sell_price':sell_price,'purchase_tax':purchase_tax,'sell_tax':sell_tax,'max_purchase':max_purchase,'max_discount':max_discount,'manufacture_order':[],'sell_order':[],'purchase_order':[],'total_sell':0}})
        if type.lower()=='stockable':
            self.products_data[name].update({'minimum_stock':50})
        self.company_data['total_investment']+=sell_price*on_hand
            
