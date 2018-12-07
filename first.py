class manufacturing:
    'Managing raw material quantity'
    quantity = 0
    row_material = ''
    
    def __init__(self, name, quantity=quantity):
        """
        func :- Constructure for initializing Material name & quantity.
        param :- name - string.
        param :- quantity - it must be an integer.
        returns :- nothing.
        """
        self.row_material = name
        self.quantity = quantity
    
    def produce(self, quantity):
        """
        func :- It will take needed raw material quantity to manufacture a product & check for sufficient quantity.
        param :- needed raw material quantity - must be integer. 
        return :- a message, if there is enough quantity then successfull, otherwise insufficient material.
        """
        if(self.quantity > quantity):
            self.quantity = self.quantity - quantity
            print("Production Successful.")
        else:
            print("Insufficient material to manufacture new product. Please, purchare some quantity.")
        self.get_stock()
            
    def get_stock(self):
        """
        func :- This method gives information about raw material inventory.
        param :- No params needed.
        return :- message with total stock of raw material.
        """
        print "There is", self.quantity, self.row_material, "left in Stock."
        
    def purchase(self, quantity):
        """
        func :- It adds new purchased material to current raw material quantity.
        param :-  raw material quantity that you want to purchase.
        return :- message of successful purchase. 
        """
        self.quantity = self.quantity + quantity
        print("Purchase Successful.")
        self.get_stock()
        
raw_material = input("Enter raw material name :-")
raw_material_quantity = int(input("Enter raw material quantity :-"))
manufacture_obj = manufacturing(raw_material, raw_material_quantity)
count = 1
while count == 1:
    print("Enter number from below options :- \n\t 1.Manufacture a Product \n\t 2.Purchase Raw Material \n\t 3.Show Raw Material Quantity \n\t 4.Exit")
    option = int(input("Enter option number :- "))
    if option == 1:
        production_quantity = int(input("Enter required raw material quantity :-"))
        manufacture_obj.produce(production_quantity)
    elif option == 2:
        puchase_quantity = int(input("Enter purchasing raw material quantity :-"))
        manufacture_obj.purchase(puchase_quantity)
    elif option == 3:
        manufacture_obj.get_stock()
    elif option == 4:
        count = 0
    else:
        print("Please, select valid option.")

