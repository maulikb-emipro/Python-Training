from testing.cgst import c_gst
from testing.sgst import s_gst

class sales(s_gst,c_gst):
    "Gives price with all taxes added"

    def sale(self, price):
        """
        func :- Give details of selling product.
        param :- price of product - must be integer.
        return :- Details of product.
        """
        total_tax = self.get_tax(price)
        amount = price + total_tax
        print("Final Amount is", amount)

    def get_tax(self, price):
        """
        func :- Calculates Taxes.
        param :- price of product - must be integer.
        return :- Total of all taxes.
        """
        print("sales")
        super().get_tax(price)
        


sales_obj = sales()
product_price = int(input("Enter price of Product :- "))
sales_obj.sale(product_price)
