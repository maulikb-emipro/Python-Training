import math
class Product:
    "Manages inventory of product using Dictionary with FIFO"
    product={}
        
    def purchase(self,price,quantity):
        """
        func :- Purchasing Product with different prices.
        param :- price of product - integer.
        param :- quantity of product - integer.
        returns :- nothing.
        """
        if not self.product:
            product_index=1
        else:
            product_index=(sorted(self.product.keys(),reverse=True)[0])+1
        self.product.update({product_index:{'price':price,'quantity':quantity}})
        
    def sales(self,qty):
        """
        func :- selling Product from inventory by FIFO method.
        param :- selling product quantity - integer.
        returns :- nothing.
        """
        for purchase_index,product in self.product.items():
            if product['quantity']>=qty:
                product['price']=product['price']-int(product['price']*qty/product['quantity'])
                product['quantity']-=qty
                break
            else:
                qty-=product['quantity']
                self.product.pop(purchase_index)
    
    def valuation(self):
        """
        func :- Valuation of Product from inventory.
        param :- No params.
        returns :- valuation of product.
        """
        total_price=0
        total_qty=0
        for product in self.product.values():
            total_price=total_price+product['price']
            total_qty=total_qty+product['quantity']
        value=math.ceil(total_price/total_qty)
        print(self.product)
        return value;
        
product_obj=Product()
product_obj.purchase(200,10)
product_obj.purchase(100,5)
product_obj.purchase(350,20)
while 1:
    print("Enter number from below options :- \n\t 1.Sell a Product \n\t 2.Purchase Product \n\t 3.Show Product Valuation \n\t 4.Exit")
    option = int(input("Enter option number :- "))
    if option == 1:
        sales_quantity = int(input("Enter selling quantity of product:-"))
        product_obj.sales(sales_quantity)
        print("Products sold.")
    elif option == 2:
        price=int(input("Enter price of product :-"))
        puchase_quantity = int(input("Enter purchasing product quantity :-"))
        product_obj.purchase(price,puchase_quantity)
        print("Purchase Successful.")
    elif option == 3:
        print("Valuation of product is",product_obj.valuation())
    elif option == 4:
        break
    else:
        print("Please, select valid option.")