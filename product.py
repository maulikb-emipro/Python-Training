class product:
    "It manages inventory of product"
    quantity = 0
    product_name = ''
    
    def __init__(self, name, quantity=quantity):
        """
        func :- Constructure for initializing Product name & quantity.
        param :- name - string.
        param :- quantity - it must be an integer.
        returns :- nothing.
        """
        self.product_name = name
        self.quantity = quantity
    
    def sales(self, quantity):
        """
        func :- It will check for sufficient quantity of product to sell it.
        param :- quantity - must be integer. 
        return :- a message, if there is enough quantity then sold, otherwise insufficient material.
        """
        if(self.quantity > quantity):
            self.quantity = self.quantity - quantity
            print("Product is sold.")
        else:
            print("Insufficient product to sell. Please, purchase some", self.product_name, ".")
        self.final_count()
            
    def purchase(self, quantity):
        """
        func :- It adds new purchased product to current quantity.
        param :-  product quantity that you want to purchase.
        return :- message of successful purchase. 
        """
        self.quantity = self.quantity + quantity
        print("Purchase Successful.")
        self.final_count()
        
    def final_count(self):
        """
        func :- This method gives information about product inventory.
        param :- No params needed.
        return :- message with total stock of product.
        """
        print("There is", self.quantity, self.product_name, "left in Stock.")
        
product_name = input("Enter Product name :-")
product_quantity = int(input("Enter Product quantity :-"))
product_obj = product(product_name, product_quantity)
count = 1
while count == 1:
    print("Enter number from below options :- \n\t 1.Sell a Product \n\t 2.Purchase Product \n\t 3.Show Product Quantity \n\t 4.Exit")
    option = int(input("Enter option number :- "))
    if option == 1:
        sales_quantity = int(input("Enter selling quantity of product:-"))
        product_obj.sales(sales_quantity)
    elif option == 2:
        puchase_quantity = int(input("Enter purchasing product quantity :-"))
        product_obj.purchase(puchase_quantity)
    elif option == 3:
        product_obj.final_count()
    elif option == 4:
        count = 0
    else:
        print("Please, select valid option.")
