class c_gst():
    "Calculates 18% Central GST"
    def get_tax(self, price):
        """
        func :- Calculates CGST.
        param :- price of product - must be integer.
        return :- Price with CGST
        """
        cgst = price * 18 / 100
        return cgst

class s_gst(c_gst, object):
    "Calculates 12% State GST"
    def get_tax(self, price):
        """
        func :- Calculates SGST.
        param :- price of product - must be integer.
        return :- Price with SGST
        """
        sgst = price * 12 / 100
        cgst = super(s_gst, self).get_tax(price)
        total = sgst + cgst
        return total

class sales(s_gst):
    "Gives price with all taxes added"
    
    def sale(self, price):
        """
        func :- Give details of saling product.
        param :- price of product - must be integer.
        return :- Details of product.
        """
        total_tax = self.get_tax(price)
        amount = price + total_tax
        print "Final Amount is", amount
        
    def get_tax(self, price):
        """
        func :- Calculates Taxes.
        param :- price of product - must be integer.
        return :- Total of all taxes.
        """
        total_tax = super(sales, self).get_tax(price)
        return total_tax

sales_obj = sales()
product_price = int(input("Enter price of Product :- "))
sales_obj.sale(product_price)
